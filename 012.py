a = int(input()) #網內語音
b = int(input()) #網外語音
c = int(input()) #市話
d = int(input()) #網內簡訊數
e = int(input()) #網外簡訊數

mod183 = 0.08*a + 0.1393*b + 0.1349*c + 1.1287*d + 1.4803*e
if(mod183 < 183):
    mod183 = 183

mod383 = 0.07*a + 0.1304*b + 0.1217*c + 1.1127*d + 1.2458*e
if(mod383 < 383):
    mod383 = 383

mod983 = 0.06*a + 0.1087*b + 0.1018*c + 0.9572*d + 1.243*e
if(mod983 < 983):
    mod983 = 983
    
if(mod183 < mod383 and mod183 < mod983):
    print('Type 183')
elif(mod383 < mod183 and mod383 < mod983):
    print('Type 383')
else:
    print('Type 983')