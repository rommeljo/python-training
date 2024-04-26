first_name="  JoHN  "
second_name="  Doe"
full_name=first_name+" "+second_name
print(full_name)
first_name=first_name.strip().title()
print(first_name)
second_name=second_name.strip().title()
print(second_name)
full_name=first_name+" "+second_name
print(full_name)
print(len(full_name))
#check if its email
email="john@mail.com"
print(email.count("@")== 1)

#split-it breaks up string according to a criteria
st="This is my book"
print(type(st.split(" ")))



