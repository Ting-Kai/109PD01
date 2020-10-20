myString = input()
newString = ''
amount = 0
for index in myString:
    if(index.islower()):
        newString += index
    elif(index.isupper()):
        amount += 1

if (len(newString) == 0):
    print('No lowercase letters')
else:
    print(newString)
    
print(len(myString))
print(amount)