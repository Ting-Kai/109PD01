dict = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':0.5,'Q':0.5,'K':0.5}

XPoint = YPoint = 0
Rounds = 0
GameOver = False

XCard, YCard = map(str,input().split(' '))
XPoint += dict[XCard]
YPoint += dict[YCard]
Rounds += 1
while(not GameOver):
    string = input().split(' ')
    
    if(string[0] == '1'):
        
        XPoint += dict[string[1]]
        if(string[2] == '1'):
            YPoint += dict[string[3]]
            
    elif(string[0] == '0'):
        
        if(string[1] == '1'):
            YPoint += dict[string[2]]
        elif(string[1] == '0'):
            GameOver = True
    
    Rounds += 1
    
    if(XPoint > 21):
        XPoint = 0
        GameOver = True

    if(YPoint > 21):
        YPoint = 0
        GameOver = True
        
    if(Rounds >= 5):
        GameOver = True
        
if(XPoint > YPoint):
    print('Player X is Winner')
else:
    print('Player Y is Winner')
    
if(XPoint == 0):print('Player X $ Bang!')
else:print('Player X $ {0}'.format(XPoint))

if(YPoint == 0):print('Player Y $ Bang!')
else:print('Player Y $ {0}'.format(YPoint))