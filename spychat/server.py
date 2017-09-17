import socket
import sys
import time
from User import User

clients = []

def startServer(IP_address, Port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((IP_address, Port))

    server.listen(1)
    print "Chat Started...\n"
    
    conn, address = server.accept()
    

    print address[0] + " connected"

        
    clientThread(conn, address)

    conn.close()
    server.close()

def clientThread(conn, address) :
    conn.send("Welcome to SpyChat!")
    time.sleep(2)
    friend = []
    if len(friend) < 1 :
        ques = ["waste","name", "age", "rating"]
        
        for i in range(4) :
            if i == 0 : 
                conn.send("Hello there. Please answer the questions that follows.")
                ans = ""
                ans = conn.recv(4096)
                while len(ans) < 1 :
                    ans = conn.recv(4096)
                    time.sleep(300)

                ques[i] = ans     
            if i>0 :
                que = "What's your {}?".format(ques[i])
                conn.send(que)
                ans = ""
                ans = conn.recv(4096)
                while len(ans) < 1 :
                    ans = conn.recv(4096)
                    time.sleep(300)

                ques[i] = ans     
        
        dict = {"name" : ques[1], "age" : ques[2], "rating" : ques[3]}
        friend.append(dict)    
        User.friends.append(dict)

    msg = ""
    while True:

        try:
            message = conn.recv(4096)
            if message :
                print "<" + address[0] + ">" + message

        except :
            continue

        msg = raw_input(">> ")
        if len(msg) > 0 :
            if msg.lower() == "exit" :
                "Closing chat..."
                time.sleep(1)
                break

            message_to_send = "<" + User.spy_name + ">" + msg

            try:
                conn.send(msg)
            except:
                conn.close()
        



