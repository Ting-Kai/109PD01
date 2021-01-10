string = input()
dict = {}
for i in string:
    if(i==' '):
        continue
    dict[i] = dict.get(i,0)+1
    
for item in dict.items():
    if(item[0].isdigit()):
        print(item[0],end='')
    elif(item[1]<10):
        print(item[1],end='')
