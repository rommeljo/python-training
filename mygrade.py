marks=int(input("Enter marks:"))
if marks>=0 and marks<=100:
    if marks>=70:
        print("A")
    elif marks>=60:
        print("B")
    elif marks>=50:
        print("C")
    elif marks>=40:
        print("D")
    else  :
        print("E")  
else:
    print("invalid marks")
