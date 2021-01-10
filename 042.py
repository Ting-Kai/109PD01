form = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
ouput = []
input_str = list(map(str,input().split(' ')))

for item in input_str:
    mos = ''
    for char in item:
        mos += form[ord(char)-97]
     
    if mos not in ouput:
        ouput.append(mos)
        
print(len(ouput))