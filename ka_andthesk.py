def welcome():
    print("""As your story continues, we find you and your noble court near that part of Britain which lies near 
the Forests of the Usk. You have been making a royal progression through your land. The weather is 
exceedingly warm. You and your noble court are peacefully
drowsing in the cool shade under the trees. Your company of exalted knights is resting nearby.
With eyes closed, but ears still attentive, you enjoy your knights' cheerful brotherly banter and 
conversation. 
          
The startling noise of thrashing and crashing through the brush of the forest alerts your entire party 
and swiftly brings you to your feet, sword in hand. Through the trees to the west you make out the 
troubling sight of an armored but injured knight in a woeful plight without his shield. He is barely held
upon his broad horse by a fatigued young squire. 

When due care for the wounded knight, his horse, and the squire is completed and a sense of order is 
established once again, you call for the young squire and inquire as to how his knight came to be in such 
a pitiable condition. 

As you and your knights listen with eager ears, the squire's woeful story of his injured 
knight's misfortune unfolds.  Your sense of justice and desire to defend this injured knight's honor 
builds within you with each passing moment. Your knights all turn to you, ready to head your orders 
oncerning this most grievous offense. You must decide!  
          
Will you, King Arthur, yes the most honorable and gentle, yet bravest and most adventurous among all 
kings who ever lived, investigate this mystery? What say you? [Yae] or [Nay]? """)
    option = input("")
    if option == 'Yea':
        dawn()
    elif option == 'Nay':
        really()
    else:
        invalidoption()
        welcome()

def dawn():
    print("""You were so disturbed by the squire's story that you could barely eat.  You were so vexed by the
          injustice done that you would not sleep. You await the chirps of the birds at dawns light, summon
          two squires, don you armor, and mount your beautiful white war-horse.  Your heart beats with joy
          and you ride to the forest. Your court reamins in camp, waves fairwell, and raises wishes of 
          good fortune and safe return. """)
    