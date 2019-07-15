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
        time.sleep(3)
        time_now = time.time()
        send_Tmsg = ''
        sql1 = "SELECT `id`, `name`, `price`, `updated_at`, `recommended`, `published`, `product_image_one`, `description` FROM products WHERE `updated_at` > {} AND `recommended` = {} and `published` = {}".format(
            time_now - 10, 1, 1)
        sql2 = "SELECT COUNT(`id`) FROM products WHERE `updated_at` > {}".format(time_now - 40)
        data_15 = sql_query(sql1)

        if data_count_15_prev < len(data_15):
            for i in data_15:
                print(i['product_image_one'])
                photo = "https://airsofter.world/images/product-image/{} \n".format(i['product_image_one'])
                Tmsg = "https://airsofter.world/images/product-image/{} Name: {}\nPrise: {}\nhttps://airsofter.world/ru-ru/product/{}".format(
                    i['product_image_one'],
                    i['name'],
                    i['price'],
                    i['id'])

                send_Tmsg += (Tmsg + '\n')

                # send_Tmsg = '[] https://airsofter.world/images/product-image/9/6/6/5cfebb6cbfea8.jpg','Some text here.'

                print(send_Tmsg)
            url = 'https://api.telegram.org/bot848307854:AAElOophxSdlMf8UXubudIQnXfWv8VuU_bE/sendMessage?parse_mode=markdown&chat_id=249356603'
            send_message = '/sendMessage?parse_mode=html'
            chat = '&chat_id=',CHAT_ID
            text_message = '&text='+send_Tmsg
            print(text_message)
            requests.get(url, f'[.]{text_message}')
            # requests.get(
            #     "https://api.telegram.org/bot{}/sendMessage?parse_mode=html&chat_id={}&text={}".format(TG_TOKEN,
            #                                                                                            CHAT_ID,
            #                                                                                            send_Tmsg))
            data_count_15_prev = len(data_15)
        elif data_count_15_prev > len(data_15):
            for i in data_15:
                Tmsg = "Name: {}, Prise: {}, https://airsofter.world/ru-ru/product/{}".format(i['name'],
                                                                                              i['price'],
                                                                                              i['id'])
                send_Tmsg += (Tmsg + '\n')
                print(send_Tmsg)
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, send_Tmsg))
            data_count_15_prev = len(data_15)
        counter += 1
        print(counter)
        if counter == 4:
            data_60 = sql_query(sql2)
            Tmsg = 'The site has {} new products'.format(
                data_60[0]['COUNT(`id`)']) + ' https://airsofter.world/ru-ru/market/index'
            print(Tmsg)
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))

        if counter == 4:
            counter = 0
