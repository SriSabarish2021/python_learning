
# number=50
# float_num=float(number).__ceil__(3)
# print(float_num)


# print('This is my BroCode First Programm')
# print('')
# print('The name of the project is MADLIBS GAME')
# print('')
# get_user_name=input("Please Enter Your Name : ")
# print('')
# print(f"Hello {get_user_name} Welcome to Our Community Of Changers")
# print('')
# print('The Game is not morre serious only enter the lenght and width for the Rectangle')
# print('')
# get_rect_length=input("Enter the Length of the Rectagle : ")
# get_rect_Width=input("Enter the Width of the Rectangle : ")

# Set_Area=int(get_rect_length)*int(get_rect_Width)

# print(f"From the length of {get_rect_length} and the width of {get_rect_Width} the total Area of the Rctangle is {Set_Area}CM")

#SHOPPING CART PROGRAM

# print("Welcome {get_user_name}")
# print('')
# print('This is Your Shopping Cart Page')
# print('')
# print('1: Chilly\n2: Biscuit\n3: Apple')
# print('')

# chilly_prize=100
# biscuit_prize=30
# apple_prize=50
# print(f'These are the prize list of the above items in KG\nChilly : {chilly_prize}\nBiscuit : {biscuit_prize}\n Apple : {apple_prize}')
# get_item=input('Select the Item you want to Buy in num from 1-3... : ')
# print('')
# get_quantity=int(input('Enter the number of quantity you needed in KG : '))
# print('')
# total_prize=0
# item_name=''
# if int(get_item)==1:
#     total_prize=get_quantity*chilly_prize
#     item_name='Chilly'
# elif int(get_item)==2:
#     total_prize=get_quantity*biscuit_prize
#     item_name='Biscuit'
# else:
#     total_prize=get_quantity*apple_prize
#     item_name='Apple'


# print(f'The item You Selected was {item_name} and the total prize is {total_prize}')

#MADLIBS GAME
# print('')
# print(f"Helllooo everyone i went to ________ yesterday and i saw ________ and i return by the time os _______")
# print('')
# get_place=input("Enter whare you went : ")
# print('')
# get_seen=input('Enter what you have seen : ')
# print('')
# get_time=input('Enter time you have return : ')
# print('')
# print(f"Helllooo everyone i went to {get_place} yesterday and i saw {get_seen} and i return by the time os {get_time}")

# import math
# print(math)

#hypothenis of right triangle

# get_a=int(input('enter the value A : '))
# print('')
# get_b=int(input('Enter the value B : '))
# print('')
# print(f"The Hyphotenins of the right anglied Traingle is {round(math.sqrt(pow(get_a,2) + pow(get_b,2)),3)}")

# print('')
# print(f"Hello {get_user_name} Welcome to the Calculator APP")
# print('')
# get_value_one=int(input("Please enter the 1ST value : "))
# print('')
# get_value_two=int(input("Please enter the 2ND value : "))
# print('')
# def operation_func():
#     get_operation=input('Select the any one operation from [+,-,*,/,%] : ')
#     if get_operation not in ['+','-','*','/','%']:
#         print("Please enter the valid Operation")
#         return operation_func()
#     elif get_operation=='+':
#         print(f'The Output is :{get_value_one+get_value_two}')
#     elif get_operation=='-':
#         print(f'The Output is :{get_value_one-get_value_two}')
#     elif get_operation=='*':
#         print(f'The Output is :{get_value_one*get_value_two}')
#     elif get_operation=='/':
#         print(f'The Output is :{round(get_value_one/get_value_two,3)}')
#     else:
#         print(f'The Output is :{round(get_value_one%get_value_two,3)}')

# operation_func()


# print('')
# print(f"Hello {get_user_name} Welcome to the Weight Conversion APP")
# print('')
# get_Weight=int(input("Please enter Your Weight : "))
# Your_unit=input('Mention Your weight Kilogram or Pounds (K OR P) : ')
# print('')

