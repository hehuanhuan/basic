import pymysql
'''
#使用connect()方法获得一个连接对象db，方法里面需要填写参数ip地址，root,密码，数据库
db=pymysql.connect('localhost','root(数据库用户名)','密码','test（还没建数据库就不写）')
cursor=db.cursor()
cursor.execute('SELECT * FROM product')
db.commit()#提交事务
db.close()#关闭连接
'''



# #创建数据库woniudb
# db=pymysql.connect('localhost','root','',charset='utf8')
# cursor=db.cursor()
# # sql='create database woniudb'
# cursor.execute('create database woniudb')
# db.commit()
# db.close()
# #创建表student
# db=pymysql.connect('localhost','root','','woniudb',charset='utf8')
# cursor=db.cursor()
# cursor.execute('''create table student6(
# id int,
# name varchar(20),
# sex varchar(2),
# age int,
# class varchar(20)
# )ENGINE=InnoDB DEFAULT CHARSET='UTF8';
# insert into student6(id,name,sex,age,class)
# values(4,'张三','男',17,'高三3班'),(5,'李四','女',16,'高三1班'),
# (6,'王五','男',18,'高三2班');
# ''')
# db.commit()
# db.close()

#删除一行
# db=pymysql.connect('localhost','root','','woniudb',charset='utf8')
# cursor=db.cursor()
# cursor.execute('''
# delete from student4 where name='大师兄';
# ''')
# db.commit()
# db.close()


#将查询到的内容打印出来
# db=pymysql.connect('localhost','root','','woniudb',charset='utf8')
# cursor=db.cursor()
# cursor.execute('''select * from student4  group by class
# ''')
# db.commit()
# results=cursor.fetchall()
# print(results)
# db.close()

a='ksagfidsjgoi'
b=a.endswith('o')
print(b)
list1=[1,2,3,4,9,5,'3']
a=max(list1)
print(len(list1))
