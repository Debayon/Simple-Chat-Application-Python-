import socket
import threading


def thread_handler():
    while (True):
        byte = s.recv(1024)
        msg = byte.decode()
        print(msg)


s = socket.socket()
#host = socket.gethostbyname()
port = 12345
s.connect(('127.0.0.1',port))
print(s.getsockname()[0])

t = threading.Thread(target=thread_handler,args=())
t.start()

while(True):
    expression = input()
    byte = expression.encode()
    s.send(byte)

s.close()