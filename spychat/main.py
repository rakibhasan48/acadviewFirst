from User import User

print 'Let\'s get started...'

ans = raw_input("Do you want to create a new user (Else we will continue with the default user)? (Y/N)")
while not (ans.lower() == "y" or ans.lower() == "n") :
    ans = raw_input("Please enter (Y/N)")

user = User()

if ans.lower() == "y" :
    from create_user import create_user
    create_user()
else :
    print "Welcome, {} {}. We are happy to see you.".format(user.sal,user.spy_name)
    print "Your rating is {}".format(user.rating)
    print "Your status message is : {}".format(user.status_message)

from options import options
options()











