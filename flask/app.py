from flask import Flask,request
import pymysql
import pandas as pd

app = Flask(__name__)

def load_data_frame_from_mysql(sql):
    # sql='SELECT * FROM customer_info_100'
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='123456', port=3306, db='customerinfo')
    # sql = "SELECT * FROM customer_info_100"
    data = pd.read_sql(sql, conn)
    print('数据库读取data')
    conn.close()
    return data


@app.route("/",methods=['GET','POST'])
def home():
    sql=request.args.get('sql')
    print(sql)
    info=load_data_frame_from_mysql(sql)
    return info.to_dict(orient='records')