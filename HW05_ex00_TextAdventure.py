#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

user_name = input("What is your name? ")

def infinite_stairway_room(count=0):
    print("{}, you walk through the door to see a dimly lit hallway.".format(user_name))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('You take the stairs, {}'.format(user_name))
        if (count > 0):
            print("but, {}, you're not happy about it".format(user_name))
        infinite_stairway_room(count + 1)
    # get fit option
    if next == "stop":
        print("Ah, you better get fit before you play this game again!")
        exit(0)


def gold_room():
    print("This room is full of gold.  How much do you take, {}?".format(user_name))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, {}!".format(user_name))
        infinite_stairway_room()
    else:
        dead("{}, you greedy goose!".format(user_name))


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("{}, how are you going to move the bear?".format(user_name))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at you {} then slaps your face off.".format(user_name))
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. {}, you can go through"
                " it now.".format(user_name))
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" or next == "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here {} you see the great evil Cthulhu.".format(user_name))
    print("He, it, whatever stares at you and you go insane, {}.".format(user_name))
    print("{}, do you flee for your life or eat your head?".format(user_name))

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    
    print("{}, you are in a dark room.".format(user_name))
    print("There is a door to your right and left.")
    print("Which one do you take, {}?".format(user_name))

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("{}, you stumble around the room until you starve.".format(user_name))

if __name__ == '__main__':
    main()
