import requests
from config import connect
from config import TG_TOKEN, CHAT_ID
import time


def sql_query(query_str):
    con = connect()
    data = []
    try:
        with con.cursor() as cursor:
            sql = query_str
            cursor.execute(sql)
            for row in cursor:
                data.append(row)
            return data
    finally:
        con.close()



def sender():
    condition = True
    counter = 0
    data_count_15_prev = 0
    time_now = 0
    while condition:
        time.sleep(60)
        time_now = time.time()
        send_Tmsg = ''
        sql1 = "SELECT `id`, `name`, `price`, `updated_at`, `recommended`, `published`  FROM products WHERE `updated_at` > {} AND `recommended` = {} and `published` = {}".format(
            time_now - 60, 1, 1)
        sql2 = "SELECT COUNT(`id`) FROM products WHERE `updated_at` > {}".format(time_now - 240)
        data_15 = sql_query(sql1)

        if data_count_15_prev < len(data_15):
            for i in data_15:
                Tmsg = "Name: {}, Prise: {}, https://airsofter.world/ru-ru/product/{}".format(i['name'],
                                                                                              i['price'],
                                                                                              i['id'])
                send_Tmsg +=(Tmsg+ '\n')
                print(send_Tmsg)
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, send_Tmsg))
            data_count_15_prev = len(data_15)
        elif data_count_15_prev > len(data_15):
            for i in data_15:
                Tmsg = "Name: {}, Prise: {}, https://airsofter.world/ru-ru/product/{}".format(i['name'],
                                                                                              i['price'],
                                                                                              i['id'])
                send_Tmsg +=(Tmsg+ '\n')
                print(send_Tmsg)
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, send_Tmsg))
            data_count_15_prev = len(data_15)
        counter += 1
        print(counter)
        if counter == 4:
            data_60 = sql_query(sql2)
            Tmsg = 'The site has {} new products'.format(data_60[0]['COUNT(`id`)']) + ' https://airsofter.world/ru-ru/market/index'
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))

        if counter == 4:
            counter = 0
