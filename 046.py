import re
data_group = {}

N = int(input())
for i in range(N):
    data_group[input()] = 0


keyword = input().split(' ')

for key in data_group.keys():

    times = 0
    
    for k in keyword:
        times += len(re.findall(k,key,flags=re.IGNORECASE))
        
    data_group[key] = times
    
data_group = dict(sorted(data_group.items(),key=lambda item: item[1],reverse=True))
    

for key in data_group.keys():
    string = key
    for k in keyword:
        for a in re.findall(k,string,flags=re.IGNORECASE):
            string = string.replace(a,k.upper())
    
    print(string)


#print(data_group)
