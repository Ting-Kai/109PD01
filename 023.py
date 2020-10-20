player_Point = 0
computer_Point = 0

isEnd = False
player = False
computer = False

dict = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':0.5,'Q':0.5,'K':0.5}

card = input()
player_Point += dict[card]
card = input()
computer_Point += dict[card]

while(not isEnd):

    if(not player):
        choice = input()
        if(choice == 'Y'):
            card = input()
            player_Point += dict[card]
        else:
            player = True
        
    #print('{0:.1f} vs. {1:.1f}'.format(player_Point,computer_Point))
                
    if(not computer):
        if(computer_Point < player_Point or computer_Point < 8):
            card = input()
            computer_Point += dict[card]
        else:
            computer = True
    #print('{0:.1f} vs. {1:.1f}'.format(player_Point,computer_Point))
    
    if(player and computer):
        isEnd = True
        
    if(player_Point > 10.5):
        player_Point = 0
        isEnd = True
        
    if(computer_Point > 10.5):
        computer_Point = 0
        isEnd = True
        
print('{0:.1f} vs. {1:.1f}'.format(player_Point,computer_Point))
if(player_Point > computer_Point):
    print('player wins')
elif(player_Point < computer_Point):
    print('computer wins')
else:
     print('It\'s a tie')   