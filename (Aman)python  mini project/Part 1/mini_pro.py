class employee_database():

    def add_employee():
        import time as t
        emp_ID=int(input('Enter ID => '))
        emp_name=input('Enter NAME => ')
        emp_DOJ=t.asctime()
        emp_designation=input('Enter DESIG => ')
        emp_salary=int(input('Enter SALARY => '))
        with open('employee.txt','a') as file:
            file.write('ID:'+str(emp_ID)+'\t\t')
            file.write('NAME:'+(emp_name)+'\t\t')
            file.write('DOJ:'+(emp_DOJ)+'\t\t')
            file.write('DESIG:'+(emp_designation)+'\t\t')
            file.write('SALARY:'+str(emp_salary)+'\n\n')

    def search_employee():
        emp_ID='ID:'+input('Enter ID=> ')
        with open('employee.txt','r') as file:
            fil=file.readlines()
            for i in fil:
                if emp_ID in i:
                    print(i)
                    break
            else:print("ID doesn't exist...!!!")

    def add_hr():
        emp_ID=int(input('Enter ID => '))
        hr_name=input('Enter NAME => ')
        hr_dept=input('Enter DEPT. => ')
        hr_role=input('Enter Hr.ROLE => ')
        with open('hr.txt','a') as file:
            file.write('ID:'+str(emp_ID)+'\t\t')
            file.write('NAME:'+(hr_name)+'\t\t')
            file.write('DEPT:'+(hr_dept)+'\t\t')
            file.write('ROLE:'+(hr_role)+'\n\n')

    def search_hr():
        emp_ID='ID:'+input('Enter ID=> ')
        with open('hr.txt','r') as file:
            fil=file.readlines()
            for i in fil:
                if emp_ID in i:
                    print(i)
                    break
            else:print("ID doesn't exist...!!!")            
            
            
            