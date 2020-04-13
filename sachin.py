import getpass
user = getpass.getuser()
for history in open('/home/'+user+'/.bash_history'):
    print(history, end='')
