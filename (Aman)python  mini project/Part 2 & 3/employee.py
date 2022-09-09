def check_hr(id):
    flag = False
    f = open("HR.txt", 'r')
    h = f.readlines()
    for i in h:
        j = i.split('\t')
        if id == j[0]:
            flag = True
    return flag


def view_details(id):
    f1 = open("HR.txt", 'r')
    f2 = open("EMP.txt", 'r')
    emp1 = f1.readlines()
    emp2 = f2.readlines()
    for i in emp1:
        j = i.split('\t')
        if id == j[0]:
            return i
    for i in emp2:
        j = i.split('\t')
        if id == j[0]:
            return i
    else:
        return "Employee doesn't exist...!!!"


def view_employee(designation):
    file = open('EMP.txt', 'r')
    emp = file.readlines()
    for i in emp:
        j = i.split('\t')
        if designation == j[3]:
            print(i)
    return 0


def view_hr_name():
    file1 = open('HR.txt', 'r')
    hr = file1.readlines()
    for i in hr:
        j = i.split('\t')
        print(j[1]+ '\t'+j[2]+'\t'+j[3])
    return 0

def welcome(id):
    file = open("HR.txt", 'r')
    file2 = open("EMP.txt", 'r')
    emp = file.readlines()
    emp2 = file2.readlines()
    for i in emp:
        j = i.split('\t')
        if id==j[0]:
            print(f'Welcome [{j[1]}] from HR..!!')
    for i in emp2:
        j = i.split('\t')
        if id==j[0]:
            print(f'Welcome [{j[1]}] ...!!')
    return 0


__name__ == '__main__'
id = input("Enter the id again: ")
welcome(id)
if check_hr(id):
    while 1:
        c = input(' Enter 1 to view own details\n Enter 2 to view all employees\n Enter q to exit\n   Enter your choice: ')
        if c == '1':
            print(view_details(id))
        elif c == '2':
            designation = input("Enter designation: ")
            view_employee(designation)
            if designation == 'all':
                file = open('EMP.txt', 'r')
                emp = file.readlines()
                for i in emp:
                    print(i)
        elif c == 'q':
            break
else:
    while 1:
        
        c = input(' Enter 1 to view own details\n Enter 2 to view all HR names\n Enter q to exit\n   Enter your choice: ')
        if c == '1':
            print(view_details(id))
        elif c == '2':
            view_hr_name()
        elif c == 'q':
            break