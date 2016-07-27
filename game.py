import random
import sys
import time

illuminationLvl1Found = False
litTorchFound = False



class characterClass():
    def __init__(self):
        self._lvl = 1
        self._exp = 0
        self._hp = 10
        self._mana = 10
        self._str = 5
        self._int = 5
        self._dex = 5
        self._weapon = ''

        weaponDictionary = {'sword': 2, 'bow': 4}
        
        
    def incExp(self, amt):
        self._exp += amt
        if self._exp >= 10 and self._exp < 20:
            self._lvl = 2
            slowprint('\n\nDing! You have reached level {}'.format(self._lvl))
        elif self._exp >= 20 and self._exp < 40:
            self._lvl = 3
        elif self._exp >= 40 and self._exp < 80:
            self._exp = 4
        elif self._exp >= 80 and self._exp < 140:
            self._exp = 5
        elif self._exp >= 140 and self._exp < 200:
            self._exp = 6
        elif self._exp >= 200 and self._exp < 250:
            self._exp = 7
        elif self._exp >= 250 and self._exp < 300:
            self._exp = 8
        elif self._exp >= 300 and self._exp < 350:
            self._exp = 9
        elif self._exp >= 350 and self._exp < 400:
            self._exp = 10
            
    def incHP(self, amt):
        self._hp += amt
    def incMana(self, amt):
        self._mana += amt
    def incStr(self, amt):
        self._str += amt
    def incInt(self, amt):
        self._int += amt
    def incDex(self, amt):
        self._dex += amt
    def castLvl1Lum(self):
        if self._mana >= 1:
            self._mana -= 1
            return True
        else:
            slowprint('\nNot enough mana!\n')
            return False

class Warrior(characterClass):
    def __init__(self):
        super().__init__()
        self._str = 10











muddbutt = Warrior()




def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.0005)
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
    slowprint('Or 3) see what is outside?')

    action = input('>> ')
    if action == '1':
        enterBackRoom()
    elif action == '2':
        searchChurchForWeapon()
    elif action == '3':
        outside()

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
        slowprint('Seeing the look on the priest\'s face, you back away slowly whilst closing the door...')
        church()

def approachPriest():
    slowprint('As you step forward, the priest speaks to you. "Who are you stranger? What brings you to our light forsaken lands?"')
    slowprint('You dont remember why you are here or how you came to be in this church, but you do know who are.')
    slowprint('How do you respond?')
    slowprint('Do you talk about your endless fight against evil 1) or 2)Do you put the priest in his place? or 3)Do you apologize and retreat back to the church?')
    action = input('>> ')
    if action == '1':
        slowprint('You respond, "I am a fighter of darkness. I go where the path of righteousness takes me."')
        slowprint('The priest lets out a sigh of relief and stands up. "I am glad to hear that. We need more of your kind in these troubled times."')
        slowprint('"If you are truly a defender of man, please take a look inside my chest."')
        
    elif action == '2':
        slowprint('"What business is it to you old man? I go where I please."')
        slowprint('The priest frowns in anger and lets out an exasperated sigh. He stands up and says, "Well whatever your business may be, I have no gold. Only weapons."')
        slowprint('"I cannot in good faith let a man, even one as rude as yourself, go out into the darkness unarmed. Look inside my chest and take what you need."')
        slowprint('You notice him stuff something silver out of sight.')
    else:
        slowprint('"Forgive me. I will be on my way."')
        slowprint('The priest stands up and says, "Wait. You cannot go out there unarmed. It is too dangerous. Heaven knows how you got here in the first place!"')
        slowprint('"Please, take a look inside my chest and take whatever weapon you need." The priest ushers you over and opens his chest. As you walk past him, you notice him stuff something silver in his robes.')
    
    slowprint('Inside are three weapons: A sword, a Bow, and a Staff.')
    slowprint('Which weapon do you choose?')
    slowprint('The Warriors sword 1) The Rogues Bow 2) The Wizards Staff 3) ')
    action = input('>> ')
    if action == '1':
        slowprint('You pick up the warriors sword. It is very old and worn but still retains its sharp edge.')
    elif action == '2':
        slowprint('You pick up the rogues bow. It is plain and made of a brown wood. There are 10 arrows as well.')
    elif action == '3':
        slowprint('You pick up the wizards staff. Ancient runes adorn its surface. You feel the remnant of magic inside.')
    slowprint('"Go forth my child in the light."')
    church()

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
    slowprint('Do you: cross the graveyard to see what can be seen from the vantage of the hill with the (1) oak?\n')
    slowprint('Walk over to the (2)crypt to see what is inside?\n')
    slowprint('Or more closely inspect the disturbed soil and (3)empty grave?')
    action = input('>> ')
    while action != '1' or action != '2' or action != '3':
        if action == '1':
            goToOakTree()
        elif action == '2':
            goToCrypt()
        elif action == '3':
            goToEmptyGrave()
        else:
            action = input('\nChoose 1, 2, or 3.\n')

