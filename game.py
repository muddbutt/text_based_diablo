import random
import sys
import time

illuminationLvl1Found = False

def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.005)
    print('\n')

slowprint('Welcome to Diablo the text based version!\n\n')

def startingPoint():
    slowprint('You wake up in a church.  The only illumination is that from a few candles.\n\n')
    slowprint('They appear to have been lit quite some time ago...\n\n')

    slowprint('What do you do next? : 1) Continue looking around the church?  2) Go outside? ')
    action = input('>> ')
    if action == '1':
        church()
    elif action == '2':
        slowprint('\n\nYou make your way to the nearest exit.\n\n')
        outside()

def church():
    slowprint('\n\nAs you get up and walk around the church you have a look around.')
    slowprint('You notice a back door.')
    slowprint('As you walk to the back-room, you hear a noise from the other side of the door...\n\n')
    
    slowprint('Do you enter the room? 1)    or     2) Continue searching the church for a weapon? ')

    action = input('>> ')
    if action == '1':
        enterBackRoom()
    else:
        searchChurchForWeapon()

def searchChurchForWeapon():
    slowprint('You peer around the church for something resembling a weapon.')
    if illuminationLvl1Found != True:
        slowprint('you come upon a very large and dusty text.')
        slowprint('You are suddenly reminded of the stories of books containing words of great power... ')
        slowprint('You take a step towards the old tome...')
        slowprint('and yet you also remember stories of men delving too greedily into lore which perhaps ought not be meddled with...')

        slowprint('1) Ahh those men who became corrupted were weak-minded fools. What is there to fear from mere words on a page? No book can overpower me...')
        slowprint('2) Perhaps we should continue our search for a more traditional weapon... [leave the text alone]')

        action = input('>> ')
        if action == '1':
            readDustyText()
        elif action == '2':
            continueSearchForWeapon()
    else:
        slowprint('You continue to search the church for anything useful.')
        church()


def readDustyText():

    slowprint('You pick up the heavy book and flip open its worn pages.')
    slowprint('Contained within the pages appear to be chants and spells and other rituals.')
    slowprint('No harm befalls you as you turn the pages.  In fact, you stumble upon a spell which could prove useful.')
    slowprint('You have discovered a minor incantation to illuminate your surroundings! This could come in handy...')
    global illuminationLvl1Found
    illuminationLvl1Found = True
    searchChurchForWeapon()

def continueSearchForWeapon():

    slowprint('You dont want to disturb the book for fear of what might be contained within.')
    slowprint('You continue to browse the nooks and crannies of the church.')
    slowprint('What is this? You see something shiny somewhat hidden in a crevice.')
    slowprint('Do you reach inside to find out what it is? 1) or 2) Decide it is best not reaching into any dark crevices.')
    action = input('>> ')
    if action == '1':
        slowprint('You found a red life potion!')
        church()
    elif action == '2':
        slowprint('You leave the mystery shiny thing be and continue your inspection of the church.')
        church()
        
def enterBackRoom():
    slowprint('\n\nYou slowly open the door and peek inside.')
    slowprint('A few paces away is a figure slouched over a chest.')
    slowprint('It is a priest of the Zakarum, a look of dread painted over his face.\n\n')

    slowprint('Do you approach the priest? 1)')
    slowprint('Speak to the priest? 2)')
    slowprint('Return to the church? 3)')

    action = input('>> ')
    if action == '1':
        approachPriest()
    elif action == '2':
        speakToPriest()
    else:
        returnToChurch()

def outside():

    slowprint('Now that you are outside, you notice the air is quite chill.\n\n')
    slowprint('The moon is full tonight and throws a faint glow across the grounds.\n\n')
    slowprint('Off to the West you see a path leading into the forest.\n')
    slowprint('To the East, a wrought-iron fence surrounding a graveyard.\n\n')
    
    slowprint('Do you head East to the graveyard?  1)  or West into the forest? 2)')

    action = input('\n>> ')
    if action == '1':
        goToGraveyard()
    else:
        slowprint('\nYou decide to head West to see what the forest contains.\n')
          
        slowprint('A web and shadow-covered bridge seperates you from your destination.')
        slowprint('Your footsteps cause the moldy old bridge to creak and groan,')
        slowprint('as you pass over a small creek on your way to the dark wood.\n\n')
        enterForest()

