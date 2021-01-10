def get_permutations(clst):
    if len(clst)==1:
        return [clst[0]]
    results = []
    for i in range(len(clst)):
        results += [clst[i]+substr for substr in get_permutations(clst[:i] + clst[i+1:])]
    return results
        

clst = list(map(str,input().split(' ')))

clst = get_permutations(clst)
clst.sort()


for i in range(len(clst)):
    clst[i] = list(clst[i])
    for j in range(len(clst[i])):
        clst[i][j] = int(clst[i][j])
    if(i != len(clst)-1):
        print(clst[i],end=',\n')
    else:
        print(clst[i])

    

