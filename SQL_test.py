# coding:utf-8
# http://www.runoob.com/python/python-mysql.html
import MySQLdb


class MySQLTest:
    def __init__(self):
        self.db = MySQLdb.Connection('localhost', 'root', '123456.qaz', 'TESTDB')
        self.cursor = self.db.cursor()
        self.fname = ""
        self.lname = ""
        self.age = 0
        self.sex = ""
        self.income = 0

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

        sql = 'CREATE TABLE EMPLOYEE (\
         FIRST_NAME  CHAR(20) NOT NULL,\
         LAST_NAME  CHAR(20),\
         AGE INT,  \
         SEX CHAR(1),\
         INCOME FLOAT )'

        self.cursor.execute(sql)

    def insert_info(self, fname, lname, age, sex, income):
        sql_1 = "INSERT INTO EMPLOYEE(FIRST_NAME,\
                 LAST_NAME, AGE, SEX, INCOME)\
                 VALUES ('%s', '%s', '%d', '%c', '%d' )" % (fname, lname, age, sex, income)
        try:
            # 执行sql语句
            self.cursor.execute(sql_1)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            # Rollback in case there is any error
            print e
            self.db.rollback()

    def show_data(self):
        sql = "select * from employee where income > '%d'" % 1000
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for each in results:
                fname = each[0]
                lname = each[1]
                age = each[2]
                sex = each[3]
                income = each[4]
                print "fname:%s lname:%s age:%d sex:%s income:%d" % (fname, lname, age, sex, income)
        except Exception as e:
            print e
            print "Error : unable to fetch data"

    def close_db(self):
        self.db.close()


tt = MySQLTest()
tt.create_table()
tt.insert_info('zas', 'Zheng', 18, 'M', 100000)
tt.show_data()
tt.close_db()
