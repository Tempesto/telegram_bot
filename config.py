import pymysql.cursors

TG_TOKEN = "848307854:AAElOophxSdlMf8UXubudIQnXfWv8VuU_bE"
CHAT_ID = "-1001192663900" #-1001192663900 249356603

def connect():
    con = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'nonroot',
        password = 'dFsd423vcvSsxXX',
        db = 'stage_airsoftorg',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con