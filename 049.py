sentence = input()
k = int(input())
temp = ''
for i in sentence:
    if(i.isalpha()):
        temp += i
sentence = temp.swapcase()

temp = []
pre = 0
for i in range(len(sentence)):

    if(i%k == k-1):
        temp.append(sentence[pre:i+1])
        pre = i+1
        
temp.append(sentence[pre:])

for i in range(len(temp)-1,-1,-1):
    if(temp[i]==''):
        continue
    print(temp[i],end='')
    if(i!=0):
        print('/',end='')