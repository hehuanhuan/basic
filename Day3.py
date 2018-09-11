#面向对象：就是把面向过程的东西全部封装，不需要知道里面的具体能容，只需要有需求后调用，得到返回值
#类：定义类：class 类名：（后面属性和方法分割不需要加分号）
'''对象：对象是实体，凡是能看到的东西都是对象，所以万物皆对象，包含两方面的内容：属性和方法，属性是对这个对象静态的描述，标签。
方法是动态的描述
'''
#面向过程：
#创建类
class day3:
    #创建全局变量（Java中的成员变量），后面必须加上self才能使用，如创建成员变量z,后面要加上self.z才能使用
    z=100

    #创建私有属性，前面加两根下划线，定义了私有变量后只能在类下面的函数中调用
    __s=300

    # 创建动态的方法
    def add(self):
        a=1
        b=2
        print(a+b+self.z)

    #创建静态方法，对象不能调用静态方法，静态方法和动态方法区别在于方法里面的（）内没有self
#     @staticmethod  #静态方法如果要调用，需加@staticmethod，否则会报错
#     def add():
#         a=1
#         b=2
#         print(a+b)


    # 修改构造方法，python的构造方法是__init__
    def __init__(self,name,age):
        self.__name=name
        self.age=age#这时age就变成了一个全局变量
        print(self.__name,self.age)


    def _print_info(self,a):
        self.x=a
        print("INFO:..%s..%s..%s..\n"%(self.__name,self.age,self.__s))

# 调用方法
# 1.day3().add()
#  2.m=day3()
#     m.add()


a=day3('wang',10)
a._print_info(1)
print(a.age)
print(a.z)
print(a.x)

numbers=['10','11','12']
numbers = [ int(x) for x in numbers ]
print(numbers)


#1.计算兔子问题，N个月后有多少只兔子
# s1=1
# s2=1
# i=1#定义一个控制变量
# m=int(input('请输入月份：'))
# while True:
#     if(i==1 or i==2):
#         print('%d个月的兔子总数是%d对'%(i,s1))
#         i+=1
#     elif i<m:
#         s1=s1+s2
#         s2=s1+s2
#         print('%d个月的兔子总数是%d对'%(i,s1))
#         i+=1
#         print('%d个月的兔子总数是%d对'%(i,s2))
#         i+=1
#     else:
#         break
class tu():
    mouth=1
    def mouth_add(self):
        self.mouth+=1
    def sum(self,a):
        a.append(tu())
class count():
    list1=[tu()]
    def count_add(self):
        x=int(input('请输入月份：'))
        for i in range(1,x+1):
            for j in self.list1:
                if j.mouth<3:
                    j.mouth_add()
                else:
                    j.sum(self.list1)
            print(i,'月',len(self.list1),'对')

# count().count_add()




#2.猜拳游戏

class AutoPeople():
    import random
    GameDic=['石头','剪刀','布']
    x=random.choice(GameDic)
    y=random.choice(GameDic)

class man(AutoPeople):
    a=AutoPeople().x

class woman(AutoPeople):
    b=AutoPeople().y

class Score(man,woman):
    def score(self):
        self.manscore=0
        self.womanscore=0
        for i in range(1,4):
            if man().a=='石头' and woman().b=='石头':
                self.manscore=self.manscore
                self.womanscore=self.womanscore
            elif man().a=='石头' and woman().b=='剪刀':
                self.manscore=self.manscore+1
                self.womanscore=self.womanscore-1
            elif man().a=='石头' and woman().b=='布':
                self.manscore=self.manscore-1
                self.womanscore=self.womanscore+1
            elif man().a=='剪刀' and woman().b=='石头':
                self.manscore=self.manscore-1
                self.womanscore=self.womanscore+1
            elif man().a=='剪刀' and woman().b=='剪刀':
                self.manscore=self.manscore
                self.womanscore=self.womanscore
            elif man().a=='剪刀' and woman().b=='布':
                self.manscore=self.manscore+1
                self.womanscore=self.womanscore-1
            elif man().a=='布' and woman().b=='石头':
                self.manscore=self.manscore+1
                self.womanscore=self.womanscore-1
            elif man().a=='布' and woman().b=='剪刀':
                self.manscore=self.manscore-1
                self.womanscore=self.womanscore+1
            elif man().a=='布' and woman().b=='布':
                 self.manscore=self.manscore
                 self.womanscore=self.womanscore

        if self.manscore>self.womanscore:
            print('机器人man得分%d,机器人woman得分%d,机器人man获胜'%(self.manscore,self.womanscore))
        elif self.manscore==self.womanscore:
            print('机器人man得分%d,机器人woman得分%d,平局'%(self.manscore,self.womanscore))
        else:
            print('机器人man得分%d,机器人woman得分%d,机器人woman获胜'%(self.manscore,self.womanscore))
Score().score()


#3.计算20次后球运行的距离
sum1=30
sum=30
list1=[]
for i in range(2,21):
    sum1=sum1/2
    list1.append(sum1)
for j in range(0,len(list1)):
    sum=sum+list1[j]
print(sum)



