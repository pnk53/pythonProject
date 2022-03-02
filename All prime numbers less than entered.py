print('Enter a number: ')
num = int(input())

if(num>2):
    for i in range (2,num):
        flag = False

        for j in range (2,i):
            if(i % j == 0):
                flag = False
                break
            else:
                flag = True

        if(flag):
            print(i, end=' ')


else:
    print('Invalid input')
