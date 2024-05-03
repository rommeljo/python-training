my_ds=[23,"Jane",(560),["Lesson","Maths",{"currency":"Kes"}]
       ,987,(76,"John")]                                          
kes=my_ds[3][2].values()
print(kes)
five=my_ds[2]
print(five)
mat=my_ds[3][1]
print(mat)
my_ds[3][2]["amount"]=90
print(my_ds)
str(my_ds[4])
my_ds[4]=789
las=list(my_ds[5])
las[1]="jane"
tuple(las)
my_ds[5]=las
print(my_ds)

