x1, y1, x2, y2, x3, y3 = map(int,input().split(' '))

i = 0
while(True):
    n = x1*i+y1
    if(n % x2 == y2 and n % x3 == y3):
        break
    else:
        i += 1
        
print(x1*i+y1)