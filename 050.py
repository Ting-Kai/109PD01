def INPUT_DATA():
    lst = []
    while(True):
        temp = input()
        if(len(temp) == 1):break
        temp = list(map(int,temp.split(' ')))
        lst.append(temp)
        f = lambda lst:[[row[col] for row in lst] for col in range(len(lst[0]))]
        
    return f(lst)

def main():
    
    if(input() != 'A'):return 
    A = INPUT_DATA()
    B = INPUT_DATA()
    C = [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]
    
    T = ''
    for i in C:
        for j in i:
            T+=chr(j)
    print(T)
            
main()