def goToOakTree():

    action = ''
    
    instance_of_oak_tree = random.randint(1,3)
	
    slowprint('You decide to head over to the Oak Tree to see what you can find.\n')
    slowprint('It is very old with blackened bark and long dead leaves.\n')
    
    if instance_of_oak_tree == 1:
        # zombie
        slowprint('As you reach the base of the tree, you notice a mound of disturbed dirt. On the trunk is a thick liquid congealing on the bark \n')
        slowprint('You touch it with your bare hand. It feels like blood and ichor. Dread washes over you.\n')
        slowprint('A moan comes from behind. "Uuhhhh".\n')
        slowprint('You whip around to see the corpse of a man shambling towards you. Its skin falling off in great chunks and missing an eye. \n')
        slowprint('Since it moves so slowly, you have more time to think over your options. What do you choose?\n')
        slowprint('Stand your ground and fight? (1) Run to the crypt? (2) Run back to the church? (3) Run into the field of graves? (4)\n')
        
        while action != '1' or action != '2' or action != '3' or action != '4':
            action = input('>> ')
        
            if action == '1':
                goToZombieFight()
            elif action == '2':
                goToRunCrypt()
            elif action == '3':
                goToRunChurch()
            elif action == '4': 
                goToFieldGraves()
            else:
                slowprint('If you dont decide quickly the zombie will be upon you!\n')
    elif instance_of_oak_tree == 2:
        #skeleton archer
        slowprint('You climb to the top of the hill with the Oak. You gaze out over the field of graves in all directions.\n')
        slowprint('**wwwhhiiizzzzz**    An arrow flies past your head from the left!\n')
        slowprint('You see an skeleton archer nocking another arrow ready to send at you.\n\n')
        slowprint('Do you charge down the hill towards the archer? (1) , or take cover behind the tree to plan your next move? (2)')
            
            
        while action != '1' or action != '2':
            action = input('>> ')
            if action == '1':
                chargeSkeletalArcher()
            elif action == '2':
                planNextMoveBehindTree()
            else:
                slowprint('You better decide what to do fast, that next arrow might not miss!\n')
            
    elif instance_of_oak_tree == 3:
        #quillRat!!
        slowprint('You notice a burrow dug out at the base of the tree. The dirt around the edge is fresh.\n')
        slowprint('There is a shiny gold coin at the mouth of the burrow. Counting your blessings, you pocket the coin.\n')
        slowprint('As you peer in for more treasure, a screeching sound greets you. Your hair stands on end.\n')
        slowprint('A Quillrat crawls out of the burrow, its spines standing on edge, ready to be thrown at you.\n')
        slowprint('You cannot run away, for fear of getting a quill in your back. You must stand your ground and fight!\n')
        slowprint('("Ah! The thrill of battle!")[1] ("Heaven guide my hand.")[2] ("I never thought I would die to a quillrat.")[3]\n')
        
        action = input('>> ')
        
        goToQuillRatBattle()
       
            
