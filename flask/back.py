from flask import Flask, request
import pymysql
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  # 允许的跨域来源

def load_data_frame_from_mysql(sql):
    # sql = 'SELECT * FROM customer_info_100'
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='114514', port=3306, db='covid-19')
    data = pd.read_sql(sql, conn)
    print('数据库读取data')
    conn.close()
    return data


@app.route("/", methods=['GET', 'POST'])
def home():
    data = request.json
    sql = data['sql']
    print(sql)
    info = load_data_frame_from_mysql(sql)
    return info.to_dict(orient='records')

if __name__ == '__main__':
    app.run(debug=True)