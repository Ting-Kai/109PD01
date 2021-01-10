lst = list(map(int,input().split(' ')))
odd = [] 
even = []
for i in lst:
    #print(type(i))
    if(i%2 == 0):
        even.append(i)#偶數
    else:
        odd.append(i)#奇數
        
even.sort()
odd.sort()

new_lst = odd + even[::-1]
print(new_lst)