def final_check(A,N,LadderNumberAmount):
    maxNum = int(N[0])
    
    for i in range(len(N)):
        
        while(int(N[i]) > maxNum):
            LadderNumberAmount += A[len(N)-(i+1)][9-maxNum]
            #print(A[len(N)-(i+1)][9-maxNum])
            maxNum += 1     
        if(maxNum == int(N[len(N)-1]) and int(i) == len(N)-1):
            LadderNumberAmount += 1

    return LadderNumberAmount


N = input()
LadderNumberAmount = 0
    
A = [[0]*9 for _ in range(len(N))]

for i in range(len(N)):
    for j in range(9):
        if(i == 0 or j == 0):
            A[i][j] = 1
        else:
            A[i][j] = A[i][j-1] + A[i-1][j]

for i in range(len(N)-1):
    for j in range(9):
        LadderNumberAmount += A[i][j]
        
#print(LadderNumberAmount)


head = int(N[0])
for i in range(head):
    if(i+1 != head):
        LadderNumberAmount += A[len(N)-1][9-(i+1)]
        #print(LadderNumberAmount)
    else:
        LadderNumberAmount = final_check(A, N, LadderNumberAmount)
        
        
LadderNumberAmount %= 1000000007
print(LadderNumberAmount)



'''
num = input()
ladderNumber = 0


def isLadderNumber(num):
    minNum = int(num[0])
    for j in range(len(num)):
        if(int(num[j]) < minNum):
            return False
            break
        else:
            minNum = int(num[j])
        if(j == len(num)-1):
            return True

for i in range(1,int(num)+1):
    print(i)
    if(isLadderNumber(str(i))):
        ladderNumber+=1
        
print(ladderNumber)
'''

