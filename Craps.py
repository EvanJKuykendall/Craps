"""
This is a recreation of the popular dice game 'Craps'
This program is intended to showcase my skill with Python
I hope you enjoy!
- Evan Kuykendall, 2019
"""

import sys
import random
from time import sleep


money = 500
intround = 1

def bet():
    while True:
        betinput = input("Place your bet: $")
        sleep(.5)
        try:
            betinput = int(betinput)
        except ValueError:
            print("Please place your bet in only numbers.")
            continue
        else:
           if betinput > money or betinput <= 0:
                print("Uh-oh, it seems you're not allowed to bet ${}.".format(betinput))
                continue
           else:
               break
    return betinput

def secondroll(previous):
    print("*ROLL*")
    rollone = random.randint(1, 6)
    rolltwo = random.randint(1, 6)
    print("{}, {}".format(rollone, rolltwo))
    total = rollone + rolltwo
    sleep(.75)
    if total == 7:
        return False
    elif total == previous:
        return True
    else:
        ans = secondroll(previous)
        return ans

def roll():
    print("Begin round {}! \n\n"
          "*ROLL*".format(intround))
    rollone = random.randint(1, 6)
    rolltwo = random.randint(1, 6)
    print("{}, {}".format(rollone, rolltwo))
    sleep(.75)
    total = rollone + rolltwo
    if total in (2,3,12):
        return False
    elif total in (7,11):
        return True
    else:
        print("Aiming for the {}!".format(total))
        sleep(.80)
        ans = secondroll(total)
        return ans


while money >= 1:
    while intround is 1:
        print("You begin with $500. \n")
        break

    print("Roll 2 dice. If the total is 2, 3, or 12 on the first roll, you lose. \n"
        "If the total is 7 or 11 on the first roll, you win. \n"
        "If you don't roll any of those numbers, you continue to roll under these conditions: \n"
        "Your first roll becomes the winning roll, and if you then roll a 7 before the winning roll, you lose. \n"
        "\nYou have ${} left to spend.".format(money))
    mybet = bet()

    money = money - mybet
    print("You have ${} left to spend.\n".format(money))
    introll = 1

    if roll():
        sleep(.8)
        print("You Win!\n")
        money = money + (2*mybet)
    else:
        print("Crap Out!\n")
    sleep(.8)
    intround = intround + 1
print("You have no more money. :( \nYou lose.")
sys.exit()
#Thank you :)