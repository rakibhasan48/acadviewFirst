
def create_user() :
    #Keep asking for the name until user enters something
    from User import User

    User.spy_name = raw_input("What is your name? : ")
    while len(User.spy_name)<1 :
        User.spy_name=raw_input('Please enter your name : ')

    #Pester the user until he/she enters their title
    User.sal = raw_input("Are you a Mr. or Mrs/Ms?  ")
    while len(User.sal)<1 :
        User.sal=raw_input('Please enter your title(Mr/Mrs/Ms) : ')

    # Get and validate age
    age = 0
    while True :
        try :
            age = int(raw_input("What is your age, {name}? ".format(name=User.spy_name)))
        except ValueError:
            print "Numbers only idiot -_- \n Try again\n"
        if isinstance(age, int) and age>0 :
            User.age = age
            break

    if User.age<18:
        print("You are still too young to be a spy....come back later ;)")
        exit()
    elif User.age>60:
        print("Time to retire, old man :|")
        exit()


    rating = 0.0

    while True:
        try:
            rating = float(raw_input("What is your rating?"))
        except ValueError:
            print "Numbers only idiot -_- \n Try again\n"
        if isinstance(rating, float) and rating >0.0 and rating <= 5.0 :
            User.rating = rating
            break

    print 'Welcome, {} {}. We are happy to see you.'.format(User.sal, User.spy_name)
    print "Your rating is {}".format(User.rating)

    #Import and call function to add status message
    from User import User
    from status_message import add_status
    add_status()
