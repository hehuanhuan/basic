from basic.Day3 import day3
class data_reverse:

    def string(self):
        x=input('请输入一串字符：')
        y=x[::-1]
        print(y)

    def list1(self):
        x=list(input('请输入一个列表：'))
        y=x[::-1]
        print(y)
    def number(self):
        x=list(input('请输入一串数字：'))
        y=x[::-1]
        z=''
        for i in y:
            z=z+i
        r=int(z)
        print(r)
        # a=x%10
        # b=(int(x/10))%10
        # c=int((x/100))
        # print('%d%d%d'%(a,b,c))




if __name__=='__main__':

    # data_reverse().list1()
    data_reverse().number()