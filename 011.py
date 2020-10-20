class class_data:
    
    def __init__(self,ID,time):
        self.ID = ID
        self.time = time
        self.session = []

class_list = []


for i in range(3):
    
    classID = input()
    classTime = int(input())

    class_list.append(class_data(classID,classTime))    
    
    for j in range(class_list[i].time):
        session =int(input())
        class_list[i].session.append(session)
  
    
for i in range(3):
    for j in range(3-i):
        if(i!=i+j):
            for p in range(class_list[i].time):
                for q in range(class_list[i+j].time):
                    if(class_list[i].session[p]==class_list[i+j].session[q]):
                        print('{0} and {1} confict on {2}'.format(class_list[i].ID,class_list[i+j].ID,class_list[i].session[p]))



    
