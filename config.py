import pymysql.cursors

TG_TOKEN = "848307854:AAElOophxSdlMf8UXubudIQnXfWv8VuU_bE"
# CHAT_ID = "249356603" #-1001192663900
CHAT_ID = "-1001192663900"

def connect():
    con = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'nonroot',
<<<<<<< HEAD
<<<<<<< HEAD
        password = 'dFsd423vcvSsxXX',
        db = 'airsoft',
=======
=======
>>>>>>> 68654e2... Настройки для glob
        # user = 'user',
        password = 'dFsd423vcvSsxXX',
        # password = 123,
        db = 'airsoft',
        # db = 'stage_airsoftorg',
<<<<<<< HEAD
>>>>>>> 68654e2... Настройки для glob
=======
>>>>>>> 68654e2... Настройки для glob
        cursorclass=pymysql.cursors.DictCursor
    )
    return con