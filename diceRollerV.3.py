import random
import os
from time import sleep

def mode(prompt, retries=4, reminder='ERROR: Invalid input. Please try again'):
    while True:
        In = input(prompt + "\n")
        if In in ('l', 'li', 'lis', 'list', '?', 'h', 'he', 'hel', 'help'):
            List(prompt)
        if In in ('e', 'E', 'Exit', 'exit'):
            raise exit
        if In in ('cl', 'Cl', 'Clear', 'clear'):
            clearMode("What would you like to do?")
        if In in ('ch', 'Ch', 'check', 'Check'):
            check()
        if In in ('R', 'r', 'Roll', 'roll'):
            roll()
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def List(prompt):
    print("This is a list of all the commands. a '/' means there is more than one input")
    print("list / List / help / Help")
    print("e / E / Exit / exit")
    mode(prompt)
    
def clear():
    yeet = input('press "enter" to clear screen. ')
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def clearMode(prompt):
    clear()
    mode(prompt)


def checkMath(number):
    addSub = input('adding or subtracting? ex: +1 = 1, -1 = -1, +/- 0 = 0 ')
    addSub = int(addSub)
    multi = input('multiplying? ')
    multi = int(multi)
    div = input('dividing? ')
    div = int(div)
    print('your number is... ')
    print(number + addSub * multi / div)
    clearMode("What would you like to do?")
    
def check():
    diceNumber = input('does the player have advantage? 1 = no, 2 = yes 3 = disadvantage ')
    clear()
    print('the computer has rolled numbers for you.')
    diceNumber = int(diceNumber)
    if diceNumber == 1:
        print('you do not have advantage nor disadvantage.')
        disAd = False
        Ad = False
    elif diceNumber == 2:
        print('you have advantage.')
        disAd = False
        Ad = True
    elif diceNumber == 3:
        print('you have disadvantage')
        diceNumber = diceNumber - 1
        disAd = True
        Ad = False
    number1 = random.randint(1,20)
    number = number1
    if diceNumber == 2:
        number2 = random.randint(1,20)
        if disAd == True:
            if number1 <= number2:
                print("you got a " + str(number1) + " and a " + str(number2) + ". using the " + str(number1))
                number = number1
            elif number2 <= number1:
                print("you got a " + str(number1) + " and a " + str(number2) + ". using the " + str(number2))
                number = number2
            elif number1 == number2:
                print("Both numbers are a " + str(number1))
                number = number1
        elif Ad == True:
            if number1 >= number2:
                print("you got a " + str(number1) + " and a " + str(number2) + ". using the " + str(number1))
                number = number1
            elif number2 >= number1:
                print("you got a " + str(number1) + " and a " + str(number2) + ". using the " + str(number2))
                number = number2
            elif number1 == number2:
                print("Both numbers are a " + str(number1))
                number = number1
        elif Ad == False and disAd == False:
            print("you got a " + number1)
            number = number1
    checkMath(number)

def roll():
    dice_number = input('amount of dice to roll: ')
    dice_number = int(dice_number)
    max_number = input('maximum number you want to roll- ex: a six sided dice = 6: ')
    max_number = int(max_number)
    for x in range(dice_number):
        print random.randint(1,max_number)
    clearMode("What would you like to do?")

mode("What would you like to do?")

# stuff used
# https://docs.python.org/3.6/tutorial/controlflow.html#default-argument-values
# past versions
