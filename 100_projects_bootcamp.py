# PROJECT 1
# print("Welcome to Band name generator!")
# enter = input()
# name = input(str("Enter your name:\n"))
# print(f"Welcome in our world {name}!\n")
# city_name = input(str(f"What is your city name:\n"))
# pet_name = input(str(f"\nWhat is your pet name:\n"))
# print(f"\nYour name is {name}, you belong from {city_name} and your pet name is {pet_name}.\nThankyou for visiting!")
# import random

#project 2
# print("Welcome to the Tip calculator!")
# bill = float(input("How much bill you paid?\n"))
# tip = int(input("How much tip would you like to give 10, 12 or 15?\n"))
# total_bill = bill + tip
# bill_split = int(input("How many people to split the bill?\n"))
# per_person_split = round(total_bill / bill_split, 2)
# print("Each person should pay ", per_person_split)

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#ROLLER COASTER PROGRAM
# print("Welcome to roller coaster ride!")
# height = int(input("How tall are you?\n"))
# bill = 0
# if height >= 120:
#     print("hurray!! You can enjoy your roller coaster ride!")
#     age = int(input("How old are you?\n"))
#     if age <= 12:
#        bill += 5
#        # print("your total bill is $5.")
#     elif age <= 18:
#         bill += 10
#         # print("your total bill is $10.")
#     elif age <= 40:
#         bill += 15
#     elif 45 <= age <= 55:
#         bill = 0
#         # print("your total bill is $15.")
#
#     want_photos = str(input("Would you like to take photos during the ride? Type Y if yes and N if no: "))
#     if want_photos == "Y" :   #this if statement will be applied to every age group that's why it's not indented
#         if age < 45:
#            bill += 3
#         else:
#             bill = 0
#     print(f"your final bill is ${bill}")
#
# else:
#     print("sorry, you have to grow taller in order to enjoy the ride!")

# PIZZA ORDER PRACTICE
# print("Welcome to python pizza deliveries!")
# size = input("What size pizza do you want? Type S for small, M for medium, L for large: ")
# want_pepperoni = input("Do you want pepperoni on pizza? Y or N: ")
# want_extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0
# if size == "S":
#    bill  += 15
#    # print("your pizza worth $15")
# elif size == "M":
#     bill += 20
#     # print("your pizza worth $20")
# elif size == "L":
#     bill += 25
#     # print("your pizza worth $25")
# else:
#     print("Please enter a valid size.")
#
#
# if want_pepperoni == "Y":
#     if size == "S":
#        bill += 2
#     else:                 #if size is M or L then
#        bill += 3
# # print(f"your total bill is ${bill}")
#
#
# if want_extra_cheese == "Y":
#     bill += 1
#
# print(f"Your total bill is ${bill}")

#PROJECT 3
print('''
                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                  o
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$$
                               GOLDEN WINNER
''')
print("Welcome to luck wonderland quest!")
print("Where your every choice can bring you either close to death or life full of wealth.\n"
      "so, be cautious about each choices you make.")

print(input("Your last countdown start now...\n press ENTER to continue."))
for i in range(3,0,-1):
    print(i)
quest1 = input('You\'re at a cross-road!\n'
               'Where do you want to go? "left" or "right":\n').lower()  # here we've used single quotation in order to give " to user's choice.
if  quest1 == "left":
    quest2 = input('\ncongratulations! You\'ve come to a lake.\n'
                   'There is an island in the middle of the lake,\n'
                   'would to "wait" for the boat or "swim"?\n').lower()

    if quest2 == "wait":
        quest3 = input('\nYou arrived at the island unharmed.\n'
                       'There are three doors one red, one green, and one blue.\n'
                       'Which door would you like to choose? "Red", "Green" or "Blue?"\n').lower()
        if quest3 == "red":
            print("You entered a room full of beasts. Game over!")
        elif quest3 == "green":
            print("You're thrown in the room full of fire. Game over!")
        elif quest3 == "blue":
            print("congratulations!you won the treasure!")
        else:
            print("Enter a valid choice.")
    elif quest2 == "swim":
        print('You got swallowed by an whale.Game over!')
else:
    print("Game over! You Die.")


# heads and tell using randomisation
# heads_or_tails = random.randint(0,1)
# if heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")

#lists
# create a russian roulette game that makes a random friend to pay everyone's bill on his own
# import random
# friends = ["Arif ","Abdul ","sufiyan ","Arman ","Rizwan"]

#option1
# print(random.choice(friends))

#option2
# random_index = random.randint(0, len(friends)-1)  #i.e. (0,4)
# print(friends[random_index])


#option3
# who_will_pay = random.randint(0,4)
# if who_will_pay == 0:
#     print(friends[0])
# elif who_will_pay == 1:
#     print(friends[1])
# elif who_will_pay == 2:
#     print(friends[2])
# elif who_will_pay == 3:
#     print(friends[3])
# else:
#     print(friends[4])

#PROJECT 4
#ROCK PAPER SCISSOR
# import random

# rock = ("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)


# paper = ("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)

# scissors = ("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)

# output = rock,paper,scissors
# print(f"choose 0 for {rock}, 1 for {paper} or 2 for {scissors}:")
# player = input("player1: ")
# computer_ = random.choice(output)
# print("computer:", computer_)
# if player == "0" and computer_== rock:
#     print("Draw")
# elif player == "1" and computer_ == paper:
#     print("Draw")
# elif player == "2" and computer_ == scissors:
#     print("Draw")
# elif player == "0" and computer_ == scissors:
#     print("You win")
# elif player == "0" and computer_ == paper:
#     print("You lose!")
# elif player == "1" and computer_ == scissors:
#     print("You lose!")
# elif player == "1" and computer_ == rock:
#     print("You win!")
# elif player == "2" and computer_ == paper:
#     print("You win!")
# elif player == "2" and computer_ == rock:
#     print("You lose!")
# else:
#     print("Invalid input")
