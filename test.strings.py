name="JOHn"
name=name.lower()
print(name)

sentence1="The Dog Breed is German Sherpherd"
sentenceA=sentence1[7:23]
print(sentenceA.strip())

sentence2="Defeats for the Clinton forces,this was her moment of triumph"
sentenceB=sentence2[15:30]
print(sentenceB.strip())

sentence3="The lazy dog;ran so fast;it hit the wall."
sentenceC=sentence3.split(";")
print(len(sentenceC))

first_name="Joh.n"
last_name="Do,e"
clean_name1=first_name.strip().capitalize().replace(".","")
clean_name2=last_name.strip().capitalize().replace(",","")
full_name=clean_name1+" "+clean_name2
print(full_name)

r=["E","W","C"]
word = "".join(r)
print(word)

name="John Doe"
print(name[::2])




