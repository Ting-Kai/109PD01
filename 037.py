dict={1:0,2:0,3:1,4:1}

def f1(n):
    if(n in dict):
        return dict[n]
    else:
        a = f1(n-1)+f1(n-2)+f1(n-3)
        dict[n] = a
        return a
    
def main():
    
    n = int(input())
    if(not n<1):
        print(f1(n))

main()