# def weight_func():
#     if Your_unit not in ['K','k','P','p']:
#         print("please enter the valid weight scale value")
#         return weight_func()
#     elif Your_unit=='k' or Your_unit=='K':
#         print(f"The Weight converted from KG to Pounds is : {round(get_Weight*2.205,2)}")
#     else:
#         print(f"The Weight converted from Pound to KG is : {round(get_Weight*0.45359237,2)}")

# weight_func()


# WEATHER CONVERSION APP

# import requests

# def weather_app():
#     get_inp=input("Mention Your City : ").lower()
#     print(get_inp)

#     request_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={get_inp}&appid={'1ba216e48f6aab5bdb1c87c858525415'}")
#     get_data=request_data.json()

#     print(f'Your City name is {get_inp}')
#     print(f"The Temperatur in your city in kelvin is: {get_data['main']['temp']}'K'")
#     print(f"The Temperatur in your city in Celcious is: {round(int(get_data['main']['temp'])- 273.15,2)}'C'")
#     print(f"The Temperatur in your city in Farenheit is: {round((int(get_data['main']['temp'])- 273.15) * 9/5 + 32,2)}'F'")


# weather_app()


# number=1
# print('hellopp') if number==2 else weather_app() if number==1 else print('not') if number==4 else print('no')


# name="sri sabarish"

# print(name[1:4])





# print(f'This is the Compund Interest Calculating Program')
# print('')
# print(f'We Welcome You {get_user_name}')
# print('')
# get_year=int(input('Enter your Time Period : '))
# print('')
# get_principle_amt=int(input("Enter Your Principle AMT : "))
# print('')
# get_interest_rate=int(input('Enter Your Rate of Interest : '))
# print('')

# while get_year<1 or get_year=='':
#     print("The year you entered is not valid")
#     get_year=int(input('Enter your Time Period : '))
#     print('')
#     if get_year<1:
#         print('Please enter Valid Year')


# while get_principle_amt<1 or get_principle_amt=='':
#     print("The AMOUNT you entered is not valid")
#     get_principle_amt=int(input('Enter Your Principle AMT : '))
#     print('')
#     if get_principle_amt<1:
#         print('Please enter Valid Your Principle AMT ')


# while get_interest_rate<1 or get_interest_rate=='':
#     print("The Rate of Interest you entered is not valid")
#     get_interest_rate=int(input('Enter your Your Rate of Interest : '))
#     print('')
#     if get_interest_rate<1:
#         print('Please enter Valid Rate of Interest')

# while get_year>=1:
    
#     get_yearly_amt=get_principle_amt*(get_interest_rate/100)
#     get_principle_amt=get_principle_amt+get_yearly_amt
#     print(get_yearly_amt)
#     print(get_principle_amt)
#     get_year-=1
# else:
#     print(f"Your Total amount with interest is = {get_principle_amt}")


# import time
# get_seconds=int(input('Enter the Seconds : '))

# for x in reversed(range(0,get_seconds)):
#     get_sec=x % 60
#     get_minites=int(x/60)%60
#     get_hour=int(x/3600)
#     print(f"{get_hour:02}:{get_minites:02}:{get_sec:02}")
#     time.sleep(1)

# arr_one=['sri','balu','mani']
# arr_two=['food','cloths','shelter']
# for x in arr_one:
   
#     for y in arr_two:
#         print(f"{x} - {y}")
#         print()


# set_one={2,3,4,5,6,6}

# for x in set_one:
#     print(x)

# fruits=[]
# prices=[]
# while True:
 

#     fruit=input('Enter the fruits you want to add (or to quit enter "q") : ')

#     if fruit.lower()=='q':
#         break
#     else:
#         fruits.append(fruit)
#         price_inp=input(f"Enter the valid price for {fruit} : ")
#         prices.append(price_inp)
#         print(f"Your Fruits Cart : {fruits}")
#         print(f"and the price of the fruits is : {prices}")


# list_one=['sri','sabari','hari','mani']
# list_two=[1,2,3,4,5]
# list_three=['apple','banana','pineapple','grapes']

# D_lists=[list_one,list_two,*list_three]
# print(D_lists)

# key_pad=((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))


# for indi_key in key_pad:
#     for keys in indi_key:
#         print(keys,end="  ")

