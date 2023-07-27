name = input('Enter your name! ')
print(f'Greetings {name}! Welcome to adventure!')
start = input('Would you rather play or perish? ')
if start == 'play':
    print("Hmmm okay, if you'd like to play it safe... ")
start = input("Would you like to change your mind? Y or N ")
if start == 'Y':
    print("Mwahahaha! You're mind is easily manipulated! ")
if start == 'N':
    print("Okay, safe it is...")