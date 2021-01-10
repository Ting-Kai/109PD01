lst1 = list(map(str,input().split(' ')))
lst2 = list(map(int,input().split(' ')))


for i in range(len(lst2)-1):
    for j in range(len(lst2)-1-i):
        if(lst2[j] > lst2[j+1]):
            lst2[j], lst2[j+1] = lst2[j+1], lst2[j]
            lst1[j], lst1[j+1] = lst1[j+1], lst1[j]
            
for i in lst1:
    print(i,end='')