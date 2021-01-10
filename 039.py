
def c(m): 
    if(m<=1):
        return m
    lst.append(m)
    if(m%2==0):
        c(m/2)
    else:
        c((m+1)/2)
    

x = '0'
while(x !='-1'):
    lst=[]
    m = int(input(),2)
    c(m)
    time = len(lst)
    for i in range(4):
        if(time >= 2**(3-i)):
            print(1,end='')
            time = time-(2**(3-i))
        else:
            print(0,end='')
    print('')
    x = input()
