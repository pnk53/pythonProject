print('Enter the number: ')
num = int(input())
strnum = str (abs(num))
rev = ''
for c in strnum:
    rev = c + rev

if(num>0):
    print(rev)

else:
    print('-' + rev)

