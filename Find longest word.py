print('Enter a word: ')
sent = str (input())
maxlen = 0
while (sent != str(-1)):
    count = 0
    for letter in sent:
        count = count + 1

    if (count > maxlen):
        maxlen = count
    sent = input('Enter a word: ')

print(maxlen)
