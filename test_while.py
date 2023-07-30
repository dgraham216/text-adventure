name = input("Enter your name:")
print(f"Salutations {name}!")
userinput = ""
while userinput != "quit":
    print("You are locked in a tiny, enclosed, sweltering room.")
    userinput = input("Would you like to [stay] in this room for eternity or [risk life and limb] to escape?\n>> ")
    if userinput == "risk life and limb":
        print("Very well. Let us begin")
        print("You stand next to a woodburning stove and a backpack")
        print("The north wall has a closed elevator door.  An elevator button next to the door has an engraved arrow pointing down.")
        print("The east wall has one simple wooden door, but the door is blocked by boards screwed horizontally into the door and wall")
        print("The south wall has what looks like a freezer door.")
        print("The west wall is completely filled with a black glass window. You can not see out the window.")
        while userinput == "backpack":
            response = input("Would you like to investigate the [backpack] or the [woodburning stove]?\n>> ")
            if response == "woodburning stove]":
                print("You reach out and touch the black iron stove and realize the sweltering heat in the room is not coming from here.")
                print("It is a black iron stove with a pipe leading up through the ceiing.")
                print("When you open the door you see unlit firewood inside")
            if response == "backpack":
                print("You pick up the backpack and open the flap.")
                print("Inside you find a screwdriver, a match, and a hammer.")
    if userinput == "stay":
        print("Eternity is a very long time. [1/6 Endings Found] Let's begin again! ")

    elif userinput == "quit":
        print("Sorry to see you go, come back soon!")
    else:
        print("Check your typing: [stay] or [risk life and limb]")