def chargeSkeletalArcher():
	
	archer_accuracy = random.randint(1,10)
	slowprint('You charge down the hill towards the skeletal archer.\n')
	
	if archer_accuracy >= 8:
		# basically the archer has a 30% chance to kill
		slowprint('The archer loosed an arrow with deadly accuracy.  You watch in slow motion as the arrow flies straight at you.\n')
		slowprint('The wind is knocked out of you as the arrow sinks into your chest.\n')
		slowprint('You fall down to your knee and collapse down into the wet grass and dirt.  As the darkness closes in around you, the last thing you \
		see is the two hollows of the skeletal archers empty eye sockets and you could swear his skeletal visage wore a grin ....\n')
		youDied()
	else:
		slowprint("The archer fires another arrow at you but it sails by harmlessly. \n")
		slowprint('As you charge towards the archer you let out a mighty roar and throw the hardest punch possible at the skeletons chest.\n')
		slowprint("The sickening crack of dry brittle bones fills your ears as the skeleton's ribcage crumples beneath your mighty blow.\n")
		slowprint('The archer flies backward and as it falls, whatever unholy magic was giving it unnatural life and holding the bones together vanishes.\n')
	
def goToQuillRatBattle():
	
	quillrat_accuracy = random.randint(1,10)
	slowprint('The Quillrat raises its backside in preperation for firing its quills. \n')
	

	if quillrat_accuracy >= 9:
		slowprint('The quills come firing at great speed and imbed themselves deep in your chest.\n')
		slowprint('You scream in pain and crumble to the ground. Your chest feels wet with your own blood. \n')
		slowprint('The Quillrat screaches in delight and crawls its way towards you, ready to drag you into its burrow for its meal. \n')
		youDied()
	else:
		slowprint('The Quillrat fires a few quills but they fly past, almost grazing your arm. \n')
		slowprint('You smile to yourself and prepare to attack the foolish Quillrat. \n')
		slowprint('You wind up a good kick and kick the beast in the face. It screams in agony and retreats back into its burrow. \n')
		slowprint('Now that the quillrat has retreated, what do you decide to do next? Do you...\n')
		slowprint('Search the tree for more treasure? (1) Go back to the front gate of the graveyard? (2) \n')
		
		while action != '1' or action != '2':
			action = input('>> ')
			
			if action == '1':
				goToSearchTreeTreasure()
			else: 
				goToReturnFrontGraveyard()

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

def approachCaravan():
    global litTorchFound
    slowprint('Upon closer inspection, the Caravan seems abandoned.  That is odd because the torches are lit...')
    slowprint('Do you climb up and have a look inside the carriage 1) or grab one of the torches and head back to the bridge? 2)')
    action = input('>> ')
    if action == '1':
        slowprint('After taking a look inside the Carriage there does not appear to be anything too interesting or useful.')
    elif action == '2':
        litTorchFound = True
        returnToBridge()

def returnToBridge():
    slowprint('You are back at the bridge crossroads.')

    slowprint('Do you go back to the left where the caravan was? 1)')
    slowprint('Or see what lies off to the right where the path has been mostly reclaimed by the Woods? 2)')
    slowprint('OR do you listen to your gut telling you, you should seek shelter back at the church immediately. 3)')

    action = input('>> ')
    if action == '1':
          takeBeatenPath()
    elif action == '2':
          takeOvergrownPath()
    elif action == '3':
          goBackAcrossBridge()

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

def proceedIntoHutDarkness():
    global illuminationLvl1Found
    global litTorchFound
    if illuminationLvl1Found or litTorchFound:
        slowprint('It is really dark, perhaps you should light the way...')
        action = input('1) To use an illumination spell or 2) to use your lit torch.')
        if action == '1':
            if muddbutt.castLvl1Lum():
                slowprint('You cast level 1 illumination! Your palm emits a weak glow.')
        if action == '2':
            slowprint('Your light your torch and proceed forward.')
        slowprint('You can just barely make out the features of an underground passage.')
        slowprint('You follow the corridor as it twists and turns.  It rises up but more often it slopes down.')
        slowprint('After what seems like hours, you at last reach the end of the tunnel.  At the end of the tunnel is a circular tube-like room, just barely wider than a man.')
        slowprint('You are inside a well! Below is the water and on the wall there are rungs leading up and out.')
                
    else:
        slowprint('It is too dark to proceed any further. Perhaps you should return when you have some form of illumination.')

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
def youDied():
	slowprint('You died!\n')
	playAgain = ''
	while playAgain != '1' or playAgain != '2':
		playAgain = input('Would you like to play again? Yes [1]  No [2]\n')
		if playAgain == '1':
			startingPoint()
		else:
			slowprint('Goodbye!\n')
			sys.exit()
def main():        

    startingPoint()

main()
        
