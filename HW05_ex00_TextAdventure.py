#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

# Home screen and user onboarding
print("\t\t Welcome to the TextAdventure Game, where you navigate the dark "
      "alleys of this command line to find fascinating things or die.")
username = input("Enter your name to get started - ")
print("Hello {}!".format(username))


def infinite_stairway_room(count=0):
    print("You walk through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    # infinite stairs option
    if next == "take stairs":
        print('You take the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(count + 1)
    elif "turn" in next or "back" in next:
        print("Going back to the cthulhu room")
        cthulhu_room()
    else:
        print("Taking you back to start, then, {}".format(username))



def gold_room():
    print("This room is full of gold.  How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear, {}?".format(username))
    bear_moved = False

    while True:
        next = input("> ")

        if "take" in next or "honey" in next:
            dead("The bear looks at you then slaps your face off.")
        elif "taunt" in next and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open" in next or "door" in next and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
            print("Do you want to take the honey or taunt the bear?")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head, {}?".format(username))

    next = input("> ")

    if "flee" in next:
        print("You get lost and stumble upon another door...")
        infinite_stairway_room()

    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def back_room():
    print("You have arrived at the control center of the universe, The Back Room.")
    print("We are the python programmers who control the workings of this universe.")
    print("Welcome {}, do you want to come join us? Say yes or no.".format(username))

    next = input("> ")
    if next.lower() == "yes":
        print("Wise decision!\n")
        import this
        print("\n")
        exit(0)
    elif next.lower() == "no":
        print("Too bad. We have to kill you now.")
        dead("Found out about the back room but refused to join it.")
    else:
        print("Are you trying to break our code? You're going to pay.")
        dead("Tried to break the game.")

def dead(why):
    print("{}\nGood job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("You are in a dark room.")
    print("There is a door to your right and left and maybe another one at the back.")
    print("Which one do you take?")

    next = input("> ")

    if next.lower() == "left":
        bear_room()
    elif next.lower() == "right":
        cthulhu_room()
    elif next.lower() == "back":
        back_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
