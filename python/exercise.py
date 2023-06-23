print("Snake Water Gun : THE GAME")
snake=1
gun=2
water=3
item=[snake,gun,water]
import random
choice = random.choice(item)
print('Type 1 for snake\n','Type 2 for gun\n','Type 3 for water\n')
user_input=int(input('Enter your choice from 1-3: '))
print(f'The input of computer is {choice}')
entry=input('You wanna play (yes OR no) : ')
if(entry=="yes"):

    if(user_input==1 and choice==2):
            print('You Lose!')
    elif(user_input==1 and choice==3):
            print('You WIN !')
    elif(user_input==2 and choice==1):
            print('You WIN !')
    elif(user_input==2 and choice==3):
            print('You Lose !')
    elif(user_input==3 and choice==1):
            print('You Lose !')
    elif(user_input==3 and choice==2):
            print('You WIN !')
    elif(user_input==choice):
            print('Its a draw !')
    else:
            print("INVALID INPUT !\n PLEASE CHECK THE INPUT")
        
print("THANKS FOR PLAYING GAME !")