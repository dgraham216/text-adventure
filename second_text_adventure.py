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
    print("Inside you find a screwdriver, a match, a wrapped piece of your favorite minty bubble gum, and a hammer.")
    print("Your stomach growls.  You might as well pop in that piece of chewing gum. This might take awhile.")
    print('You notice the logo on the gum wrapper as you happily chomp away.  It reads "Fresh Breath".')
    intro2()


def intro2():
    print()
    print(" After munching for a bit on your gum, you believe you have four obvious options.")
    print("Option #1: Go north to the elevator door.")
    print("Option #2: Go east to the blocked door. Your screwdriver might work on that")
    print("Option #3: Go south to the barn door.")
    print("Option #4: Go west to the black paned window. Your hammer might break that.")
    print("Option #5: unknown at this point, but you hate to limit your options.")
    firstDecision = input("Which option will you chose? 1/2/3/4/5 \n>> ")
    if firstDecision == '1':
        print()
        north()
    elif firstDecision == '2':
        print()
        east()
    elif firstDecision == '3':
        print()
        south()
    elif firstDecision == '4':
        print()
        west()
    elif firstDecision == '5':
        print()
        fire()




def north():
    print('You walk north. This wall has a closed elevator door. An elevator button next to the door has an engraved arrow pointing down.') 
    action = input('Do you want to push the elevator button? (y/n)\n>> ')
    if action == 'y':
        print('You feel a rumble - then the entire floor beneath you drops and you begin descending 3000ft into a lava filled cavern. [ending 2/6 found]')
        print(' OR do you?')
        print('You remember that you have a single use Rewind Button installed in the middle of your forehead and you smack it - HARD!')
        print('You feel a tug of force from behind, and before you can blink, you find yourself back where you started a few minutes earlier.')
        intro2()
    elif action == 'n':
        intro2()


def east():
    print('You are at a wall with one ordinary door, but it is fastened shut by three boards screwed horizontally into the door and wall')
    remove = input('Would you like to use the screwdriver to unscrew the boards? (y/n)\n>> ')
    if remove == 'y':
        print('The boards fall to the floor.')
        open = input('Would you like to open the door?(y/n)\n>> ') 
        if open == 'y':
            print('When you turn the nob and tug the door open, you find a rocky volcanic wall that is extremely hot. Sadly, is not a way of escape.')
            print('You close the door quickly as the steam and heat eminating from the volcanic wall is too much to bear [Dead End 1/1 Found!]')
            intro2()
        elif open == 'n':
            print("Come on. Take a big breath. What's the worst that could happen? Hehehe... ")
            print('When you turn the knob and tug the door open, you find a rocky volcanic wall that is sizzling hot! Sadly, this is not a way of escape.')
            print('You close the door quickly as the steam and heat eminating from the volcanic wall is too much to bear [Dead End 1/1 Found!]')
            intro2()
    elif remove == 'n':
        print("Really? Sometimes the obvious choice is the right choice. Let's try this again.")
        east()
         
def south():
    print('You walk south to barn style double doors. They are red with white trim. With hope in your heart, you lift the latch, place one hand on each doorpull and swing them towards you.') 
    print('Pulling them open wide, you find a shimmery slimy cobweb covering the doorway.')
    print('The moment your hand reaches out to sweep the web aside, two giant metalic pincers from the giant, sparking spider now framing the doorway jolt your body rigid with electricity.') 
    print('This must be the end...')
    print('OR is it?')
    print('As you shake uncontrollably, and your eyes roll to the back of your head, your left foot slips on a puddle of slime from the web.')
    print('Miraculously, your leg swings up as your body falls down, and you kick the spider back with your rubber toed boots.')
    print('With the pincers no longer zapping you, your head clears, and you have just enough strength to get to your knees, reach out, and slam both doors shut.')
    print('Latch slammed in place!') 
    print("It takes you a few minutes to recover...that was close!")
    intro2()


def west():
    print()
    print('You find yourself facing a large black glass window. You can not see out the window.')
    remove = input('Would you like to use the hammer in your bag to break the window? (y/n)\n>> ')
    if remove == 'y':
        print('The black glass shatters spraying glass everywhere! The window is completely gone. Thick green clouds of poisonous gas begin to fill the room and your lungs [Ending 3/4 Found].')
        print('OR does it?')
        print('As you strain with pain to hold your breath, you remember the bubble gum you have been chewing!')
        print('You have a hunch...')
        print('You somehow blow a surprisingly large lavender bubble with what little air you have left.')
        print('It grows to the size of your face and then pops over your nose and mouth.') 
        print('Your hunch was correct, the bubblegum forms an oxygen releasing mask over your nose and mouth, protecting you from the gas in the room.')
        intro2()
    elif remove == 'n':
        print("Really? You're here. You have a hammer. It should easily break this glass.  Haven't you ever wanted to smash glass?")
        print('Smash the glass!  Smash the glass!  Smash the glass!')
        print("You just can't resist.")   
        print('The black glass shatters spraying glass everywhere! The window is completely gone. Thick green clouds of poisonous gas begin to fill the room and your lungs [Ending 3/4 Found].')
        print('OR does it?')
        print('As you strain with pain to hold your breath, you remember the bubble gum you have been chewing!')
        print("You have a hunch...")
        print('You somehow blow a surprisingly large lavender bubble with what little air you have left.')
        print('It grows to the size of your face and then pops over your nose and mouth.') 
        print("Your hunch was correct...after all, the gum was called 'Fresh Breath'. The bubblegum forms an oxygen releasing mask over your nose and mouth, thus protecting you from the gas in the room.")
        print('After a minute to catch your breath...the green gas disipates. You head back to the center of the room.')
        intro2()



def fire():
    print('You search around the room once more. It seems like an impossible answer, but why else would the match have been in the bag?')
    print('You pull the match out of the bag and open the door to the woodburning stove.')
    print('You strike the match against the iron door and the match sparks to life.')
    print('You light the kindling and within seconds the dry wood piled above it begins to catch.')
    print('Can your body handle any more heat?  Will this be the end? Was there something else you could have tried?')
    print('As your eyes search around the room for any other option, the wood is now fully ablaze.')
    print('The black pipe leading up to the ceiling begins to shake and shimmy, rumble and creek!')
    print('In fact the whole ceiling seems to be rippling, waving, almost fluttering in all the commotion!')
    print('In fact, it seems to be expanding upwards!')
    print('You can not believe your eyes! Your body is slammed to the floor as the entire room seems to lifting up!')
    print('The realization becomes solid in your mind.')
    print('You are in a giant hot air balloon soaring up through the cleaer blue sky!')
    print('You Are Free!!!')
    ending()

def ending():
    print('The wood in the stove quickly burns down to coals, and the balloon gently descends.')
    print('As you sit in a corner, still stunned from your experience, you hear a "ding" from the elevator door.')
    print('The elevator doors slide open...')
    print('You stand up, walk to the door, and step outside')
    print('onto')
    print('the MOON!?!')
    closing()

def closing():
    print("          ##############################")
    print("          #                            #")
    print("          #   Thank You For Playing!   #")
    print("          #                            #")
    print("          ##############################")   

    


    














print()
print()
print()
print("          ##############################")
print("          #                            #")
print("          #       Going Somewhere?     #")
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
elif start == "risk life and limb":
    print()
    intro()
