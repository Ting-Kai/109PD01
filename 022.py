num = int(input())
total = 1
if(num<=15):
    for i in range(num,0,-1):
        total *= i
        
print(total)

