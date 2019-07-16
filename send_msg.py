import requests
from config import connect
from config import TG_TOKEN, CHAT_ID
import time
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
import json


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
        New_prod_mes = []
        sql1 = "SELECT `id`, `name`, `price`, `updated_at`, `recommended`, `published`, `product_image_one`, `description` FROM products WHERE `updated_at` > {} AND `recommended` = {} and `published` = {}".format(
            time_now - 10, 1, 1)
        sql2 = "SELECT COUNT(`id`) FROM products WHERE `updated_at` > {}".format(time_now - 40)
        data_15 = sql_query(sql1)

        if data_count_15_prev < len(data_15):
            for i in data_15:
                # print(i['product_image_one'])
                photo = 'https://airsofter.world/images/product-image/{} \n'.format(i['product_image_one'])
                Tmsg = f'[⁠]({photo})\n'
                img =[[InlineKeyboardButton('Товар', url='https://airsofter.world/ru-ru/product/{}'.format(i['id']))]]
                # print('img ===',img)
                url_img= InlineKeyboardMarkup(img)
                des='Name: {}\nPrise: {}\nhttps://airsofter.world/ru-ru/product/{}'.format(i['name'], i['price'], i['id'])
                print('url_img =', url_img)
                # fff = {'inline_keyboard': [[{'text': 'Товар', 'url': 'https://airsofter.world/ru-ru/product/{}'.format(i['product_image_one'])}]]}

                output_mes = Tmsg +des
                print('output_mes =', output_mes)
                New_prod_mes.append(output_mes)
            print('New_prod_mes==',New_prod_mes)
            # urll = 'https://api.telegram.org/bot{}/sendMessage?&reply_markup={}&parse_mode=markdown&chat_id={}&text='.format(TG_TOKEN,fff, CHAT_ID)
            # print('url = ', url)
            for ii in New_prod_mes:
                print('ii = ',url_img)
                data = {
                    "chat_id": CHAT_ID,
                    "parse_mode": "markdown",
                    "text": ii,
                    "reply_markup": json.dumps(url_img.to_dict())
                }
                print('data =',data)
                requests.post(url='https://api.telegram.org/bot{}/sendMessage'.format(TG_TOKEN), data=data)



            data_count_15_prev = len(data_15)

        elif data_count_15_prev > len(data_15):
            for i in data_15:
                print(i['product_image_one'])
                photo = 'https://airsofter.world/images/product-image/{} \n'.format(i['product_image_one'])
                Tmsg = f'[⁠]({photo})\n'

                des='Name: {}\nPrise: {}\nhttps://airsofter.world/ru-ru/product/{}'.format(i['name'], i['price'],i['id'])
                output_mes = Tmsg +des
                New_prod_mes.append(output_mes)
            url = 'https://api.telegram.org/bot{}/sendMessage?parse_mode=markdown&chat_id={}&text='.format(TG_TOKEN, CHAT_ID)
            print('!!!!!!!!!!!!',send_Tmsg)
            for ii in New_prod_mes:
                print('ii = ',url_img)
                data = {
                    "chat_id": CHAT_ID,
                    "parse_mode": "markdown",
                    "text": ii,
                    "reply_markup": json.dumps(url_img.to_dict())
                }
                print('data =',data)
                requests.post(url='https://api.telegram.org/bot{}/sendMessage'.format(TG_TOKEN), data=data)
            data_count_15_prev = len(data_15)

        counter += 1
        print(counter)
        if counter == 4:
            data_60 = sql_query(sql2)
            Tmsg = 'The site has {} new products'.format(
                data_60[0]['COUNT(`id`)']) + ' https://airsofter.world/ru-ru/market/index'
            print('Tmsg =',Tmsg)
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))

        if counter == 4:
            counter = 0
