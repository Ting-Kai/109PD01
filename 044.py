import json

def main():
    N = int(input())
    
    if(N == 0):
        print('menu = {\n}')
        return
    
    menu = {}
    for i in range(N):
        data = input().split(' ')
        menu[data[0]] = {}
        s = data[1]+'-'+data[2]
        menu[data[0]]['hours'] = s
        menu[data[0]]['items'] = {}
        
        items = data[3:]
        
        prev = 0
        for j in range(len(items)):
            if(items[j].isdigit()):
                name = ''
                for index,e in enumerate(items[prev:j]):
                    name = name + e
                    if(index != len(items[prev:j])-1):
                        name = name + ' '
                    
                price = '$'+items[j]
                menu[data[0]]['items'][name] = price
                prev = j+1
        
    print('menu = ',end='')
    JS = json.dumps(menu,indent = 2)
    print(JS.replace('\"','\''))
    
main()