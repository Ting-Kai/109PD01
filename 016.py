name = input()
height = int(input())
weight = int(input())
height /= 100
BMI = weight / (height * height)
if(BMI < 18.5):
    print('Hi %s, Your BMI: %f too LOW.' % (name,BMI))
elif(BMI > 24):
    print('Hi %s, Your BMI: %f too HIGH.' % (name,BMI))
else:
    print('Hi %s, Your BMI: %f.' % (name,BMI) )