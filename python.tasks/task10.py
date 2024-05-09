prods=[['omo','30ksh','300'],['milk','50ksh','200'],
      ['bread','45ksh','359'] ,['coffee','5ksh','79']]
total_stock=0
for i in prods:
    total_stock+=int(i[2])
print(total_stock)