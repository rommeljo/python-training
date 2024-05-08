email=input("Enter email").split("@")
if email.count("a")==1:
    print(email)
else:
    print("invalid email")