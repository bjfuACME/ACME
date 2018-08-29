import pymssql
# 创建连接
server="42.159.5.42"
user="dengjianqiong"
password="dengjianqiong"
database="User"
conn=pymssql.connect(server,user,password,database)
cur = conn.cursor()
if not cur:
    print("连接失败")
else:
    print("连接成功")

# 查询
def search():
    sql = "select * from Users"
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

# 添加
def insert(a,b):
    cur.execute("INSERT INTO Users VALUES (a,b)")
    conn.commit()
    # sql="INSERT INTO Users VALUES(%s, %d)",
    # [('fanxuanwei','123')]
    # cur.execute(sql)
    # conn.commit()
#     cur.executemany(
#     "INSERT INTO Users VALUES (%d, %s)",
#     [('John Smith', '123'),
#      ('Jane Doe', '456'),
#      ('Mike T.', '789')])
# # 你必须调用 commit() 来保持你数据的提交如果你没有将自动提交设置为true
#     conn.commit()

search()
# insert('fanxuanwei', '123456')
# search()
m=0
n=1
insert(0,1)
search()
cur.close()
conn.close()