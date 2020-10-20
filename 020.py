number = int(input())

isPrime = True

for i in range(2,number):
    if(number%i == 0):
        isPrime = False
        break
    
if(isPrime):
    print('{0} is prime number'.format(number))
else:
    print('{0} is not prime number'.format(number))
        