#     print(' ')


# Question=(
#     "Elon Musk recent project ?",
#     "How long is MARS from EARTH"
# )
# Answers=(
#     ('A. Starship-9','B. Starship-1','C. Starship-8','D. Starship-10'),
#     ('A. 1km','B. 10000km','C. 800km','D. 1000500km')
# )
# Correct_ans=('D','B')

# Score=0
# quest_num=0

# for quest in Question:
#     print('---------------------------')
#     print(quest)
#     for Option in Answers[quest_num]:
#         print(Option)
#     print('')
#     get_ans=input('Enter Your Answer : ').upper()

#     if get_ans==Correct_ans[quest_num]:
#         print('')
#         print('Your answer is Correct')
#         Score+=1
#     else:
#         print(f'Your answer is InCorrect Answer is : {Correct_ans[quest_num]}')

#     quest_num+=1    

# print(f'The total Score you have gained is : {Score}')


#PROJECT TIME


# Sakthi__cini_menu={
#     "coke":100,
#     "rice":120,
#     "popcorn":80,
#     "drinks":140,
#     "icecream":60,
#     "pufs":35
# }
# print(Sakthi__cini_menu)
# selected_items=[]
# total=0
# while True:
#     get_items=input("Enter Your Snacks (or) Want to Quit Enter ['q'/'Q'] : ").lower()
#     if get_items=='q':
#         break
#     elif Sakthi__cini_menu.get(str(get_items)) is None:
#         print('*******************')
#         print('The Items is not in the Menu Please go with Avialable items')
#         print('*******************')
#     else:
#         selected_items.append(str(get_items))
#         print('')
#         print('The Items you have selected are listed below: ')
#         print('-------------')
#         total=0
#         for indiitemss in selected_items:
#             print(f"The item you seleted is {indiitemss} = {Sakthi__cini_menu[str(indiitemss)]}")
#             total+=Sakthi__cini_menu[str(indiitemss)]
            
#         print('--------*--------')
#         print(f'The total Amount is : {total}')


import random
# items=['rock','papaper','scissors']

# print(random.shuffle(items))
# print(items)

# guess_count=0
# initial_num=1
# end_num=50
# computer_random=int(random.randint(initial_num,end_num))
# while True:
#     get_user_num=int(input("Enter Random Number : "))
#     guess_count+=1
#     if get_user_num == computer_random:
#         print("************")
#         print('Success Your Guess Matches')
#         print("************")
#         print(f"Your Total Guesses = {guess_count}")
#         break
#     elif get_user_num < initial_num or get_user_num > end_num :
#         print("************")
#         print('Your Guess is out of range Please select number from 1 - 50')
#         print("************")
#     elif get_user_num < computer_random:
#         print("************")
#         print('Your Guess Too low')
#         print("************")
#     else:
#         print("************")
#         print('Your Guess Too high')
#         print("************")


# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")


# dice={
#     1:( "┌──────────┐",
#         "│          │",
#         "│    ●     │" ,
#         "│          │",
#         "└──────────┘"),
#     2:( "┌──────────┐",
#         "│    ●     │",
#         "│          │" ,
#         "│    ●     │",
#         "└──────────┘"),
#     3:( "┌──────────┐",
#         "│     ●    │",
#         "│     ●    │" ,
#         "│     ●    │",
#         "└──────────┘"),
#     4:( "┌──────────┐",
#         "│  ●    ●  │",
#         "│          │" ,
#         "│  ●    ●  │",
#         "└──────────┘"),
#     5:( "┌──────────┐",
#         "│  ●    ●  │",
#         "│    ●     │" ,
#         "│  ●    ●  │",
#         "└──────────┘"),
#     6:( "┌──────────┐",
#         "│   ●  ●   │",
#         "│   ●  ●   │" ,
#         "│   ●  ●   │",
#         "└──────────┘")
# }
# random_arr=[]

# user_dice=int(input('Enter the total Dice : '))
# total=0

# for num in range(user_dice):
#     random_num=random.randint(1,6)
#     random_arr.append(int(random_num))

