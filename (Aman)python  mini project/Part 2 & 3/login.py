import sys
import getpass
print('***Welcome to Employee System***')
user_id =input("Please enter your Login ID =>")
password=getpass.getpass("Please enter your passwod =>")
file=open("login.txt","r")
a=file.readlines()
for i in a:
    b=i.split()
    if user_id== b[0] and password==b[1]:
        if user_id == 'admin' :
            import admin
            break
        else:
            import employee
            break
        
else:
    print('Invalid id & password')
    sys.exit()

