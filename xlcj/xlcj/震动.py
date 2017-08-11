import pymysql

con = pymysql.connect(db='test_check',user='check_user',port=3306,host='123.56.72.57',password='654321123456',charset='utf8')
cursor = con.cursor()
sql = "select high,low from stock_kline"
cursor.execute(sql)
data = cursor.fetchall()
for d in data:
    a = (d[0]-d[1])/d[1]*100
    if  a>10:
        print(a)