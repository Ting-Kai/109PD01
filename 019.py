def printmark(n):
    for i in range(n):
        print('#',end='')
        
def printnumber(n):
    for i in range(n,0,-1):
        print(i,end='')
 
n = int(input())

for i in range(n,0,-1):
    printmark(n)
    printnumber(i)
    n += 1
    print('')
