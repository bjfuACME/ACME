import pymssql

class sql():
    def __init__(self):
        self.host ='42.159.5.42'
        self.port = 1433
        self.db = 'User'
        self.user ='dengjianqiong'
        self.pwd ='dengjianqiong'
        self.charset='utf8'
    #获取连接对象
    def connection(self):
        self.conn = pymssql.connect(host=self.host,
        port = self.port,db=self.db,
        user = self.user,passwd = self.pwd,charset=self.charset)
        self.csl = self.conn.cursor()
        if not self.csl:
            print("连接失败")
        else:
            print("连接成功")

    #关闭资源
    def free(self):
        try:
             self.csl.close()
             self.conn.close()
        except Exception as e:
            print(e)
    #增加，删除，更新
    def executeUpdate(self,sql,params=[]):
        rows = 0
        try:
            self.connection()
            rows = self.csl.execute(sql,params)
            print("影响的行数：",rows)
            self.conn.commit()
            self.free()
        except Exception as e:
            print(e)
        return  rows
    #查询
    def executeQuery(self,sql,params=[]):
        result =()
        try:
            self.connection()
            self.csl.execute(sql,params)
            result = self.csl.fetchall()
            self.conn.commit()
            self.free()
        except Exception as e:
            print(e)
        return result

    connection()
