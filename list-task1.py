trainees=["John",[2,["James","Mary"]]]
two=trainees[1][0]
print(two)
jam=trainees[1][1][0]
print(jam)
trainees.append(56)
trainees[1][1].insert(1,"Mike")
print(trainees)
trainees[1][0]=8
print(trainees)

trainees.remove("John")
print(trainees)
trainees[0][1].pop(2)
print(trainees)
print(len(trainees))
