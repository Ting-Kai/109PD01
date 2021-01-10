def f1(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return 2*f1(n-1) + 3*f1(n-2)

try:        
    n = int(input())
    kn = f1(n)
    print(kn)
except:
    print('Error')
    