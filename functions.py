#function to check if a number is even or odd
def check_number():
    a=int(input("Enter Number"))
    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
check_number()

def triangle_area():
    h=int(input("Enter Height"))
    b=int(input("Enter Base"))
    area=0.05*h*b
    print(area)
triangle_area()

def check_number(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
check_number(80)

def tri_area(x,y):
    area=(x*y)/2
    print(area)
base=int(input("enter base"))
height=int(input("enter height"))
tri_area(base,height)

def gross(a,b):
    Gross=a+b
    return Gross
basic=float (input( "Enter Basic Salary "))
benefits=float(input("Enter Benefits "))
Gross_Salary=gross(basic,benefits)
print(Gross_Salary)
