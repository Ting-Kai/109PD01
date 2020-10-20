case = int(input())
num = int(input())

def myPrint(n,mark):
    for i in range(n):
        print(mark,end='')

if(case == 1):
    rows = 0
    for i in range(num):
        if(i < (num//2) + 1):
            rows += 1
        else:
            rows -= 1
        myPrint(rows,'*')
        print('')
elif(case == 2): 
    rows = 0
    for i in range(num):
        if(i < (num//2) + 1):
            rows += 1
        else:
            rows -= 1
        myPrint(((num//2) + 1) - rows,'.')  
        myPrint(rows,'*')
        print('')
elif(case == 3):
    rows = -1
    rows_2 = num//2 + 1
    for i in range(num):
        if(i < (num//2) + 1):
            rows += 2
            rows_2 -= 1
        else:
            rows -= 2
            rows_2 += 1
        myPrint(rows_2,'.')  
        myPrint(rows,'*')
        print('')
    
