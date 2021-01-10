def f(lst):
    if(lst[:1]=='0'):
       return
    if(len(lst)<=1):
        global num
        num+=1
        return
    if(len(lst)>=2):
        if(int(lst[:2])<=26):
            f(lst[2:])
        f(lst[1:])
        
global num
num = 0     
N = input()
f(N)
print(num)