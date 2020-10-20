A1 = input()
A2 = input()
A3 = input()
B1 = input()
B2 = input()
B3 = input()

dict = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':0.5,'Q':0.5,'K':0.5}

Apoint = dict[A1] +dict[A2] +dict[A3]
Bpoint = dict[B1] +dict[B2] +dict[B3]

if Apoint > 10.5:
    Apoint = 0
    
if Bpoint > 10.5:
    Bpoint = 0
    
print(Apoint)
print(Bpoint)

if Apoint > Bpoint:
    print('A Win')
elif Bpoint > Apoint:
    print('B Win')
else:
    print('Tie')