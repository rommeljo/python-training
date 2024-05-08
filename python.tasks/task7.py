marks=int(input("Enter marks:"))
if marks>=0 and marks<=100:
    if marks>=79:
        print("A")
    elif marks>=60:
        print("B")
    elif marks>=49:
        print("C")
    elif marks>=40:
        print("D")
    else  :
        print("E")  
else:
    print("invalid marks")
