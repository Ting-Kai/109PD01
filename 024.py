al, an, d = map(int,input().split(' '))
sum = 0
for i in range(al,an+d,d):
    print(i,end=' ')
    sum += i
    
print('')
print(sum)