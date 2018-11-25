import socket
import threading


def thread_handler(c, addr):        #, current_thread, threads
    global current_thread
    global thread_number
    global sockets
    global socket_index
    msg = "Welcome to Chat Server:\n"
    byte = msg.encode()
    c.send(byte)

    try:
        while (True):
            print(len(threads))
            byte = c.recv(1024)
            client_message = byte.decode()
            for i in sockets:
                #print(i)
                if(i != c):
                    print(i != c)
                    i.send(byte)
    except ConnectionResetError:
        c.close()



s= socket.socket()
port = 12345
s.bind(('',port))
s.listen(5)
threads = []
thread_number = -1
sockets = []
socket_index = -1
lock = threading.Lock()

while True:
    c, addr = s.accept()
    sockets.append(c)
    socket_index += 1
    thread_number += 1
    print("Got Connected", addr)
    t = threading.Thread(target=thread_handler, args=(c, addr))     #, thread_number, sockets
    # t.start()
    threads.append(t)
    threads[thread_number].start()
