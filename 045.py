def f(bonus,num):
    
    if(num == bonus[0]):
        return 10000000
    elif(num == bonus[1]):
        return 2000000
    elif(num == bonus[2] or num == bonus[3] or num == bonus[4]):
        return 200000
    elif(num[1:] == bonus[2][1:] or num[1:] == bonus[3][1:] or num[1:] == bonus[4][1:]):
        return 40000 # 二獎
    elif(num[2:] == bonus[2][2:] or num[2:] == bonus[3][2:] or num[2:] == bonus[4][2:]):
        return 10000 # 三獎
    elif(num[3:] == bonus[2][3:] or num[3:] == bonus[3][3:] or num[3:] == bonus[4][3:]):
        return 4000 # 四獎
    elif(num[4:] == bonus[2][4:] or num[4:] == bonus[3][4:] or num[4:] == bonus[4][4:]):
        return 1000 # 五獎
    elif(num[5:] == bonus[2][5:] or num[5:] == bonus[3][5:] or num[5:] == bonus[4][5:]):
        return 200 # 六獎
    elif(num[5:] == bonus[5] or num[5:] == bonus[6] or num[5:] == bonus[7]):
        return 200 # 增開六獎
    else:
        return 0
    

bonus = []
for i in range(4):
    num = input().split(' ')
    for j in num:
        bonus.append(j)

N = int(input())
money = 0
for i in range(N):
    money += f(bonus,input())
    
print(money)