# -*- coding: utf-8 -*-
from pymysql import cursors, connect
#连接数据库
conn = connect(host='127.0.0.1',
               user='root',
               password='123456',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursors:
        #创建嘉宾数据
        sql = 'INSERT INTO sign_guess (realbame, phone, email, sign, event_id, create_time) VALUES ("tt",18612341235,"tt@mail.com",0,1,NOW());'
        cursor.execute(sql)
    #提交事务
    conn.commit()

    with conn.cursor() as cursors:
        #查询添加的嘉宾
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone = %s"
        cursor.execute(sql,('18612341235',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()