def goToGraveyard():
          
    slowprint('\nYou walk over to the gate which allows entrance to the graveyard.\n')
    slowprint('The hinges squeal their dissapproval as you push open the gate.\n')

    slowprint('Now inside the graveyard, you take stock of your surroundings.')
    slowprint('Off in the distance to the right, a small hill with a gnarled Oak sits atop its peak.')
    slowprint('To the left, a large Crypt silently keeps watch over the smaller tombs and tombstones.')
    slowprint('Besides you, what appears to be freshly disturbed soil next to an empty grave.\n\n')
    slowprint('Do you: cross the graveyard to see what can be seen from the vantage of the hill with the (o)ak?\n')
    slowprint('Walk over to the (c)rypt to see what is inside?\n')
    slowprint('Or more closely inspect the disturbed soil and (e)mpty grave?')
    action = input('>> ')
    while action != 'o' and action != 'c' and action != 'e':
        if action == 'o':
            goToOakTree()
        elif action == 'c':
            goToCrypt()
        elif action == 'e':
            goToEmptyGrave()
        else:
            action = input('\nChoose o, c, or e.\n')

def enterForest():

    slowprint('As you reach half-way across the bridge, suddenly a feeling of icy-terror scuttles up your spine.\n')
          
    slowprint('\n\t\tYou feel like you are being watched...\n\n')

    slowprint('You turn around to see if someone is there.')
    slowprint('But only creeping shadows and leaves rustling in the breeze are there to greet you.\n')
    slowprint('You double your pace and finish crossing the second-half of the bridge.')
    slowprint('Upon reaching the foreign embankment, you find yourself at another crossroads.')
    slowprint('The path to the left appears more well-traveled. The path off to the right appears overgrown and disused.\n')

    slowprint('Do you stick to left where it seems more travelers pass? 1)')
    slowprint('Or see what lies off to the right where the path has been mostly reclaimed by the Woods? 2)')
    slowprint('OR do you listen to your gut telling you, you should seek shelter back at the church immediately. 3)')

    action = input('>> ')
    if action == '1':
          takeBeatenPath()
    elif action == '2':
          takeOvergrownPath()
    elif action == '3':
          goBackAcrossBridge()

def takeBeatenPath():
    slowprint('You head off along the well-worn path which winds its way into the dark woods.')
    slowprint('On either side of you, trees flank the path and provide intermittent cover from the moonlight which seeps through the dense growth overhead.')
    slowprint('The occasional hoot of an owl and the rustle of small animals in the bushes are the only indications that there is life in these woods.')
    slowprint('After continuing for a while along the travelled path, you see a glow off in the distance.')
    slowprint('As you get closer to the light, you just begin to make out that the glow is being given off by a pair of torches on either side of a caravan.')
          
    slowprint('Do you continue approaching the caravan along the path to see who is there? 1)')
    slowprint('Or, do you keep your guard up and step off the path and into the woods to get a closer look from the safety of the shadows? 2)')
    slowprint('Or return the way you came and leave the caravan be. 3)')

    action = input('>> ')
    if action == '1':
        approachCaravan()
    if action == '2':
        approachCaravanFromShadows()
    if action == '3':
        returnToBridge()

