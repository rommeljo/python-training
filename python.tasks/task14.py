attempts=0
for attempts in range(1,100000000000):
    num1=float(input("Enter Number"))
    num2=float(input("Enter Number"))
    add=num1+num2
    print(add)
    if num1==str() or num2==str():
        print("Invalid Character Entered")
        