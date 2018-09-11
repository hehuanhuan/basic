import socket
import threading
import time
class client():
    def __init__(self):
        self.c=socket.socket()
        host=socket.gethostname()
        self.c.connect((host,8888))
        # self.threads()
        self.conn()
    def conn(self):
        data=self.c.recv(1024)
        print(data.decode('utf-8'))
        threading.Thread(target=self.send).start()
        threading.Thread(target=self.recive).start()

    def send(self):
        #向服务器发送消息
        try:
            while True:
                x=input()
                send_message.append(x)
                if x=='quit':
                    self.c.send(x.encode('utf-8'))
                    self.c.close()
                else:
                    self.c.send(x.encode('utf-8'))#向服务器发送内容
                    time.sleep(0.5)

        except:
            print('你已成功退出')

    def recive(self):
        #接收服务器发送的消息
        while True:
             a=self.c.recv(1024).decode('utf-8')
             print(a)

    def __del__(self):
        self.c.close()
client()