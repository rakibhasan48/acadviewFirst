print 'Let\'s get started...'

#Keep asking for the name until user enters something
spy_name = raw_input("What is your name? : ")
while len(spy_name)<1 :
    spy_name=raw_input('Please enter your name : ')

#Pester the user until he/she enters their title
sal = raw_input("Are you a Mr. or Mrs/Ms?  ")
while len(sal)<1 :
    sal=raw_input('Please enter your title(Mr/Mrs/Ms) : ')

print 'Welcome, {sal} {name}. We are happy to see you.'.format(sal=sal,name=spy_name)



