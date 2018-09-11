# 控制结构
# 顺序结构：程序从上到下依次执行



#分支结构：注意语句块的缩进和条件后面的冒号
#比较运算符：>  <  ==  !=  >=   <=



#输出较大的数
# a=10
# b=20
# if a>b:
#     print(a)
# else:
#     print(b)
#
#
# if a>b and b>20:
#     print(a+b)
# elif a<b or a<0:
#     print(a-b)
# else:
#     print(a*b)


#输入字符串，大写转小写，小写转大写
# r=input("请输入字符串")
# if r.islower():
#     print(r.islower())
#     print(r.swapcase())
# elif r.isupper():
#     print(r.swapcase())
# else:
#     print(r)




# 输入年、月、日  打印出是今年的第几天
# a=int (input("请输入年份："))
# b=int (input("请输入月份："))
# c=int (input("请输入日:"))
#
# list1=[0,31,59,90,120,151,181,212,243,273,304,334]
# list2=[0,31,60,91,121,152,182,213,244,274,305,335]
# if a%4==0:
#     list=list2
# else:
#     list=list1
# sum=list[b-1]+c
#
# print("今天是今年的第",sum,"天")



#循环结构:while ,for
#continue,break只能跳出当前循环，如果有嵌套的话不能跳出外层循环
# sum1=0
# for i in range(1,101):
#     sum1=sum1+i
# print(sum1)
#
# sum2=0
# a=0
# b=101
# while a<b:
#     sum2=sum2+a
#     a=a+1
# print(sum2)



# list1=[1,2,3,4,5]
# sum3=0
# for i in list1:#这里i遍历到List里面的每个数
#     sum3=sum3+i
# print(sum3)

#打印99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        m=j*i
        print('%d*%d=%d\t'%(j,i,m),end='')
    print('')




# import  math
# for i in range(0,1000):
#     a=math.sqrt(i+100)#math.sqrt(value)开完全平方
#     b=math.sqrt(i+268)
#     if a==int(a) and b==int(b):
#       print(i)



# x=int(input("请输入x："))
# y=int(input("请输入y："))
# z=int(input("请输入z："))
# a=[x,y,z]
# for i in range(0,len(a)-1):
#     if a[i]>a[i+1]:
#         temp=a[i]
#         a[i]=a[i+1]
#         a[i+1]=temp
# for i in range(0,len(a)-2):
#     if a[i]>a[i+1]:
#         temp=a[i]
#         a[i]=a[i+1]
#         a[i+1]=temp
#
# print(a)


#水仙花数
# for i in range(1,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             if i*100+j*10+k==i*i*i+j*j*j+k*k*k:
#                 print(i*100+j*10+k)
#
#
# #排序
# list1=[3,65,22,102,4]
# for i in range(0,len(list1)-1):
#     for j in range(0,len(list1)-1-i):
#         if list1[j]>list1[j+1]:
#             temp=list1[j]
#             list1[j]=list1[j+1]
#             list1[j+1]=temp
#
# print(list1)


import random
#random.random()是0到1之间的浮点数
# b=random.randint(0,1000)#randint 是直接给范围
# i=0
# while True:
#     a=int (input("请输入一个数字"))
#     if a>b:
#       i=i+1
#       print("大了,你进行了",i,"次")
#     elif a<b:
#        i=i+1
#        print("小了,你进行了",i,"次")
#     elif a==b:
#        i=i+1
#        print("通关，你一共进行了",i,"次")
#        break

'''
list2=[3,2,5,9,6,4]
list2.sort()
print(list2)#不能写成print(list2.sort())的形式，否则打印不出来
'''

#打印图形：直角三角形
for i in range(0,6):
     print('*'*i)


#打印等腰三角形
a='*'
for i in range(1,10,2):
    print((a*i).center(9,))

#打印倒等腰三角形
# a='*'
# list=[9,7,5,3,1]
# for i in list:
#     print((a*i).center(9,))

#全局函数：内置函数
#模块级别（全局）
#外层函数（局部）
#内层函数（本地）
#函数以表达式return结束，不带表达式的return返回none


def add(x,y):
    return x+y



def sum(n):
    sum1=0
    for i in range(1,n+1):
        sum1=sum1+i
    return  sum1

print(sum(100))

#可以给其中一个变量赋值，x,y的顺序可以交换
def sub(x,y=2):
    return x+y



#查找something中有多少个some
def coot(something,some):
    i=0
    for j in range(0,len(something)):
        if some==something[j]:
            i=i+1
    print(i)
# coot('hdaFKJDSHLKFJ','J',1,2)



'''
def cott(something,some):
    i=0
     if some in something:
        i=i+1

    print(i)
coot('hdaFKJDSHLKFJ','J')
'''



#支持传入任意多个整数进行加法运算
def add_most(*float):
    sum2=0
    for i in float:
        sum2=sum2+i
    print(sum2)
add_most(1,2,3,4.5,5)


#简易计算器
def aaa(x,y):
    z=x+y
    return z

def bbb(x,y):
    z=x-y
    return z


def ccc(x,y):
    z=x*y
    return z


def ddd(x,y):
    z=x/y
    return z


def use():
    x=int(input("请输入x的值"))
    n=input("请输入运算符：")
    y=int(input("请输入y的值"))
    if n=="+":
        print(aaa(x,y))
    elif  n=="-":
       print(bbb(x,y))
    elif  n=="*":
        print(ccc(x,y))
    elif  n=="/":
        print(ddd(x,y))
# use()

#可变对象和不可变对象

#可变对象

def change(val):
    val.append(1)
nums=[0]
change(nums)
print(nums)


def change1(val):
    val.add(1) #集合增加元素使用add
nums={0}
change1(nums)
print(nums)

# help(set)


tup1=([1,2,3],[3,3])
tup1[0].append(4)
print(tup1)

def change2(val):
    x=type(val)
    if x==int:
        val=val+1
        print(val)
    elif x==str:
        val=val+'1'
        print(val)
    elif x==list:
       val.append(1)
       print(val)
# change2([4,5])


#函数的作用域
#全局变量


#局部变量


#在屏幕上循环输入，每输入一次就以字符串的形式添加到列表中

#局部函数
# def aaa():
#     list1=[]
#     while True:
#         x=input("请输入内容：")
#         if x!='quit':
#            list1.append(x)
#         else:
#             break
#     return list1
# print(aaa())


#全局函数
# list1=[]
# def bbb():
#     while 1==1:
#         x=input("请输入内容：")
#         if x!='quit':
#            list1.append(x)
#         else:
#             break
# bbb()
# print(list1)


#函数Lambda
# func=lambda x:x+1
# print(func(5))


#函数：文档字符串
# def fun():
#     '''lijpojfovga'''
#     print('udfhoidsajofj')
#     return
# print(fun.__doc__)



func1=lambda x,y:x**y
print(func1(2,3))


def so(a):
    # a=list(input("请输入一个列表"))
    a.sort()
    return a
print(so([1,5,6,2,9,4]))



def fun():
    '''
    作者：我自己
    功能：实现查找计数
    参数说明：一个包含在另一个中
    返回值：print(coot("abaa",'a'))
    '''
    return
print(fun.__doc__)
fun()

list3=[1,2]
print(id(list3))
list3.append(4)
print(id(list3))


num=[]
for i in range(2,100):
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)