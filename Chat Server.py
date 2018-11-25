import socket
import threading


def thread_handler(c, addr):        #, current_thread, threads

    #global current_thread
    #global thread_number
    global sockets
    global socket_index
    msg = "Welcome to Chat Server:"
    byte = msg.encode()
    c.send(byte)
    try:
        while (True):
            #print("Number of Threads:",len(threads))
            #print("Number of Sockets:",len(sockets))
            byte = c.recv(1024)
            client_message = byte.decode()
            i = 0
            #for i in range(0, len(sockets)):
            for i in sockets:
                #print(i)
                if(i != c):
                    #print(i != c)
                    try:
                        i.send(byte)
                    except OSError:
                        lock.acquire()
                        sockets.pop(sockets.index(i))
                        socket_index -= 1
                        lock.release()
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

    print("Got Connected", addr)
    print(len(threads))
    flag = 0
    for i_threads in threads:
        if(not(i_threads.isAlive())):
            i_threads = threading.Thread(target=thread_handler, args=(c, addr))
            i_threads.start()
            flag = 1
            break
    if(flag == 0):
        t = threading.Thread(target=thread_handler, args=(c, addr))     #, thread_number, sockets
        #print("flag before")
        #print(thread_number)
        thread_number += 1
        #print("after")
        #print(thread_number)
        #print("\n")
        threads.append(t)
        threads[thread_number].start()
    # t.start()
    print(len(threads))
    print("check\n")