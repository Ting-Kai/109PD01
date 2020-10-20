x = int(input())
y = int(input())
z = int(input())

if(x >= 21):
    totalX = (30*x)*0.8
elif(x >= 16):
    totalX = (30*x)*0.9
elif(x >= 11):
    totalX = (30*x)*0.95
else:
    totalX = 30*x
    
    
if(y >= 21):
    totalY = (70*y)*0.75
elif(y >= 16):
    totalY = (70*y)*0.85
elif(y >= 11):
    totalY = (70*y)*0.9
else:
    totalY = 70*y
    
    
if(z >= 21):
    totalZ = (40*z)*0.8
elif(z >= 16):
    totalZ = (40*z)*0.8
elif(z >= 11):
    totalZ = (40*z)*0.85
else:
    totalZ = 40*z
    
total = totalX+totalY+totalZ    

if((x+y+z)>=30):
    total *= 0.87
    
print(int(total))