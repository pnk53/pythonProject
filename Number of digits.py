print('Enter a number: ')
num = abs(int(input()))
digits = 1

while (num > 9):
    num = num // 10
    digits = digits + 1

print(digits)