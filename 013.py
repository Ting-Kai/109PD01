m = int(input())
n = int(input())

add_m = m
add_total = 0

while(add_m <= n):
    add_total += add_m
    add_m += 2
    
mul_m = m
mul_total = 1

while(mul_m <= n):
    mul_total *= mul_m
    mul_m += 3
    
print(add_total)
print(mul_total)