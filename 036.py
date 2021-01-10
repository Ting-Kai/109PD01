def f1(n):
    if(n == 1):
        return 2
    else:
        return(f1(n-1)+n)
    
n = int(input())
print(f1(n))