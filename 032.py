# S:83, H:72, D:68, C:67
card = list(map(str,input().split(' ')))

for i in range(len(card)):
    if('S'in card[i]):
        card[i] = 13*3+int(card[i][0:-1])-2
    elif('H'in card[i]):
        card[i] = 13*2+int(card[i][0:-1])-2
    elif('D'in card[i]):
        card[i] = 13*1+int(card[i][0:-1])-2
    elif('C'in card[i]):
        card[i] = 13*0+int(card[i][0:-1])-2
        
        
isFlush = True

for i in card:
    if(i//13 != card[0]//13):
        isFlush = False
        break
    
rank = [0 for _ in range(13)]

for i in card:
    rank[i%13] += 1
    
isStraight = 1
for i in range(len(rank)):
    if(rank[i] != 0):
        for j in range(1,5):
            if(rank[(i+j) % 13] > 0 and j == isStraight):
                isStraight += 1 
            elif(rank[(i+j) % 13] == 0):
                break
pair = 0

for i in rank:
    if(i==2):
        pair += 1
            
if(isFlush and isStraight==5):
    print(8)
elif(4 in rank):
    print(7)
elif(3 in rank and 2 in rank):
    print(6)
elif(isFlush):
    print(5)
elif(isStraight==5):
    print(4)
elif(3 in rank):
    print(3)
elif(pair == 2):
    print(2)
elif(pair == 1):
    print(1)
else:
    print(0)


#print(rank)   
#print(isStraight)
        
    
        