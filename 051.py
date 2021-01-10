paragraph,banned = input().split('|')
paragraph = paragraph.lower().split(' ')
banned = banned.split(',')
dict ={}
for i in paragraph:
    dict[i] = dict.get(i,0)+1

dict = sorted(dict.items(), key = lambda x : x[1], reverse=True)

for item in dict:
    if(item[0] not in banned):
        print(item[0])
        break

