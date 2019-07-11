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



# def sql():
#     con = connect()
#     mes = []
#     new_public_for_one_hour = []
#     try:
#         with con.cursor() as cursor:
#             sql = 'SELECT * FROM products'
#             cursor.execute(sql)
#             for row in cursor:
#                 if row['updated_at'] > time.time() - 3600:
#                     new_public_for_one_hour.append(row)
#                 mes.append(row)
#             return mes, new_public_for_one_hour
#     finally:
#         con.close()
#
#
# def scan_15_min():
#     con = connect()
#     mes_15 = []
#     try:
#         with con.cursor() as cursor:
#             sql = 'SELECT `name`, `price`, `updated_at`, `recommended`, `published`, `id` FROM products'
#             cursor.execute(sql)
#             for row in cursor:
#                 if row['updated_at'] > time.time() - 900:
#                     if row['published'] == 1 and row['recommended'] == 1:
#                         p = row['name'], float(row['price']), 'https://airsofter.world/ru-ru/product/{}'.format(
#                             row['id'])
#                         mes_15.append(p)
#             return mes_15
#     finally:
#         con.close()


# def send_message():
#     msg, new_public_for_one_hour = sql()
#     if not msg:
#         print('Error')
#         return (False, [])
#     else:
#         return (msg, new_public_for_one_hour)


def sender():
    condition = True
    msg_prev = []
    counter = 0
    data_count_15_prev = 0
    data_count_60_prev = 0
    time_now = time.time()

    sql1 = "SELECT `id`, `name`, `price`, `updated_at`, `recommended`, `published`  FROM products WHERE `updated_at` > {} AND `recommended` = {} and `published` = {}".format(
        time_now - 900, 1, 1)
    sql2 = "SELECT `id` FROM products WHERE `updated_at` > {}".format(time_now - 3600)

    while condition:
        data_15 = sql_query(sql1)
        # print(data_15)
        if data_count_15_prev < len(data_15):
            # print('dedeefefevfe', data_15[0][0], data_15[0][1], data_15[0][2])
            # print(('https://airsofter.world/ru-ru/market/index'))
            # print('dwedwdwdw',data_15[0]['name'])
            Tmsg = "Name: {}, Prise: {}, https://airsofter.world/ru-ru/product/{}".format(data_15[0]['name'],
                                                                                          data_15[0]['price'],
                                                                                          data_15[0]['id'])
            # print(Tmsg)
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))
            data_count_15_prev = len(data_15)
        counter += 1
        print(counter)
        time.sleep(900)
        if counter == 4:
            data_60 = sql_query(sql2)
            if data_count_60_prev < len(data_60):
                # print('The site has {} new products'.format(len(data_60)))
                # print(('https://airsofter.world/ru-ru/market/index'))
                Tmsg = 'The site has {} new products'.format(
                    len(data_60)) + ' https://airsofter.world/ru-ru/market/index'
                requests.get(
                    "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))
                data_count_60_prev = len(data_60)
        if counter == 4:
            counter = 0
