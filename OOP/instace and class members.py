class Employee:
    company_name=''
    company_location=''
    def __init__(self,eid,n,s):
        self.employee_id = eid
        self.name=n
        self.salary=s
    def print_employee_details(self):
        print('Employee Id:',self.employee_id) 
        print('Employee name:',self.name)
        print('Employee salary:',self.salary)
        print('company name:',Employee.company_name)
        print('company location:',self.company_location)


    def update_employee_salary(self,new_salary):
        self.salary= new_salary
        print('Salary is updated succesfully')
    @classmethod
    def sat_company_details(cls):
        cls.company_name=cn
        cls.company_location=cl
    @classmethod
    def update_company_location(cls,new_location):
        cls.company_location=new_location
        print('company locatiopn is updated successfully')

Employee.sat_company_details('tcs',"Banglore")
e1=Employee(1001,'Vijay Verma',55000)
e2=Employee(1002,'Mahima gupta',60000)
e1.print_employee_details()
e1.print_employee_details()
e1.update_employee_salary(660000)
e2.update_company_location('pune')
e1.print_employee_details()
e2.print_employee_details()

 
 
 