# for die_num in range(user_dice):
#     for line in dice.get(random_arr[die_num]):
#         print(line)


# for all_num in random_arr:
#     total+=all_num
    
# print(f"total : {total}") 



# def argu(**name):
#     print(f"{name}")

# argu(f_name='sri',l_name='sabarish',father_name='nataraj',Mother_name='valarmathi')

# obj_one={"name":'Sri Sabarish',
#          "age":20,
#          "Degree":'MBA'}
# id="age"
# if id not in obj_one:
#     print('no')
# for val in obj_one:
    
#     print(obj_one[val])


# fruits=["apple","banana",'pineapple']
# get_upper=[fruit.upper() for fruit in fruits]
# print(get_upper)

# number=[-1,2,3,-4,-6,-7]
# get_positive=[num for num in number if num > 0]
# print(get_positive)
# num=1
# get_vr=print('hello') if num==2 else print('no') if num==4 else print('hey...')

# day_inp=''

# def get_day_func():
#     global day_inp
#     day_inp=input('Enter the day : ').lower()
#     match day_inp:
#         case 'monday':
#             print('Bad day')
#         case 'tuesday':
#             print('Almost Gooder one')
#         case 'wednesday' | 'thursday':
#             print('Best day')
#         case 'friday' | 'saturday':
#             print('great day')
#         case 'sunday':
#             print('rest day')
#         case _:

#             print('Enter valid day')
#             return get_day_func()
  
# get_day_func()



#PROGRAMMS OF GAME

#BANKING PROGRAM

# import argparse
# import sys
# parser=argparse.ArgumentParser(
#     description="Getting Name of the User"
# )
# parser.add_argument(
#     '-n','--name',metavar='name',
#     required=True
# )
# get_name=parser.parse_args()
# user_name=get_name.name

# bank_balance=0
# def banking_programm():
#     global bank_balance
#     print("Banking Programm".center(40,'*'))
#     print('')
#     print(f"Hello.. {user_name} welcome to our CODE bank")
#     print('')
#     print('Select the required Services Number(1,2,3,4)\nMentioned Below : ')
#     print('****************')
#     print('1:Bank Balance')
#     print('2:Deposite')
#     print('3:Withddrawl')
#     print('4:EXIST')
#     print('****************')
#     get_user_inp=input('Enter the required Service Number : ')

#     match get_user_inp:
#         case '1':
#             print(f"Your Account Balance is : {bank_balance:.2f}")
#             return banking_programm()
#         case '2':
#             get_amt_for_DEPO=int(input("Enter AMT to Deposite : "))
#             bank_balance+=get_amt_for_DEPO
#             print(f"The Amount of {get_amt_for_DEPO:.2f} is Deposited to your Account Succesfully....")
#             print('')
#             print(f'Current Balance : {bank_balance:.2f}')
#             return banking_programm()
#         case '3':
#             if bank_balance==0:
#                 print('')
#                 print('Please Deposite an Amount to Withdrawl')
#                 print('')
#                 return banking_programm()
             
#             get_amt_for_withdrwl=int(input("Enter AMT to Withdrawl : "))
#             if get_amt_for_withdrwl>bank_balance:
#                 print('')
#                 print('Balance in Your Account is low to withdrawl')
#                 print('')
#                 print(f'Current Balance : {bank_balance:.2f}')
#                 print('')
#                 print(f'Withdrawl AMT : {get_amt_for_withdrwl:.2f}')
#                 return banking_programm()
#             else:                  
#                 bank_balance-=get_amt_for_withdrwl
#                 print(f"The Amount of {get_amt_for_withdrwl:.2f} is Withdrawl from your Account Succesfully....")
#                 print('')
#                 print(f'Current Balance : {bank_balance:.2f}')
#                 return banking_programm()
#         case _:
#             print('****************')
#             print('')
#             sys.exit('Thank You for an Member in CODE Bank')
#             print('')
#             print('****************')
            


# banking_programm()


