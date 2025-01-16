import random

print("Welcome to Snake,Water,Gun game\n")



print("1 for snake,2 for water, and 3 for gun...")
print("Press 0 to quit this game...")
dict={1:'Snake',2:'Water',3:'Gun'}


while True:
    you=int(input("Enter Your Chouce According to Corresponding Number: "))
    comp=random.randint(1,3)
    if you not in dict and you != 0:
        print("Invalid input! Please choose 1, 2, 3, or 0 to quit.")
        continue
    if you!=0:
        print(f'You Chose {dict[you]} and the computer chose {dict[comp]}')
    if you==comp:
        
        print("Its a Draw!!!")
    else:
        if you==1 and comp==2:
            print("Snake Drinks Water,you win!!!")
        elif you==1 and comp==3:
            print("Gun Shoots Snake,You Lose!!!")
        elif you==2 and comp==1:
            print("Snake Drinks Water,You Lose!!!")
        elif you ==2 and comp==3:
            print("Water Destroys Gun,You Win!!!")
        elif you==3 and comp==1:
            print("Gun Shoots Snake,You Win!!!")
        elif you==3 and comp==2:
            print("Water Destroys Gun,You Lose!!!")
        
        if you==0:
            print("Exitting the Game...")
            break

    
