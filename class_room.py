import basic.stu as p
from basic.teacher import teacher
class class_room(p.stu,teacher):
    name = 'lsi'
    def make_money(self):
        print('哈哈哈哈哈')
if __name__=='_main_':
    class_room().make_money()
    print(class_room().name)
    print(class_room().name)