#Slot Machine Game 
import random
# game_balance=0
# def Slot_Game():
#     global game_balance
#     print("SloTgaMe".center(50,'*'))
#     print('')
#     print(f'Hello.. {user_name} Welcome to the Slot Game...')
#     print('')
#     print('Enter the initial Amount to start the Game (Minimal Deposite : 50)')
#     print('')
#     def amt_deposite():
#         get_amt=int(input('Initial Deposite : '))
#         if get_amt<50:
#             print(f'Minimal Deposite is 50 but your Entered AMT is {get_amt:.2f}')
#             return amt_deposite()
#         else:
#             return get_amt
    
#     game_balance+=int(amt_deposite())

#     def main_slot_flow_game():
#         global game_balance
#         if int(game_balance)==0 or int(game_balance)<0:
            
#             print('***********')
#             print(f'The Balance in your Account is : {game_balance:.2f}')
#             print('***********')
#             print('Please Deposite amt to continue')
#             print('')
#             get_again_deposite=int(input("Again Deposition : "))
#             game_balance+=get_again_deposite
#             return main_slot_flow_game()
#         else:
#             print('')
#             print('Your Slots are 🍇 🍉 🍌 🍎 🍐')
#             print('')
#             print('*************')
#             print(f'Your Curresnt Balance is = {game_balance:.2f}')
#             print('')
#             Get_bet_amt=int(input('Enter the Bet AMT : '))
#             print('*************')
#             print('')
#             print('Slotting.....')
#             print('')
#             slot_arr=['🍇','🍉','🍌','🍎','🍐']
#             choice_one=random.choice(slot_arr)
#             choice_two=random.choice(slot_arr)
#             choice_three=random.choice(slot_arr)
#             print(f'Your Slots are :{choice_one}|{choice_two}|{choice_three}')
#             if choice_one==choice_two==choice_three:
#                 game_balance+=Get_bet_amt
#                 print('')
#                 print('Hurray..... You Won the Game...')
#                 print('')
#                 print('******************')
#                 print(f'You Earn the Profit of Rupees : {Get_bet_amt:.2f}')
#                 print('******************')
#                 print(f'Current Balance in your ACCOUNT is : {game_balance:.2f}')
#                 print('------------------')
#             else:
#                 game_balance-=Get_bet_amt
#                 print('*******************')
#                 print('Sorry Your Luck Not Good by Now')
#                 print('*******************')
#                 print(f'The amount of rup={Get_bet_amt} is deducted from your account')
#                 print('')
#                 print(f'The Balance in your account is {game_balance:.2f}')
#                 print('')

#                 def user_response():
#                     get_response_val=input('Want to try Again(y) or Quit(q) -- (y/q) : ').lower()
#                     return get_response_val
#                 get_response=user_response()
#                 if get_response=='q':
#                     print('(****************)')
#                     sys.exit('ThanK You For Playing the Game')
#                 elif get_response=='y':
#                     return main_slot_flow_game()
#                 else:
#                     print('')
#                     print('Enter Valid Data Input')
#                     print('')
#                     return user_response()  
    
#     main_slot_flow_game()

# Slot_Game()



# from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# print(key)
# main_key=Fernet(key)
# print(main_key)

# get_input_to_encrypt=input('Enter the text to encrypt : ')
# encrytp=main_key.encrypt(b'{get_input_to_encrypt}')
# print(encrytp)
# decrytp=main_key.decrypt(b'{encrytp}')

import sys

