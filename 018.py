case = int(input())
num = int(input())

def printNumber(n):
    for i in range(1,n):
        print(i,end='')
    for i in range(n,0,-1):
        print(i,end='')

def myPrint(n):
    for i in range(n):
        print('_',end = '')

if(case == 1):
    rows = 1
    for i in range(num):
        printNumber(rows)
        rows += 1
        print('')
elif(case == 2): 
    for i in range(num):
        myPrint(num-i-1)
        printNumber(i+1)
        myPrint(num-i-1)
        print('')   
elif(case == 3):
    for i in range(num):
        myPrint(i)
        printNumber(num-i)
        myPrint(i)
        print('')  