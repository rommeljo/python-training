attempts=0
for attempts in range(1,5):
    password=input("Enter Password")
    if password=="admin@123":
        print("Access granted")
    else:
        attempts+=1
        print("Try again")
print("Blocked")