def hangman_game():
  
    attempt=0
    hang_man_obj={
         1: """
       -----
       |   |
       |   O
       |
       |
       |
    --------
    """,

    2: """
       -----
       |   |
       |   O
       |   |
       |   |
       |
    --------
    """,

    3: """
       -----
       |   |
       |   O
       |  /|\\
       |   |
       |
    --------
    """,

    4: """
       -----
       |   |
       |   O
       |  /|\\
       |   |
       |  / \\
    --------
    """
    }
    hang_man_img_arr=[]
    words=['apple','mango','pinepple','grapes','banana','watermelon']
    get_random_word=random.choice(words)
    print(get_random_word)
    print('****************')
    print('')
    print('Welcome to HangMan Game')
    print('')
    print('****************')
    
    display_word = ["_"] * len(get_random_word)
   
    print(" ".join(display_word)) 
    def main_func():
        nonlocal attempt
        nonlocal hang_man_obj
        nonlocal hang_man_img_arr
        nonlocal display_word
        def user_inp():   
            print('')
            get_user_inp=input('Find the Word to be filled : ').lower()
            print('')
            num_arr=['1','2','3','4','5','6','7','8','9','0']
            if len(get_user_inp)>=2:
                print('Please Enter One Word')
                return user_inp()
            elif get_user_inp in num_arr:
                print('Please Enter Alphabets')
                return user_inp()
            return get_user_inp
        get_user_val=user_inp()
        if get_user_val in get_random_word:
            for idx, letter in enumerate(get_random_word):
                if letter == get_user_val:
                   
                    display_word[idx] = get_user_val
            print(" ".join(display_word))
            print('')
            if "_" not in display_word: 
                print('')
                print("🎉 Congratulations! You guessed the word:", get_random_word)
                print('')
                get_inp_for_continue=input('Want to continue (y) or quit (q) : ').lower()
                if get_inp_for_continue=='y':
                    hangman_game()
                else:
                    print('')
                    sys.exit("Thanks for Playing the Game")  
            return main_func()
        else:
            attempt+=1
            if attempt<=4:
               
                hang_man_img_arr.append(hang_man_obj[attempt])
                for img_hang_man in hang_man_img_arr:
                    print(img_hang_man)
                
                if attempt==4:
                    sys.exit(f'You have reached your maximum of {attempt} attemps')
                else:
                    return main_func()
                

    main_func() 
          

# hangman_game()



# class animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def eat(self):
#         print(f'{self.name} eats')
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Dog(animal):
#     def __init__(self, name, age,bark):
#         super().__init__(name, age)
#         self.bark=bark
    
#     def sound(self):
#         print(f"{self.name} sounds like {self.bark}")

# class mouse(Dog):
#     pass

# dog=Dog('Chipppi',4,'vovvv')
# mouse=mouse('Jerry',5,'ichhh')
# print(dog.sound())
# print(mouse.sound())





# class basic_info:
#     degree="MBA"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_info(self):
#         print(f"{self.name} is {self.age} old and he is currently pursuing {self.degree}")


# student_one=basic_info("Sri Sabarish",15)


# class main_info(basic_info):
#     Clg="Vivekananda Institute of management studies"

#     def __init__(self, name, age,pan,aadhaar):
#         super().__init__(name, age)
#         self.pan=pan
#         self.aadhaar=aadhaar

#     def getter(self,clg):
#         self.Clg=clg
#     @staticmethod
#     def getdata():
#         print('helloo')
#     @classmethod
#     def get_clg(cls):
#         print(cls.Clg)

    

#     def get_full_info(self):
#         print(f"{self.name} is {self.age} old and he is currently pursuing {self.degree} in {self.Clg} adn his pan number is {self.pan} and aadhaar number is {self.aadhaar}")


# student_two=main_info('sri sabarish',16,'239389****','1232 1221 1213')
# student_two.getter("TIPS")
# print(student_two.get_full_info())
# print(student_two.getdata())



# import datetime
# import time 
# import pygame
# def set_alarm(get_alarm_time):
#     print(f"Alarm time is set on : {get_alarm_time}")

#     sound_track="Wooden Train Whistle.mp3"
#     is_running=True

#     while is_running:
#         loop_time=f"{datetime.datetime.now().time().hour:02}:{datetime.datetime.now().time().minute:02}:{datetime.datetime.now().time().second:02}"
#         if str(get_alarm_time)==str(loop_time):
#             print("heyyy")
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_track)
#             pygame.mixer.music.play()
#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)
#             break
#         else:
#             print(loop_time)
        

#         time.sleep(1)

        


# alarm_time_get=input("Set your alarm time (HH:MM:SS) : ")

# set_alarm(alarm_time_get)


import requests
get_url="https://pokeapi.co/api/v2/pokemon/pikachu"

def get_data():
    get_data=requests.get(get_url)
    get_json=get_data.json()
    print(get_json["name"])

get_data()