import pymysql.cursors

TG_TOKEN = "848307854:AAElOophxSdlMf8UXubudIQnXfWv8VuU_bE"
# CHAT_ID = "249356603" #-1001192663900
CHAT_ID = "-1001192663900"

def connect():
    con = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'nonroot',
        # user = 'user',
        password = 'dFsd423vcvSsxXX',
        # password = 123,
        db = 'airsoft',
        # db = 'stage_airsoftorg',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con