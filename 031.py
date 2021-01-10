import sys
def fullarray(begin,end,nums):
    if begin==end:
        k=nums[:]
        for num in range(len(k)):
            if(num == len(k)-1):
                for i in k:
                    print(i,end='')
                sys.exit()
            elif(k[num] == k[num+1]):
                break
    else:
        for i in range(begin,end):
            nums[begin],nums[i] = nums[i],nums[begin]
            fullarray(begin+1,end,nums)
            nums[begin],nums[i] = nums[i],nums[begin]
            

nums=list(map(int,input().split(' ')))
nums.sort()
fullarray(0,len(nums),nums)





