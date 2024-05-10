def gross(a,b):
        Gross=a+b
        return Gross
basic=float (input("Enter Basic Salary "))
benefits=float(input("Enter Benefits "))
Gross_Salary=gross(basic,benefits)
print(f"GROSS SALARY = {Gross_Salary}")

def nh(x):
        if Gross_Salary>=0 and Gross_Salary<=5999:
                x=150
        elif Gross_Salary >=6000 and Gross_Salary <=7999:
                x=300
    
        elif Gross_Salary>= 8000 and Gross_Salary <= 11999 :
         x = 400
    
        elif Gross_Salary>= 12000 and Gross_Salary <= 14999 :
         x = 500
    
        elif Gross_Salary>= 15000 and Gross_Salary <= 19999:
          
                x = 600
    
        elif Gross_Salary>= 20000 and Gross_Salary <= 24999:
                x = 750
    
        elif Gross_Salary>= 25000 and Gross_Salary <= 29999:
                x = 850
    
        elif Gross_Salary>= 30000 and Gross_Salary <= 34999 :
         x = 900
    
        elif Gross_Salary>= 35000 and Gross_Salary <= 39999:
                x = 950
    
        elif  Gross_Salary>=40000 and Gross_Salary<=44999:
                x = 1000
    
        elif Gross_Salary>= 45000 and Gross_Salary <= 49999:
         
                x = 1100
    
        elif Gross_Salary>= 50000 and Gross_Salary <= 59999 :
         x = 1200
    
        elif  Gross_Salary>= 60000 and Gross_Salary <= 69999 :
                x = 1300
    
        elif  Gross_Salary>= 70000 and Gross_Salary <= 79999:
                x = 1400
    
        elif Gross_Salary>= 80000 and Gross_Salary <= 89999 :
                x = 1500

        elif Gross_Salary>= 90000 and Gross_Salary <= 99999:  
                x = 1600

        else:
                x=1700
        return x
NHIF=nh("Nhif contribution")
print( "NHIF CONTRIBUTION = ",NHIF)

def nssf_calc(y):
       if Gross_Salary>18000:
              y=Gross_Salary*0.06
       else:
              print("NO NSSF")
       return y
Nssf=nssf_calc("nss")
print("NSSF CONTRIBUTION = ",Nssf)

def Nhdf_calc(z):        
        z=Gross_Salary*0.015
        return z
Nhdf=Nhdf_calc("NHDF")
print("NHDF CONTRIBUTION = ",Nhdf)

def calc_taxable(r):
        r= Gross_Salary - (Nssf+Nhdf)
        return r
taxable_income=calc_taxable("tax")
print("TAXABLE INCOME = ",taxable_income)

def calc_payee(u):
        relief=2400
        if taxable_income>=0 and taxable_income<=24000:
                u=0
    
        elif taxable_income>24000 and taxable_income<=32333:
                u=(24000*0.01)+((taxable_income-24000)*0.25)-relief
    
        elif taxable_income>32333 and taxable_income<=500000:
                u=(24000*0.01)+(8333*0.25)+((taxable_income-32333)*0.3)-relief
    
        elif taxable_income>500000 and taxable_income <=800000:
                u=(24000*0.1)+(8333*0.25)+(467667*0.3)+((taxable_income-500000)*0.325)-relief
        else:
                u=(24000*0.1)+(8333*0.25)+(467667*0.3)+(300000*0.325)+((taxable_income-800000)*0.35)-relief
        return u
payee=calc_payee("PAY")
print("PAYEE = ",payee)

def calc_net_salary(x):
        x=Gross_Salary-(NHIF+Nhdf+Nssf+payee)
        return x
net_salary=calc_net_salary("NET")
print("NET SALARY = ",net_salary)