'''
#异常:
try:
    def div(a,b):

        return a/b
    print(div(x,0))
# except NameError:
#     print('.....')
except Exception:
    print('goio')


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
    while True:
        try:
            x=int(input("请输入x的值"))
            n=input("请输入运算符：")
            y=int(input("请输入y的值"))
            if n=="+":
                if x==a:
                    raise ValueError
                else:
                    print(aaa(x,y))
            elif  n=="-":
               print(bbb(x,y))
            elif  n=="*":
                print(ccc(x,y))
            elif  n=="/":
                if y==0:
                    raise ZeroDivisionError
                else:
                    print(ddd(x,y))
            else:
                raise NameError
        except ValueError:
            print('输入字符错误')
            continue
        except NameError:
           print('输入运算符错误')
           continue
        except ZeroDivisionError:
           print('分母不能为0')
           continue

# use()

a=1
b=0
def do():
    try:
        c=a/b
    except Exception as e:
        # print(e)
        return e
    finally:#不会因为之前程序执行完了return后就不再执行，finally下的语句块都会执行
        print('go on')
do()

def error():
    try:
        dict={1:'a',2:'b',3:'c',4:'d'}
        #根据输入的键名，得到键值
        i=int(input('请输入键名：'))
        print(dict[i])
    except ValueError:
        print('键名不能为空')
    except KeyError:
        dict[i]='abc'
        print(dict)
    else:
        print('没有异常')

# error()
'''
# x=open('C:\\Users\\Administrator\\Desktop\\aaa.txt','r+')
# x.write('just so so')
# y=x.read()
# print(y)
# x.close()
# y=open('C:\\Users\\Administrator\\Desktop\\aaa.txt','r')
# # y.seek(0)
# z=y.read()
# print(z)
# y.close()

#打开文件d://a.txt，并写入字符
# a=open('d:\\a.txt','r+')
# a.write('test aaa')
# a.close()
# #以读的方式打开，并读取
# b=open('d:\\a.txt','r')
# c=b.read()
# print(c)
# x=open('d:\\a.txt','a')
# x.writelines(['\ndsaiugoifufa\n','uaoiufoiiso\n','udsahfois\n','123\n','saf\n'])
# x.close()
# y=open('d:\\a.txt','r')
# z=y.readlines()
# for i in range(0,len(z)):
#     print('第%d行：'%(i+1),z[i])
# y.close()
# a=open('d:\\a.txt','r+')
# b=a.readlines()
# for i in b:#通过遍历，输出文件的每行
#    print(i)


'''
#对xampp中的apache日志文件（以。log结尾的文件）进行读取，筛选其中的错误信息，并全部输出到另一个文件中
import os
list_file=os.listdir('c:\\xampp\\apache\\logs')
# print(list_file)
f_file=[]
for i in list_file:
    if '.log' in i:
        f_file.append(i)
print(f_file)
#打开全部后缀名为.log的文件
list1=[]
for j in f_file:
    x='c:\\xampp\\apache\\logs\\'+j
    list1.append(x)
list3=[]
for k in list1:
    f=open(k,'r+')
    y=f.readlines()
    for w in y:
        if 'error' in w:
            list3.append(w)
print(list3)
r=open('d:\\new.log','w')
r.writelines(list3)
r.close()
e=open('d:\\new.log','r')
h=e.read()
print(h)
'''





def read_file(name,begin_line,end_line):
    f=open(name,'r')
    list1=f.readlines()
    z=list1[begin_line-1:end_line]
    for i in z:
        print(i,end='')

    #写入
    # list5=[]#对行写东西
    # f=open(name,'a')
    # while True:
    #     x=input('请输入每行内容')
    #     list5.append(x)
    #     if len(list5)<=end_line-begin_line:
    #          f.writelines(list5)
    #     else:
    #          print('行数超出要求')
    #          f.close()
    #          break
# read_file('C:\\Users\\Administrator\\Desktop\\aaa.txt',2,4)


#3.写一个程序，实现打开后有三种方式：读、写
def choicemethod(load,name):
    if name=='write':
        f=open(load,'w')
        x=input('请输入内容：')
        y=x+'\n'
        f.write(y)
        f.close()
    elif name=='read':
        f=open(load,'r')
        z=f.read()
        print(z)
        f.close()
    elif name=='quit':
        f=open(load,'r')
        f.close()
# choicemethod('C:\\Users\\Administrator\\Desktop\\aaa.txt','read')


'''
f=open('C:\\Users\\Administrator\\Desktop\\日常总结.doc','rb')
n=f.read()
print(n)
x=open('C:\\Users\\Administrator\\Desktop\\日常总结-副本.txt','wb')
y=x.write(n)
f.close()
x.close()
'''
