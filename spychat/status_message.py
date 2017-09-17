from globals import messages

def add_status() :
    from User import User

    if len(messages) > 0 :
        print "Your message is : " + User.status_message
        ch = raw_input("Do you want to change your status?")
        if(ch.lower() == 'y'):
            ch2 = raw_input("Do you want to select one from older status?(Y/N)")
            if (ch2.lower() == 'y'):
                print "Your old messages are :"
                for i, msg in enumerate(messages):
                    print "{}. {}".format(i, msg)
                chMsg = int(raw_input("Which one do you want as your status?(Enter index)"))
                User.status_message = str(messages[chMsg])
            else :
                cmsg = raw_input("Type in the msg you want : ")
                messages.append(cmsg)
                User.status_message = cmsg
                print "Your status message is : " + User.status_message
        else :
            print "Ok then..."
            return
    else :
        default = raw_input("Do you want the default message as your status? (Y/N) : ")
        if(default.lower() == 'y') :
            print "Your status message is : " + User.status_message
            messages.append(User.status_message)
        else :
            cmsg = raw_input("Type in the msg you want : ")
            messages.append(cmsg)
            User.status_message = cmsg
            print "Your status message is : " + User.status_message