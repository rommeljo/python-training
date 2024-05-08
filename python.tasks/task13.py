attempts=0
for attempts in range(1,4):
    email=input("Enter Email")
    password=input("Enter Password")
    if password=="admin@123" and email=="admin@gmail.com":
        print("Login is Successful")
    else:
        attempts+=1
        print("Invalid username or password")
print("Blocked")

