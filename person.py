class person:
    mon=1
    def make_money(self):
        print('i need more money')
    def add(self):
        for i in (0,5):
            self.mon=self.mon+i
        print(self.mon)
a=person()
print(a.mon)
a.add()
class woman(person):
    pass
b=woman()
print(b.mon)