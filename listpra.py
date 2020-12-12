listOfElements = [[10,2,20,30,20,20,40,50,12],10,20,30,[10,20,30,40,50,50],20]

count= 0

for item in listOfElements:
    if type(item)==list:
        count+=item.count(20)

count+=listOfElements.count(20)

print(count)


lis=[2,4,6,8]

lis2=[1,3,5,7]

lis.append(lis2)
lis.pop(3)

print('\n', dir(list))

print("v")
print("massage")
list = [1,3]