def takeOvergrownPath():
    slowprint('You head to the right along where a path once was.  You brush aside bushes and tree branches as you slowly make your way deeper into the forboding Wood. ')
    slowprint('\nAs sight of the bridge dissappears behind you, ahead of you is nothing but more trees, overgrowth and darkness.')
    slowprint('The thought starts to cross your mind that maybe you should turn back.  You have heard stories from travelers that these woods are haunted.')
    slowprint('Men have turned up at inns with nasty-looking wounds that they claim were given to them by creatures of the night. Though you have your doubts about such stories.')
    slowprint('You suspect the injuries were likely caused by disgruntled gambling acquaintences...')
    slowprint('As you continue through the brush, an unpleasant odor noticeably hangs in the air.')
    slowprint('You begin to think that maybe this path was not such a good idea... \n')

    slowprint('Just as you decide to turn around, you notice a clearing far up ahead through the dense trees.')
    slowprint('As you notice the clearing, a single wolf breaks the silence with a mournful howl.')
    slowprint('Another wolf, and another, and another, join the chilling cry. They are not far away at all.')
    slowprint('Realizing the danger of your situation you start jumping and rushing through the overgrowth towards the clearing as quickly as you can.')
    slowprint('As the clearing nears, you notice a wooden hut at the edge of the clearing, with its back touching the wood at the other end of the clearing.')
    slowprint('You take off across the clearing towards the shelter. Once you have reached the middle of the clearing, still sprinting, you look over your shoulder.')
    slowprint('From the darkness of the woods, several four-legged creatures burst from the foliage coming straight for you.')
    slowprint('As you close in on the wooded hut, you can hear the beasts behind you gaining ground rapidly.')
    slowprint('You are within feet of the door and the creatures are close enough that you can hear them.')
    slowprint('You slam into the door, throw it open, and rush inside the dark room just barely getting it shut as the creatures reach the door, slamming their heavy bodies against it.')
    slowprint('After several seconds of clawing, snarling and scratching, the sounds cease.\n\n')

    slowprint('With the immediate danger passed, you look around the space in which you find yourself. No one or nothing is immediately visible which may want to attack you.')
    slowprint('Confident that you can stop supporting the door, you start searching the hut for any clue what this is, where you are, and why no one is home.')
    slowprint('Due to the cobwebs and dust coating everything, the hut appears to have been abandoned some time ago.')
    slowprint('In the middle of the room you can barely make out what appears to be a ladder which leads up into the rafters.')
    slowprint('As you cross the room to get a better look you trip over something on the floor.')
    slowprint('After dusting yourself off, you look at which you stumbled over.  A hatch leading into some kind of cellar perhaps.\n')

    slowprint('What is your next move: 1) Climb the ladder to the attic, 2) Open the hatch and see where it leads, or 3) continue searching the hut.')
    action = input('>> ')
    if action == '1':
          climbHutLadder()
    elif action == '2':
          openHutHatch()
    elif action == '3':
          continueSearchingHut()

def openHutHatch():

    slowprint('You grab the handle of the hatch and lift it open to peer into the pitch darkness below.')
    slowprint('Do you proceed down into the darkness 1) or 2) close the hatch and continue investigating the hut?')
    action = input('>> ')
    if action == '1':
        proceedIntoHutDarkness()
    elif action == '2':
        continueInvestigatingHut()

def climbHutLadder():
    slowprint('You decide to climb the ladder. Once in the attic, you notice a window which faces the clearing which you came from.')
    slowprint('You look out the window and you just catch the wolves returning to the trees, but that is not all.')
    slowprint('You squint and rub your eyes, you think you are seeing things, because it appeared that someone or something was leading the lupine creatures back into the dark woods.')

    slowprint('As you are deciding whether you really did just see someone, or something, it sounds like something knocked over in the room below, where you just were.')
    slowprint('Do you convince yourself you are just hearing things and continue searching the attic 1) or check to see if perhaps you arent so alone in this hut. 2)')
    action = input('>> ')
    if action == '1':
        searchAttic()
    elif action == '2':
        checkoutNoiseBelow()
    
    

def goBackAcrossBridge():
    slowprint('You know that when your gut is telling you to do something, there is probably a good reason.')
    slowprint('You turn around and head back across the creaky, shadowy, bridge, back to the church grounds.')
    slowprint('As you cross the church grounds, you still cant shake the feeling that something is watching you.')
    slowprint('You quicken your pace and head for the side entrance of the church, grab the door handle, and enter.')
    church()

def main():        

    startingPoint()

main()
        
