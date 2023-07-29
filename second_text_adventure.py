name = input('Enter your name: ')
print(f'Salutations {name}!')
start = input('You are locked in a tiny, enclosed, steamy, sweltering room. Would you like to [stay] in this room for eternity or [risk life and limb] to escape? ')
if start == 'risk life and limb':
    print('Very well. Let us begin')
    print('To the north is a blank wall with a small disc that resembles an elevator button. An arrow just below it points down.')
    print('To the east is a wall with one door, but the door is blocked by boards screwed into the door and wall')
    print('To the south is a wall with one ordinary looking door.')
    print('To the west the wall is completely filled with a black glass window. You can not see out the window.')
    print('In the center of the room is a woodburning stove and a backpack containing a screwdriver, a match, and a hammer,')
    response = input('Would you like to [go] a certain direction or [pick up bag]')
    if response == 'go north':
        print('You are at a blank wall with a small disc inserted in the center of the wall. It resembles an elevator button. An arrow just below it points down.') 
        action = input('Do you want to [push] it? ')
        if action == 'push':
            print('The entire floor drops and you begin descending 3000ft into a lava filled cavern. [ending 2/6 found]')
            print(' OR do you?')
            print('You remember that you have a single use Rewind Button installed in the middle of your forehead and you smack it - hard!')
            print('You find yourself back in the tiny, steamy, sweltering room near the woodburning stove as if nothing ever happened.')
    if response == 'pick up bag':
        print('You put the backpack on your back. ')
    if response == 'go east':
        print(' You are at a wall with one door, but the door is blocked by boards screwed into the door and wall')
        remove = input('Would you like to use the screwdriver to [unscrew the boards]?')
        if remove == 'unscrew the boards':
            print('The boards fall to the floor.')
            open = input('Would you like to [open the door]? ') 
            if open == 'open the door':
                print('When you turn the nob and tug the door open, you find a rocky volcanic wall that is extremely hot. You can not escape.')
                print('You close the door quickly as the steam and heat eminating from the vocanic wall is too much to bear [Dead End 1/1 Found!]')
    if response == 'go south':
        print('You walk south to the ordinary looking door. With hope in your heart, you turn the knob and pull.')
        print('You find a shimmery slimy bubble covering the doorway.')
        print('The moment your finger reaches out, the bubble bursts, slime flies, and you are immediately zapped by giant electrical pincers of a metalic spider now framing the doorway. [Ending 2/4]')
        print('OR is it.')
        print('As you shake uncontrollably, and your eyes roll to the back of your head, your foot slips on some of the slime and you miraculously kick the spider back.')
        print('Your head clears and you have just enough energy to roll to the side and slam the door shut ')
        print('You find yourself back in the tiny, steamy, sweltering room near the woodburning stove as if nothing ever happened')
    if response == 'go west':
        print('You find yourself facing a large black glass window. You can ot see out the window.')
        remove = input('Would you like to [use the hammer] in your bag to break the window? ')
        if remove == 'use the hammer':
            print('The black glass shatters and thick, green, poisonous gas begins to fill the room and your lungs [Ending 3/4 Found].')
            print('OR does it?')
            print('As you strain with might to hold your breath, you remember the bubble gum you have been chewing since this morning.')
            print('You quickly blow a large lavender bubble which pops and forms an oxygen releasing mask over your nose and mouth.')
            print('You find yourself back in the tiny, steamy, sweltering room near the woodburning stove as if nothing ever happened')
    if response == ''       
elif start == 'stay':
    print('Very well. Eternity is a very long time...')
    response = input('Have you changed your mind? ')
    if response == 'yes':
        print('Very well. Let us begin again.')
        setting = input('Hit return to continue')
        print('To the north is a blank wall with a small disc inserted in center of the wall. It resembles an elevator button. An arrow just below it points down.')
        print('To the east is a wall with one door, but the door is blocked closed by boards screwed into the door and wall')
        print('To the south is a wall with one ordinary looking door.')
        print('To the west the wall is completely filled with a black glass window. You can not see out the window.')
        print('In the center of the room is a low table. On the table is a screw driver, a wood burning stove, a match, a hammer, a gas mask, and a knife ')
    else: 
        print('Death by sauna [ending 1/6 found] was a dumb way to die. Goodbye.')
        quit()
    