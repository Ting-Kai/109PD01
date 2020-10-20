N = int(input())
num_list = []

for i in range(N):
    number = int(input())
    num_list.append(number)
    
num_list.sort()
print(num_list[-2])
print(num_list[0]*num_list[-1])
