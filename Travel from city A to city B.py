print('Travel from city A to city B!')
Time = int(input('Enter time: '))
Longer = int(input('Enter Longer: '))

if (Time >= Longer):
    Price = int(input('Enter price: '))
    Higher= int(input('Enter higher price: '))
    if (Price>=Higher):
        print('train')
    else:
        print('coach')
else:
    Price = int(input('Enter price: '))
    Higher= int(input('Enter higher price: '))
    if(Price>=Higher):
        print('daytime flight')
    else:
        print('red eye flight')
print('arrive at city B')