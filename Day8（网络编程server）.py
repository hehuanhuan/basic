import socket
import threading


class server:
    def __init__(self):
        self.s=socket.socket()
        host=socket.gethostname()
        self.s.bind((host,8888))
        self.s.listen(5)      #5指监听个数
        self.conn()
    # def conn(self):
    #     while True:
    #         con,addr=self.s.accept()#con指连接对象，有send和recv两种方法，addr返回的第一个是ip地址
    #         data='你已成功连接'
    #         con.send(data.encode('utf-8'))
    #         print('用户%s,%s已成功连接'%(addr[0],addr[1]))
    #         while True:
    #             #接受客服端发送的信息
    #             a=con.recv(1024)
    #             print(a.decode('utf-8'))
    #             #向客户端发送相同的消息
    #             con.send(a)
    def conn(self):
        # self.list1=[]
        self.all=[]
        self.two=[]
        while True:
            con,addr=self.s.accept()
            threading.Thread(target=self.threads,args=(con,addr)).start()
            # self.list1.append(con)
            self.two=[con,addr]
            self.all.append(self.two)

    def threads(self,con,addr):
        data='服务器已开启，你已成功连接'
        con.send(data.encode('utf-8'))
        print('用户%s,%s已成功连接'%(addr[0],addr[1]))
        try:
             while True:
                recive_message=con.recv(1024).decode('utf-8')
                if recive_message=='quit':
                    pass
                    # print('有客户端'+addr[0]+'退出')
                    # for i in self.all:
                    #     if addr[0]==i[1]:
                    #         self.all.remove(i)
                    #     print(addr[0]+'已移除')
                else:
                    print(recive_message)
                    b='用户'+addr[0]+'发送了：'+recive_message
                    for i in self.all:
                        i[0].send(b.encode('utf-8'))
                    # for i in self.list1:
                    #      i.send(a.encode('utf-8'))
                # return recive_message
        except:
            print('有客户端'+addr[0]+'退出')
            for i in self.all:
                if addr[0]==i[1]:
                    self.all.remove(i)
                print(addr[0]+'已移除')

    def __del__(self):
        self.s.close()
if __name__=='__main__':
    ss=server()
