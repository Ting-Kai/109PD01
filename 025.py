Input = input()
while(Input != '-1'):
    height, weight = map(float,Input.split(' '))
    if(weight < 20 or weight > 300):
        print('Input Error 20~300')
    elif(height < 0.5 or height > 2.5):
        print('Input Error 0.5~2.50')
    else:
        BMI = weight / (height*height)
        if(BMI < 15.5):
            print('BMI too low')
        elif(BMI > 24):
            print('BMI too hight')
        else:
            print('{0:.2f}'.format(BMI))
    Input = input()