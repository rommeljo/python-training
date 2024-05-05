ls1=list(range(1,51))
print(ls1)
ls2=[]
for i in ls1:
    if i%7==0 or i%5==0:
       ls2.append(i)
print(ls2)  

ls3=list(range(10,41))
total=0
for i in range(10,41):
    total+=i
print(total)

ls3=list(range(10,51))
odd_numbers=[]
for i in ls3:
    if i%2 !=0:
        odd_numbers.append(i)
    if len(odd_numbers)==10:
        break
print(odd_numbers)  

num=int(input("Enter Number"))
for i in range(1,11):
    multiple=i*num
    print("Multiplication=",multiple)

even=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)
print(len(even))

ls5= [("Jay", 20), ("Mo", 30), ("Mya", 32) ]
numbers=ls5[0][1],ls5[1][1],ls5[2][1]
total=0
for i in numbers:
        total+=i
print(total)



