import requests
from config import connect
from config import TG_TOKEN, CHAT_ID
import time


def sql():
    con = connect()
    mes = []
    new_public_for_one_hour = []
    try:
        with con.cursor() as cursor:
            sql = 'SELECT * FROM products'
            cursor.execute(sql)
            for row in cursor:
                if row['updated_at'] > time.time() - 3600:
                    new_public_for_one_hour.append(row)
                mes.append(row)
            return mes, new_public_for_one_hour
    finally:
        con.close()

def scan_15_min():
    con = connect()
    mes_15 = []
    try:
        with con.cursor() as cursor:
            sql = 'SELECT `name`, `price`, `updated_at`, `recommended`, `published`, `id` FROM products'
            cursor.execute(sql)
            for row in cursor:
                if row['updated_at'] > time.time() - 900:
                    if row['published'] == 1 and row['recommended'] == 1:
                        p = row['name'], float(row['price']), 'https://airsofter.world/ru-ru/product/{}'.format(row['id'])
                        mes_15.append(p)
            return mes_15
    finally:
        con.close()

def send_message():
    msg, new_public_for_one_hour = sql()
    if not msg:
        print('Error')
        return (False ,[])
    else:
        return (msg, new_public_for_one_hour)

def sender():
    condition = True
    msg_prev = []
    caunter = 0
    msg_15_prev = []
    while condition:
        msg_15 = scan_15_min()
        if len(msg_15_prev) < len(msg_15):
            print('dedeefefevfe',msg_15[0][0], msg_15[0][1], msg_15[0][2])
            print(('https://airsofter.world/ru-ru/market/index'))
            Tmsg = "Name: {}, Prise: {}, {}".format(msg_15[0][0], msg_15[0][1], msg_15[0][2])
            print(Tmsg)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))
            msg_15_prev = msg_15
        caunter += 1
        print(caunter)
        time.sleep(900)
        if caunter == 4:
            msg, new_public_for_one_hour = send_message()
            if len(msg_prev) < len(msg):
                print('The site has {} new products'.format(len(new_public_for_one_hour)))
                print(('https://airsofter.world/ru-ru/market/index'))
                Tmsg = 'The site has {} new products'.format(len(new_public_for_one_hour))+ ' https://airsofter.world/ru-ru/market/index'
                requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))
                msg_prev = msg
        if caunter == 4:
            caunter = 0
