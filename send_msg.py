import requests
from config import connect
from config import TG_TOKEN, CHAT_ID
import time
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
import json
import datetime


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
    end_url_img = []
    while condition:
        hour_now = datetime.datetime.now().hour
        # hour_now = 20
        if 9 <= hour_now < 20:
            print("Time ok", hour_now,':', datetime.datetime.now().minute)
            time.sleep(900)
            time_now = time.time()
            New_prod_mes = []
            sql1 = "SELECT `id`, `name`, `price`, `updated_at`, `recommended`, `published`, `product_image_one`, `description` FROM products WHERE `updated_at` > {} AND `recommended` = {} and `published` = {}".format(
                time_now - 900, 1, 1)
            sql2 = "SELECT COUNT(`id`) FROM products WHERE `updated_at` > {}".format(time_now - 3600)
            data_15 = sql_query(sql1)

            if data_count_15_prev < len(data_15):
                for i in data_15:
                    photo = 'https://airsofter.world/images/product-image/{} \n'.format(i['product_image_one'])
                    Tmsg = '[⁠]({})'.format(photo)
                    img = [
                        [InlineKeyboardButton('View more',
                                              url='https://airsofter.world/ru-ru/product/{}'.format(i['id']))]]
                    url_img = InlineKeyboardMarkup(img)
                    end_url_img.append(url_img)
                    if len(i['name']) > 36:
                        new_name = i['name'][0:36] + '\n' + i['name'][37:]
                        print('new_name =', new_name)
                        des = 'Name: {}\nPrice: {}'.format(new_name, i['price'])
                        new_name = ''
                    else:
                        des = 'Name: {}\nPrice: {}'.format(i['name'], i['price'])
                    output_mes = Tmsg + des
                    New_prod_mes.append(output_mes)
                print('New_prod_mes==', New_prod_mes)
                for num, prod in enumerate(New_prod_mes):
                    data = {
                        "chat_id": CHAT_ID,
                        "parse_mode": "markdown",
                        "text": prod,
                        "reply_markup": json.dumps(end_url_img[num].to_dict())
                    }
                    print('data =', data)
                    requests.post(url='https://api.telegram.org/bot{}/sendMessage'.format(TG_TOKEN), data=data)
                data_count_15_prev = len(data_15)

            elif data_count_15_prev > len(data_15):
                for i in data_15:
                    photo = 'https://airsofter.world/images/product-image/{} \n'.format(i['product_image_one'])
                    Tmsg = '[⁠]({})'.format(photo)
                    img = [
                        [InlineKeyboardButton('View more',
                                              url='https://airsofter.world/ru-ru/product/{}'.format(i['id']))]]
                    url_img = InlineKeyboardMarkup(img)
                    end_url_img.append(url_img)
                    if len(i['name']) > 36:
                        new_name = i['name'][0:36] + '\n' + i['name'][37:]
                        print('new_name =', new_name)
                        des = 'Name: {}\nPrice: {}'.format(new_name, i['price'])
                        new_name = ''
                    else:
                        des = 'Name: {}\nPrice: {}'.format(i['name'], i['price'])
                    output_mes = Tmsg + des
                    New_prod_mes.append(output_mes)
                print('New_prod_mes==', New_prod_mes)
                for num, prod in enumerate(New_prod_mes):
                    data = {
                        "chat_id": CHAT_ID,
                        "parse_mode": "markdown",
                        "text": prod,
                        "reply_markup": json.dumps(end_url_img[num].to_dict())
                    }
                    print('data =', data)
                    requests.post(url='https://api.telegram.org/bot{}/sendMessage'.format(TG_TOKEN), data=data)
                data_count_15_prev = len(data_15)

            counter += 1
            print(counter)
            if counter == 4:
                data_60 = sql_query(sql2)
                Tmsg = 'Product update\nThe website has {} new products'.format(
                    data_60[0]['COUNT(`id`)']) + ' https://airsofter.world/ru-ru/market/index'
                print('Tmsg =', Tmsg)
                requests.get(
                    "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))

            if counter == 4:
                counter = 0
        else:
            print('Time sleep', hour_now)
            time.sleep(46800)
            sql3 = "SELECT COUNT(`id`) FROM products WHERE `updated_at` > {}".format(time_now - 46800)
            data_46800 = sql_query(sql3)
            Tmsg = 'Product update\nThe website has {} new products'.format(
                    data_46800[0]['COUNT(`id`)']) + ' https://airsofter.world/ru-ru/market/index'
            print('Tmsg =', Tmsg)
            requests.get(
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TG_TOKEN, CHAT_ID, Tmsg))
