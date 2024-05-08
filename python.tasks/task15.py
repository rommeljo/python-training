basic=float (input( "Enter Basic Salary "))
benefits=float(input("Enter Benefits "))
Gross_Salary=basic+benefits
print ("Gross Salary =",Gross_Salary)

if Gross_Salary>=0 and Gross_Salary<=5999:
        nhif_contribution=150
elif Gross_Salary >=6000 and Gross_Salary <=7999:
        nhif_contribution=300
    
elif Gross_Salary>= 8000 and Gross_Salary <= 11999 :
        nhif_contribution = 400
    
elif Gross_Salary>= 12000 and Gross_Salary <= 14999 :
        nhif_contribution = 500
    
elif Gross_Salary>= 15000 and Gross_Salary <= 19999:
          
        nhif_contribution = 600
    
elif Gross_Salary>= 20000 and Gross_Salary <= 24999:
        nhif_contribution = 750
    
elif Gross_Salary>= 25000 and Gross_Salary <= 29999:
        nhif_contribution = 850
    
elif Gross_Salary>= 30000 and Gross_Salary <= 34999 :
        nhif_contribution = 900
    
elif Gross_Salary>= 35000 and Gross_Salary <= 39999:
        nhif_contribution = 950
    
elif  Gross_Salary>=40000 and Gross_Salary<=44999:
        nhif_contribution = 1000
    
elif Gross_Salary>= 45000 and Gross_Salary <= 49999:
         
        nhif_contribution = 1100
    
elif Gross_Salary>= 50000 and Gross_Salary <= 59999 :
        nhif_contribution = 1200
    
elif  Gross_Salary>= 60000 and Gross_Salary <= 69999 :
        nhif_contribution = 1300
    
elif  Gross_Salary>= 70000 and Gross_Salary <= 79999:
        nhif_contribution = 1400
    
elif Gross_Salary>= 80000 and Gross_Salary <= 89999 :
        nhif_contribution = 1500

elif Gross_Salary>= 90000 and Gross_Salary <= 99999:  
        nhif_contribution = 1600

else:
     nhif_contribution=1700
    
print("NHIF CONTRIBUTION =",nhif_contribution)

if Gross_Salary>18000:
        Nssf=0.06*Gross_Salary
        print("NSSF =" ,Nssf)
else:
        print("NO NSSF")

Nhdf=Gross_Salary*0.015
print("NHDF =",Nhdf)

taxable_income= Gross_Salary - (Nssf+Nhdf)
print("TAXABLE INCOME =",taxable_income)

relief=2400
if taxable_income>=0 and taxable_income<=24000:
        payee=0
    
elif taxable_income>24000 and taxable_income<=32333:
        payee=(24000*0.01)+((taxable_income-24000)*0.25)-relief
    
elif taxable_income>32333 and taxable_income<=500000:
        payee=(24000*0.01)+(8333*0.25)+((taxable_income-32333)*0.3)-relief
    
elif taxable_income>500000 and taxable_income <=800000:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+((taxable_income-500000)*0.325)-relief
else:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+(300000*0.325)+((taxable_income-800000)*0.35)-relief
print("PAYEE =",payee)

net_salary=Gross_Salary-(nhif_contribution+Nssf+Nhdf+payee)
print("NET SALARY =",net_salary)