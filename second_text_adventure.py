name = input('Enter your name: ')
print(f'Salutations {name}!')
start = input('You are locked in a tiny, enclosed, hot sweltering room. Would you like to [stay] in this room for eternity or [risk life and limb] to escape? ')
if start == 'risk life and limb':
    print('Very well. Let us begin')
    setting = input('Hit return to continue')
    print('To the north is a blank wall with a small disc that resembles an elevator button. An arrow just below it points down.')
    print('To the east is a wall with one door, but the door is blocked closed by boards screwed into the door and wall')
    print('To the south is a wall with one ordinary looking door.')
    print('To the west the wall is completely filled with a black glass window. You can not see out the window.')
    print('In the center of the room is a low table. On the table is a screw driver, a wood burning stove, a match, a hammer, a gas mask, and a knife ')
elif start == 'stay':
    print('Very well. Eternity is a very long time...')
    response = input('Have you changed your mind? ')
    if response == 'yes':
        print('Very well. Let us begin')
        setting = input('Hit return to continue')
        print('To the north is a blank wall with a small disc that resembles an elevator button. An arrow just below it points down.')
        print('To the east is a wall with one door, but the door is blocked closed by boards screwed into the door and wall')
        print('To the south is a wall with one ordinary looking door.')
        print('To the west the wall is completely filled with a black glass window. You can not see out the window.')
        print('In the center of the room is a low table. On the table is a screw driver, a wood burning stove, a match, a hammer, a gas mask, and a knife ')
    else: 
        print('Death by sauna is a dumb way to die. Goodbye.')