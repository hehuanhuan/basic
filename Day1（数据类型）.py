# 当没有输入类型时，输出时默认为字符型
# i=input('请输入一个列表')
# print(type(i))
# j=input({1,2,3})      #input是提示输入内容，赋的是input输入的值
# print(type(j))
# a=8000
# b=8000
# print(id(a))
# print(id(b))
# print(a is b)


print('123\n456')
print('123\r456')
print('我是：'+'123')
print('我是：','123')

print('我是：',end='')
print('中国人')

# print默认为自动换行，单行输出:print(+，end='')
# while 1:
#     print(1,end="")
# 想要用两个print输出999123
print(999,end='')
print("123")




# i=int(input("请输入i的值"))
# j=int(input("请输入j的值"))
# print(i+j)
# print(i-j)
# print(i*j)
# print(i/j)

# i=float(input("请输入浮点数i的值"))
# j=float(input("请输入浮点数j的值"))
# print(i+j)
# print(i-j)
# print(i*j)
# print(i/j)
# 输入abc时报错，输入小数和整数时均正常

# x=10
# print(x) #输出10，变量不能加引号
# print("x") #输出x
# print(z)  #报错，显示z没有定义

# print("please input number:")
# x=int(input())
# print(x)


# x=int(input("please input number:"))
# print(x)

#分别在键盘上输出三角形和正方形
# print(''''
#
# ''''''')

# 变量：变量只能以字母或下划线的方式才能识别，标识符，，，，，不要用关键字命名变量名
# 关键字：False,None,Ture,and,as,assert,except,finally,from,global,lambda,pass,raise,yield
# python里面只要内存地址相同就会绝对相同，变量名不重要
# a="a"
# b="a"
# print(id(a),id(b))
# 显示地址相同

# 占位符%
# %d代表整数，%f浮点，%s字符串，%e科学计数，%c读入一个字符，%x读入十六进制整数，%X读入时间格式，%%读%符号
a=123
b=123
c=123
# print("a="+a,"b="+b)  报错
# 同时打印a/b/c的值
print('a=%d,b=%d,c=%d'%(a,b,c))

# 1、查看所有关键字
# import keyword
# print(keyword.kwlist)
#
# a=100
# b=100
# # as=100,关键字不能使用
# As=100
# print('a=%d,b=%d,As=%d'%(a,b,As))


# 多行注释使用三个'，即'''
'''x=10
x=20
x=30
print(x) #x的值打印为30'''

# 引入数学运算符
# import math
# print(dir(math))#查看所有函数名列表
# x=30
# y=4
# print(math.pow(x,y))#x的y次方计算，用pow()函数
#
#
# print(2**3)  #计算2的3次方，用两个*号
# print(8**(1/3))#开三次方计算，括号里后面的数字是多少就是开的几次方
# print(64**(1/2))
# print(2**4)#16
# print(2**2)#4
# a=257
# b=257
# print(id(a),id(b))
# a=123
# b=124
# print(id(a),id(b))
#
#
# list=[1,2,3,4]
# print(list[1:4])
# print(list[6:])
# list[2]=2017
# print(list)
# del list[2]
# print(list)
#
# list1=(1,2,3,4)
# print(list1[0])#显示下标为多少时也必须使用[]才能，不能用（）

# r=float(input("请输入一个半径:"))
# print("周长是：",2*r)






# 数据类型
# 数字类型：int,float,complex
print(complex(2,(-4)))
# 数据类型转换，
print(int(12.3))  #12
print(float(12))  #12.0
print(int('12.3'))


# a='12.3'
# b=float(a)
# a=int(b)
# print(a)



import math
#计算周长
def d(r):
    d=2*r*math.pi
    return d
#计算面积
def s(r):
    s=r*r*math.pi
    return s
print(d(3))
print(s(3))

def mul(a,b):
    c=(a+b)*(a-b)
    return c
print(mul(1,3))


def s(a,b):
    c=(a**b)//b
    return c
print(s(4,3))

#字符串类型，输入时必须用引号，可以用+号连接
var='hello'
var1='world'
var4=var+var1
print(var4)
print(var+var1)
print(var+','+var1)
print('%s%s'%(var,var1))


# 凡是有索引的都可以切片，字符串也可以，下标开头为0
#倒序输出
print(var[::-1])
# 从下标为3的开始，倒序输出
print(var[2:3:-1])
len("123456")
a="a01234563002554"
print(a.count("0"))
# print(a.count("0",beg=0,end=len(a)))
#把首字母转换为大写
print(a.capitalize())


