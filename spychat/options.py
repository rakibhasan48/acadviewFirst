def options() :
    choice = 0

    while choice != 7 :
        try :
            choice = int(raw_input("1) Add a status update\n"
                                    "2) Start Chat Server\n"
                                    "3) Join a Chat Server\n"
                                    "4) See Friends List\n"
                                    "5) Send a secret message\n" 
                                    "6) Read a secret message\n" 
                                    # "8) Read chats from a user\n" 
                                    "7) Close application\n"))

            if choice <= 0 and choice > 6:
                print "Invalid input"
                continue
            elif choice == 1 :
                from status_message import add_status
                add_status()

            elif choice == 2:
                from server import startServer

                IP_address = (raw_input("Enter the IP Address : "))
                Port = int(raw_input("Enter the Port : "))

                startServer(IP_address, Port)

            elif choice == 3:
                from join import startClient

                IP_address = str(raw_input("Enter the IP Address : "))
                Port = int(raw_input("Enter the Port : "))

                startClient(IP_address, Port)

            elif choice == 4:
                from User import User
                print "Your friends are : \n"
                count = 0
                for i in User.friends :
                    count +=1
                    for key, value in i.iteritems() :
                        print "{} : {}".format(key, value)  
                print "\nYou have {} friends".format(count)

            elif choice == 5 :
                from secret import sendSecretMsg


                IP_address = str(raw_input("Enter the IP Address : "))
                Port = int(raw_input("Enter the Port : "))

                sendSecretMsg(IP_address, Port)

            elif choice == 6 :
                from secret import recvSecretMsg

                IP_address = str(raw_input("Enter the IP Address : "))
                Port = int(raw_input("Enter the Port : "))

                msg = recvSecretMsg(IP_address, Port)

                print "\n The message is : {}".format(msg)

        except ValueError :
            print "Enter a number idiot -_-"
