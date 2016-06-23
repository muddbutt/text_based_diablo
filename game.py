print('Welcome to Diablo the text based version!\n\n')

def church():
    print('As you get up and walk around the church you have a look around.  You notice a back door.  As you walk to the back room, you hear a noise from the other side of the door.')
    response = input('Do you enter the room? 1)    or     2) Continue searching the church for a weapon?')
    if response == 1:
        print('You slowly open the door and peek inside.  A few paces away is a figure slouched over a chest.')
    else:
        print('Peering around the church for something resembling a weapon, you come upon a very large and dusty text.')


def outside():
    print('You make your way to the nearest exit.')
    print('Now that you are outside, you notice the air outside is quite chill.  The moon is full tonight and throws a faint glow across the grounds.  Off to the west you see a path leading into the forest.  To the east, a wrought-iron fence surrounding a graveyard.')
    response = int(input('Do you head East to the graveyard?  1)  or West into the forest? 2)'))
    if response == 1:
        print('You walk over to the gate which allows entrance to the graveyard.  You push it open and the hinges squeal sharply.')
    else:
        print('Your footsteps cause the moldy old bridge to creak and groan as you pass over a small creek on your way to the dark wood.')
        

userInput = 'continue'

while userInput != 'escape':

    print('You wake up in a church.  The only illumination is that from a few candles.\n\n  They appear to have been lit quite some time ago.')

    userInput = input('What do you do next? : 1) Continue looking around the church?  2) Go outside?')

    if userInput != 'escape':
        if userInput == '1':
            church()
        else:
            outside()
