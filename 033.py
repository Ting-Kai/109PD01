N = input()

while(N != '-1'):
    lst = list(map(int,N.split(' ')))
    lst.sort()
    GND = 0
    for i in range(1,lst[0]+1):
        if(lst[0]%i==0 and lst[1]%i==0 and lst[2]%i==0):
            GND = i
    print(GND)
    N = input()