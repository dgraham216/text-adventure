def intro():
    print()
    print("You stand in the center of a sweltering, tiny room next to a woodburning stove and a backpack")
    print("You slowly turn in place")
    print()
    print("North wall: has a closed elevator door.  An elevator button next to the door has an engraved arrow pointing down.")
    print()
    print("East wall: has one simple wooden door, but the door is blocked by boards screwed horizontally into the door and wall")
    print()
    print("South wall: has what looks like a barn door.")
    print()
    print("West wall: is completely filled with a black glass window. You can not see out the window.")
    print()
    print("Before stepping towards any door or window, you decide to investigate the woodburning stove and the backpack at your feet.")
    print("You reach out and touch the black iron stove and realize the sweltering heat in the room is not coming from here.")
    print("You open the heavy door of the black iron stove and see unlit kindling and firewood piled inside.")
    print("You note a black pipe rising up from the stove to the ceiling")
    print("It is bolted in place")
    print()
    print("Next you investigate the backpack. You pick it up and unbuckle the flap.")
    print("Inside you find a screwdriver, a match, a wrapped piece of your favorite chewing gum, and a hammer.")
    print("Your stomach growls.  You might as well pop in that piece of chewing gum.")
    print()
    print(" After munching for a bit on your gum, you believe you have four obvious options.")
    print("Option #1: Go north to the elevator door.")
    print("Option #2: Go east to the blocked door. Your screwdriver might work on that")
    print("Option #3: Go south to the barn door.")
    print("Option #4: Go west to the black paned window.")
    print("Option #5: unknown at this point, but you hate to limit your options.")
    firstDecision = input("Which option will you chose? (1/2/3/4/5): \n>> ")
    if firstDecision == 1:
        print()
        north()
    elif firstDecision == 2:
        print()
        east()
    elif firstDecision == 3:
        print()
        south()
    elif firstDecision == 4:
        print()
        west()
    elif firstDecision == 5:
        print()
        fire()

def north():
    print()


def east():
    print()


def south():
    print()


def west():
    print()


def fire():
    print()




    














print()
print()
print()
print("          ##############################")
print("          #                            #")
print("          #      Title Here            #")
print("          #                            #")
print("          ##############################")
print()
print()
print()
print()
name = input('Enter your name: ')
print()
print()
print()
print(f'Salutations {name}!')
print("I hope you are game for an adventure!")
print("Close your eyes, and let your trial begin!")
print()
print()
print()
print(f'{name} wake up!')
print("You open your eyes to find that you are enclosed in a tiny room with four walls, a floor, and a ceiling.")
start = input(" It is sweltering in here. Would you like to [stay] here for eternity or [risk life and limb] to escape?\n>> ")
if start == "stay":
    print()
    print("Eternity is a very long time...")
    print()
    response = input("Have you changed your mind? [y/n]: \n>> ")
    if response == 'y':
        print("Very well. Let us begin again.")
        intro()
    elif response == 'n':
        print()
        print("I thought you were open for an adventure? [Ending 1/6 Found]")
