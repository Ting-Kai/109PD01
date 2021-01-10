L,N = map(int,input().split(' '))
lst = []

while(L>1):
    
    if(N%2 == 0):
        lst.append(1)
        N = N / 2
    else:
        lst.append(0)
        N = (N+1)/2
    L -= 1

num = 0
for i in range(-1,-len(lst)-1,-1):
    if((num==1 and lst[i]==0)or(num==0 and lst[i]==1)):
        num = 1
    else:
        num = 0
            
print(num)

        
    