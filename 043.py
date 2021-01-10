import copy

def input_data(school_data):
    
    data_amount = int(input())
    
    for i in range(data_amount):
        data = input().split(' ')
        school_data[data[0]] = data[1:]
        
    return school_data

def input_search_data(search_data):
    
    search_amount = int(input())
    
    for i in range(search_amount):  
        
        answer = input().split(' ')
        
        prev = 0
        answer_group = []
        
        for i,e in enumerate(answer):
            if(type(e) == str and e == '+'):
                answer_group.append(answer[prev:i])
                prev = i+1
                
        answer_group.append(answer[prev:])
                            
        search_data.append(answer_group)
        
    return search_data

def judge(search_data,school_data):
    
    
    for item in school_data.items():
        bol = True
        for e in search_data:
            bol = bol and (e in item[1])
                
        if(bol):
            print(item[0],end=' ')
        
        

#school_data = {'NSYSU': ['NC', 'CT', 'NS', 'NM'], 'NTU': ['BC', 'NC', 'CT', 'NS'], 'NCCU': ['BC', 'NL', 'HL'], 'Providence': ['BC', 'NC'], 'NTHU': ['BC', 'NS']}
school_data = {}
school_data = input_data(school_data)

#search_data = input().split(' ')
search_data = []
search_data = input_search_data(search_data)

for i in search_data:
    sd = copy.deepcopy(school_data)
    for j in i:
        judge(j,sd)
    print('')

    
