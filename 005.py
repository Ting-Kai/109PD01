text = input()
P = input()
Q = input()

new_text = text.replace('This','A')

line1 = new_text.replace(P, Q)
print(line1.replace('A', 'This'))
line2 = new_text.replace(P, Q+' '+P)
print(line2.replace('A', 'This'))
line3 = new_text.replace(P+' ', '')
print(line3.replace('A', 'This'))
