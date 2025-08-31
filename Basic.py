
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

day_inp=''

def get_day_func():
    global day_inp
    day_inp=input('Enter the day : ').lower()
    match day_inp:
        case 'monday':
            print('Bad day')
        case 'tuesday':
            print('Almost Gooder one')
        case 'wednesday' | 'thursday':
            print('Best day')
        case 'friday' | 'saturday':
            print('great day')
        case 'sunday':
            print('rest day')
        case _:

            print('Enter valid day')
            return get_day_func()
  
get_day_func()

