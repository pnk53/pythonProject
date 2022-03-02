print('Enter a number: ')
num = int(input())
strnum = str (abs(num))
rev = ''

for c in strnum:
    rev = c + rev

if(num < 0):
    rev = '-' + rev

if(num == int(rev)):
    print('Palindrome')

else:
    print('Not palindrome')