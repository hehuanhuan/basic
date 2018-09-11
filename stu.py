from basic.person import person
class stu(person):
    name='张三'
    def make_money(self):
        print('so much money')

    def test(self,a,b,c):
        print(a+b+c)
    def test(self,x,y):
        print(x+y)


if __name__=='__main__':
     stu().test(1,2)