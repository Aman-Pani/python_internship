def add_employee():
    f1=open('EMP.txt','a')
    f2=open('login.txt','a')
    e=emp_ID+'\t'+emp_name+'\t'+emp_DOJ+'\t'+emp_designation+'\t'+emp_salary+'\n'
    n=emp_name.split()
    emp_log='\n'+emp_ID+' '+n[0]
    f1.writelines(e)
    f2.writelines(emp_log)
    f1.close()
    f2.close()
    return 'Input successful....'

def remove(a,b,c):
    with open(b,'r') as rm:
        d=rm.readlines()
        for i in range(len(d)):
            j=d[i].split(c)
            if j[0] == a:
                d[i]=''
                break
    with open(b,'w') as rm:
        e=rm.writelines(d)
        
def remove_emp(a):
    remove(a,'EMP.txt','\t')
    remove(a,'HR.txt','\t')
    remove(a,'login.txt',' ')

def search():
    flg=False
    with open('EMP.txt','r') as file:
        fil=file.readlines()
        for i in fil:
            ID=i.split('\t')
            if ID[0] in i:
                flg=True
        return flg
    
def add_hr():
    with open ('HR.txt','a') as f:
        l=emp_ID+'\t'+hr_name+'\t'+hr_dept+'\t'+hr_role+'\n'
        f.writelines(l)
    with open('login.txt','a') as f:
        n=hr_name.split()
        emp_log='\n'+emp_ID+' '+n[0]
        f.writelines(emp_log)
    return 'Input successful....'

def remove_hr(a):
    remove(a,'HR.txt','\t')
    
while(1):
    x=input('1-> Add employee\n2-> Add hr\n3-> Remove employee\n4-> Remove hr\nq-> Exit\n   Enter choice:: ')
    if  (x=='1'):
        import time as t
        emp_ID=input('Enter ID => ')
        emp_name=input('Enter NAME => ')
        emp_DOJ=t.asctime()
        emp_designation=input('Enter DESIG => ')
        emp_salary=(input('Enter SALARY => '))    
        add_employee()
    elif(x=='2'):
        emp_ID=input('Enter ID=> ')
        if search():
            hr_name=input('Enter NAME => ')
            hr_dept=input('Enter DEPT. => ')
            hr_role=input('Enter Hr.ROLE => ')
            add_hr()
        else:print('Employee does not exist...')
    elif(x=='3'):
        emp_ID=input('Enter ID => ')
        remove_emp(emp_ID)
    elif(x=='4'):
        emp_ID=input('Enter ID => ')
        a=input('He is leaving organization..!! (y/n)=>  ')
        if a == 'y':remove_emp(emp_ID)
        else       :remove_hr(emp_ID)
    elif(x=='q'):break
    else      :print('WRONG INPUT')
   