#返回指定宽度,1为填充
# print(a.center(20,"1"))

#find  如果有就显示查询值所在下标，如果没有就返回-1
print(a.find("a"))


# 替换
print(a.replace("9","0"))

# isdigit(),如果字符串只包含数字就返回Ture,否则返回False
print(a.isdigit())

#islower()区分大小写的字符全都是小写，返回ture,否则返回False
print(a.islower())

#isspace(),如果全为空格返回ture,否则返回False
b="   "
print(a.isspace())
print(b.isspace())


#istitle()字符串是标题化的返回Ture,否则返回False
print(a.istitle())



#lower 转换所有大写为小写
#max（返回字符串中最大的字母）
#min(返回最小的字母)


str="days12343567"
# 1.调换
print(str[::-1])
#2。输出长度
print(len(str))
#出现的次数
print(str.count('3'))
#截取字符串,分割
print(str.split("s",3))


ss='abcdabkrajb'
#3.分别求ab出现的次数和e出现的次数
print(ss.count('ab'))
print(ss.count('e'))
list=ss.split("ab")
i=len(list)-1


a='abc kdn lad'
#4.分别打印以d分割的第二部分和第三部分
list=a.split('d')
print(list[1],list[2])

ss='abcdabkrajb'
# 5,截取第三到第五个字符,判断是否包含数字,并将截取的字符串与hello连接
print(ss[2:5])

print(ss[2:5].isdigit())

print(ss[2:5],"hello")



#列表清空  list.clear()

list=[1,2,3,4,5]
#在末尾追加值
list.append(5)
print(list)
#统计出现的次数
print(list.count(5))
#追加另外一个列表，相当于两个列表相加
list2=[2,3,4]
list.extend(list2)
print(list)
#
print(list.index(2))

#insert 插入insert（index,插入的值）

#list.reverse()反转
#list.pop()移除最后一个
#list.remove（index）移除指定的那个

list=[1,2,3,"duayiuf",4,"udsahyif"]
print(list[2:5])
print(list[-3])

list[2]="third"
print(list)
list2=[2,3,4]
list.extend(list2)
print(list[-2])


list=[['xiaoming','student',10],['xiaohong','coder',23],['xiaohuang','boss',35]]
print(list[2])
del list[1]
print(list)
list.append(10)
print(list)
print(list.count(10))
list.reverse()
print(list)
del list[1][2]
print(list)
list.remove(10)
print(list)

#元祖不能改变，但是元祖里面有列表时可以改变
tup=(1,2,[1,9],10)
tup[2][0]=0
print(tup)
print(id(tup[2][0]))
tup[2][0]=8
print(id(tup[2][0]))
#单个元祖时会将（）默认为优先级
# a=(5)#此时a为int型的
# b=(5,)#后面加,程序即可认为是元祖
# print(type(a))
# print(type(b))


tup1=(1,2,3)
tup2=(4,5,6)
print(tup1[0])
print(len(tup1))
print(tup1[1:2])
tup=tup1+tup2
# list=['dsaoif','yusaiud']
# print(tup1.max())
# set={1,2,3,4}
# print(set.max())
# help(list)
s=set({1,2,3})
#用于强制转换
print(type(set))

del list
list1=[1,2,3,3,4,5,4,4]
s=set(list1)
print(s)
list2=list(s)
print(list2)
#集合：相同的不会同时出现，有去重的功能

t={1,2,3,4}
s={3,4,56,5}
a=t|s
b=t&s
c=t-s#项在t中，但不在s中
d=t^s#项在t或s中，但不会同时出现在二者之中
print(a)
print(b)
print(c)
print(d)

t={1,2,3,4}
s=set({3,4,56,5})
s1={32,5,"c","32",'11'}
s2=set({32,'46',32,'aa'})
s3=set('4,32,46,11,32')
print(s1)
print(s2)
print(s3)

dict1={1:1,2:2,3:3,4:4}
sql=1,2,3,4
val=1
dict2={}
print(dict2.fromkeys(sql,val))

list3=[{'name':'zhangsna','age':20},{'name':'lisi','age':22}]
list3[1]['age']=23
print(list3[1])
# list3.append({'name':'wang','age':30})
# print(list3)
a="hfaijigpfdgpojsofd"
print(a[2:3])

print(dict1[1])