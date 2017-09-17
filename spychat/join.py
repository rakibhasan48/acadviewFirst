
import sys
import time


msg = ""

def startClient(IP_address, Port) :
    import socket

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.connect((IP_address, Port))

    def send_msg(socket):
        global msg
        while True:
            msg = sys.stdin.readline()
            if msg.lower() == "exit":
                print "Closing Chat"
                time.sleep(1)
                break
            server.send(msg)
            sys.stdout.write("<You>")
            sys.stdout.write(msg)
            sys.stdout.flush()


    def recv_msg(socket) :
        while True :
            msg = socket.recv(4096)
            print msg

    global msg
    
    while True:
        msg = server.recv(4096)
        print "<Server>" + msg

        
        msg = raw_input(">> ")
        if len(msg) > 0 :
            if msg.lower() == "exit" :
                "Closing chat..."
                time.sleep(1)
                break
            server.send(msg)
            sys.stdout.flush()

    server.close()
