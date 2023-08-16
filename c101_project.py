import random
print('Would you like to roll the dice?')
response=input('Press Y to roll again and Press N to exit')
response = 'y'
while response=='y':
    no=random.randint(1,6)
    if no==1:
        print('the number on the dice is 1')
    elif no==2:
        print('the number on the dice is 2')
    elif no==3:
        print('the number on the dice is 3')
    elif no==4:
        print('the number on the dice is 4')
    elif no==5:
        print('the number on the dice is 5')
    elif no==6:
        print('the number on the dice is 6')