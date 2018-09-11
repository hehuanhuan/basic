class student():
    x=100
    # def __init__(self,name,age,list1,list2):
    def __init__(self,name,age,tup):
        self.name=name
        self.age=age
        # self.list1=list1
        # self.list2=list2
        self.tup=tup

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_course(self):
        # x=max(self.list2)
        # y=self.list2.index(x)
        # print(self.list1[y])
        # print(x)
          list1=self.tup.items()
          list2=list(list1)
          x=max(list2[0][1],list2[1][1],list2[2][1])
          print(x)
          if list2[0][1]==x:
              print(list2[0])
          if list2[1][1]==x:
              print(list2[1])
          if list2[2][1]==x:
              print(list2[2])

    # def get_avg(self):
    #     y=(self.list2[0]+self.list2[1]+self.list2[2])/3
    #     print(y)


a=student('张三',10,{'语文':88,'数学':99,'英语':99})
a.get_name()
a.get_age()
a.get_course()
# a.get_avg()
