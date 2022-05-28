#!/usr/bin/env python3

import time
import sys

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

# Create items
# Closet Items
screen1 = Item("screen", "\nA blank \033[3;31mscreen\033[3;32m. It doesn't seem to be working\n", False)
uniform = Item("uniform", "\nA Military \033[3;31muniform\033[3;32m that is unfamiliar to you.\n", True)
shelf = Item("shelf", "\nAn empty shelf... Well except a little space dust.\n", False)
        
# Control Room Items
guard = Item("guard", "\nThe \033[3;31mguard\033[3;32m looks friendly enough...for now...", False)
weapon = Item("weapon", "\nYou notice the \033[3;31mguard\033[3;32m's \033[3;31mweapon\033[3;32m unattended on the desk.\nThe \033[1;32mHammond Elite Forces Special\033[3;32m, with built in wifi...", True)
electronic_lock = Item("lock", "\nThe lock is in front of a large door to the east.", "False")
id = Item("id", "\nExamining the \033[3;31mid\033[3;32m you notice a code of some kind at the bottom.\nIt reads: '\033[3;33m706c616e6574\033[3;32m'\nPeculiar...", True)

# Airlock Items
spacesuit = Item("spacesuit", "\nThe \033[3;31mspacesuit\033[3;32m looks old, but safe.\n", True)
button = Item("button", "\nThe big red \033[3;31mbutton\033[3;32m has a warning symbol on it.\n", False)
computer = Item("computer" , "\nAn old, dusty \033[3;31mcomputer\033[3;32m sits in the corner.\n", False)

# Kitchen Items
robot = Item("robot", "\nOne of those ancient \033[3;31mrobot\033[3;32m chef things. What are they called again? \nMaybe you could '\033[1;32mtalk\033[0m\033[3;32m' to it.", False)
sign = Item("sign", "\nAn unmissable \033[3;31msign\033[3;32m on the wall reads \033[3;37m'No Hacking Allowed!'\033[3;32m", False)
broucher = Item("broucher", "\nThis must be the \033[3;31mrobot\033[3;32m's menu. Odd choices...\n\n'\033[3;33mHex\033[3;32m soup - 150 credits'\n'\033[3;33mRot13\033[3;32m rissoles - 200 credits'\n'\033[3;33mBase64\033[3;32m burritos - 850 credits'", True)
thermostat = Item("thermostat", "\nA temperature control device i probably shouldn't mess with...\nProbably", False)

# Fridge Items
carcuss = Item("carcuss", "\nA stripped out carcuss of a large, unknown animal swings by chains", False)
mushrooms = Item("mushrooms", "\nThese don't look like the mushrooms that chef \033[3;31mrobot\033[3;32m needed.\nDid he say they needed to be \033[3;33mmagic\033[3;32m?", False)
coin = Item("coin", "\nTarnished and dusty, the \033[3;31mcoin\033[3;32m looks old.\nYou turn it over and notice some characters stamped into it: \033[3;33maGFja2luZwo=\033[3;32m \nIs this another 'ingredient'? ", True)

# Bathroom Items
log = Item("log", "\nHave you ever seen a \033[1;32mCargo Ship\033[0m\033[3;32m stuck sideways in a \033[1;32mCanal\033[0m\033[3;32m?", False)
sink = Item("sink", "\nYou wash your hands for twenty minutes", False)
sign = Item("sign", "\nAn unmissable \033[3;31msign\033[3;32m on the wall reads '\033[1;32m\033[1m\033[4mNo Hacking Allowed!\033[0m\033[3;32m'", False)
ticket = Item("ticket", "\nThere's a \033[3;31mticket\033[3;32m stub seemingly discarded on the floor.\nA single, hand-written word stands out: '\033[3;33mrirel\033[3;32m'.\nWhat the heck does that mean?", True)

# Outside Items
planet = Item("planet", "\nYou're amazed at how close you are to a large, dessert planet", False)
pod = Item("pod", "\nNo idea what i was thinking here", False)
vastness = Item("vastness", "\nThe shear amount of vastness is vast", False)

# Your Ship Items
chair = Item("chair", "\nThe Captains chair", False)


# Create Rooms
# Closet
closet = Room("Closet", "You are in a small, dimly lit room. Probably a \033[1;32mcloset\033[0m\033[3;32m.")
closet.items.append(uniform)
closet.items.append(screen1)
closet.items.append(shelf)

# Control Room
control_room = Room("The Control Room", "You look around. You see an airlock door.")
control_room.items.append(guard)
control_room.items.append(weapon)
control_room.items.append(electronic_lock)
control_room.items.append(id)

# Kitchen
kitchen = Room("Kitchen", "\nYou are in a bright, industrial looking \033[1;32mkitchen\033[0m\033[3;32m.\nThere is a refridgerator to your east and a bathroom to your west.\nSouth is the control room")
kitchen.items.append(robot)
kitchen.items.append(sign)
kitchen.items.append(broucher)
kitchen.items.append(thermostat)

# Fridge
fridge = Room("Fridge", "\nYou're in a large \033[1;32mrefridgerator\033[0m\033[3;32m. Strange meat hangs from the ceiling.\nThere isn't much on the shelves. You shiver in the cold.")
fridge.items.append(carcuss)
fridge.items.append(mushrooms)
fridge.items.append(coin)

# Bathroom
bathroom = Room("Bathroom", "\nYou are in a clean yet foul smelling \033[1;32mbathroom\033[0m\033[3;32m.\nLooking to your left you recoil at the unflushed toilet.\n'I think we found the \033[1;32mCaptains Log\033[0m\033[3;32m', you say to yourself.")
bathroom.items.append(log)
bathroom.items.append(sink)
bathroom.items.append(sign)
bathroom.items.append(ticket)

# Airlock
airlock = Room("The Airlock", "You've entered the \033[1;32mairlock\033[0m\033[3;32m. You peer out a small window at the vastness of space. \nThere is an airlock door to the west.")
airlock.items.append(spacesuit)
airlock.items.append(button)
airlock.items.append(computer)

# Outside
outside = Room("Space", "You are now in Space. Real Space. Not movie Space.")
outside.items.append(planet)
outside.items.append(pod)
outside.items.append(vastness)

# Your Ship
your_ship = Room("Ship", "Your space ship")
your_ship.items.append(chair)


# Create exits
closet.exits["north"]= control_room
control_room.exits["south"] = closet
control_room.exits["north"] = kitchen
kitchen.exits["south"] = control_room
kitchen.exits["east"] = fridge
kitchen.exits["west"] = bathroom
bathroom.exits["east"] = kitchen
fridge.exits['west'] = kitchen
#control_room.exits["east"] = airlock
airlock.exits["west"] = control_room
outside.exits["west"] = airlock
outside.exits["north"] = your_ship
your_ship.exits["south"] = outside

# Create the player
player = Player("The Player", closet)

# Start game

# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
# now call function we defined above
clear()
sleep(1)

# Flag function for test purposes
flag1 = "a"
flag2 = "b"
flag3 = "c"
encflag1 = "aGFja2luZwo="
encflag2 = "rirel"
encflag3 = "706c616e6574"
password = flag1 + flag2 + flag3


# Typing function
def type(text):
  words = text
  for char in words:
    time.sleep(0.03)
    sys.stdout.write(char)
    sys.stdout.flush()

print("\n\033[3;32m**  \033[3;32mRemote connection detected\033[3;32m  **\n")
sleep(2)
print(">>  Firewall: ", end="")
sleep(1)
type("    \033[5m\033[1;32mCIRCUMVENTED\033[0m\033[3;32m  <<\n")
sleep(1)
print(">>  Security System: ", end="")
sleep(1)
type(" \033[5m\033[1;32mBYPASSED\033[0m\033[3;32m  <<\n")
sleep(1)
print(">>  Coffee Machine: ", end="")
sleep(1)
type("     \033[5m\033[1;32mEMPTY\033[0m\033[3;32m  <<\n")

sleep(3)

type("\n\033[3;32m>  You've been compromised... ")
sleep(2)
type("\n>  They found out you were learning to become a \033[1;32mhacker\033[0m\033[3;32m... ")
sleep(2)
type("\n>  You have to get off the ship \033[1;32mimmediately!\033[0m\033[3;32m ")
sleep(2)
type("\n>  I've left \033[3;33mclues\033[3;32m for you to help \033[1;32mhack\033[0m\033[3;32m their system... ")
sleep(1)
type("\n>")
sleep(1)
type("\n>  Remember: '\033[3;31mlook\033[3;32m' carefully, '\033[3;31mget\033[3;32m' cracking and don't forget to take '\033[3;31minv\033[3;32mentory' ")
sleep(2)
type("\n>")
sleep(1)
type("\n>  Good luck, Candidate! ")
sleep(1)
type(" We're all counting on you !\n\n")
sleep(4)


def loading():
    type(">>\033[1;32m  Consciousness Relocation APplication (\033[0m\033[3;32m\033[3;31mC.R.A.P\033[3;32m) \033[1;32mactivating...\033[0m\033[3;32m\n\n")
    sleep(2)
    for i in range(0, 100):
        time.sleep(0.05)
        sys.stdout.write(u"  uploaded...\u001b[1000D" + str(i + 1) + "%  ")
        sys.stdout.flush()
    print
    
loading()

time.sleep(2)
type("\033[3;31m** Activation complete **\033[3;32m")
sleep(4)
clear()
sleep(2)
print("\nYou awaken \033[1;32mdizzy\033[0m\033[3;32m and \033[1;32mdisoriented\033[0m\033[3;32m. Was that a dream?")
sleep(2)


while True:
    #    print(player.location.name)
    print(player.location.description)
    sleep(1)
    print("\nYou see the following: \033[3;31m")
    for item in player.location.items:
        sleep(1)
        print(item.name)
    sleep(1)
    print("\033[3;32mHere are the exits: \033[3;31m")
    sleep(1)
    for exit in player.location.exits:
        print(exit)
 
        
    # Get command
    try:
        # Python 2.7
        command = raw_input("\n\033[3;32m> ")
    except:
        # Python 3.x
        command = input("\n\033[3;32m> ")
        
    words = command.split()
    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun = words[1]
    
    # Examine
    if verb == "examine":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

    # Look
    if verb == "look":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)                

    # Get
    if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                # Check is it movable
                if item.is_movable:
                    print("\nYou take the \033[3;31m{}\033[3;32m".format(item.name))
                    # Remove from room
                    player.location.items.remove(item)
                    # Add to player's inventory
                    player.inventory.append(item)
                
                else:
                    print("\nSorry, you can't move that.\n")

    # Drop
    if verb == "drop":
       for item in player.inventory:
            print("\nYou drop the \033[3;31m{}\033[3;32m.".format(item.name))
            player.inventory.remove(item)
            player.location.items.append(item)
        
    # Inventory
    if verb in ["inv", "inventory"]:
        print("\nYou have the following: \033[3;31m")
        for item in player.inventory:
            print(item.name)
        print(" \033[3;32m")

    # Movement
    if verb in ["north", "south", "east", "west", "space", "down"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            print("\nYou go \033[3;31m{}\033[3;32m and find yourself in a new room.".format(verb))
            sleep(2)
            

    # Room specific code
    # Control Room
    if player.location == control_room:
        if uniform not in player.inventory:
            print("You notice an armed \033[3;31mguard\033[3;32m sitting at a computer terminal.")
            sleep(2)
            print("The \033[3;31mguard\033[3;32m looks up, sees you out of \033[3;31muniform\033[3;32m")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(2)
            print("...pulls out his laser gun and \033[1;32mblasts you in the face!\033[0m\033[3;32m") 
            sleep(3)
            print("\n\n    Game over. \n\n")
            sleep(2)
            sys.exit()
        else:
            sleep(3)
            print("\nYou look to be in some kind of an \033[1;32moffice\033[0m\033[3;32m.")
            print("The armed \033[3;31mguard\033[3;32m at a computer terminal sees your \033[3;31muniform\033[3;32m and smiles.")

    if player.location == control_room:
        if verb == "open" and noun == "airlock":
            if id in player.inventory:
                print("You swipe the \033[3;31mid\033[3;32m and the airlock opens.")
                control_room.exits["east"] = airlock
                
            else:
                print("The airlock won't open. You must need some \033[3;31mid\033[3;32m to open it.")

    if player.location == control_room:
        if verb == "get" and noun == "weapon":
            sleep(2)
            print("He knew you were a spy and booby-trapped the \033[3;31mweapon\033[3;32m.")
            sleep(2)
            print("\nAs you feel a \033[1;32mmillion volts\033[3;32m course through your body,")
            sleep(2)
            print("your last thoughts are...")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(2)
            print("...\033[1;32mDoes anybody smell bacon?\033[3;32m")
            sleep(3)
            print("\n\n\033[3;31mGame Over\033[3;32m\n\n")
            sleep(2)
            sys.exit()


    # Airlock
    #if player.location == airlock:
     #   if "west" in airlock.exits:
      #      del(airlock.exits["west"])
       #     print("The airlock door closes! You are trapped.  There is no lock on this side.")
            
    if player.location == airlock:
        if verb == "press" and noun == "button":
            if spacesuit in player.inventory:
                sleep(2)
                print("\nYou put on the \033[3;31mspacesuit\033[3;32m and push the red \033[3;31mbutton\033[3;32m.")
                sleep(2)
                print("The outer airlock door opens...")
                sleep(2)
                print("\nAs you float gently out into space you are grabbed roughly by an \n\033[1;32mAlien Tentacle\033[0m\033[3;32m.")
                sleep(1)
                print("Numerous other \n\033[1;32mTentacles\033[0m\033[3;32m, all holding \n\033[1;32mprobes\033[0m\033[3;32m, surround you.")
                sleep(2)
                print("\nYou keep repeating to yourself: '\n\033[1;32mButtons aren't toys... Buttons aren't toys...\033[0m\033[3;32m'")
                sleep(2)
                print("\n\nGame Over\n\n")
                sleep(3)
                sys.exit()
            else:
                print("\nThe outer airlock door opens.  You are sucked into the vacuum of space and die immediately.")
                sleep(3)
                print("\n\n\033[3;31mGame Over\033[3;32m\n\n")
                sleep(3)
                sys.exit()

    if player.location == airlock:
        if id in player.inventory and coin in player.inventory and ticket in player.inventory and spacesuit in player.inventory:
            print("\n\033[1;32mYou've succeeded in finding all the clues and unlocking space\033[0m\033[3;32m")
            airlock.exits["space"] = outside

    # Kitchen
    if player.location == kitchen:
        if verb == "talk" and noun == "robot":
            sleep(1)
            print("\nYou hear some crackling, notice some sparks and smell burning...")
            sleep(3)
            print("\n'\033[1;32mBeep-beep boop-boop\033[0m\033[3;32m'")
            sleep(2)
            print("'Welcome to the \033[3;33mCyberChef\033[3;32m 3000'")
            sleep(2)
            print("'Currently OFFLINE due to lack of ingredients' ")
            sleep(2)
            print("'\033[3;33mGoogle\033[3;32m me if you find anything to \033[3;33mbake\033[3;32m'")
            sleep(2)
            print("'We apologise for any...\033[1;32mBeep-Boop-Boooooooo....\033[0m\033[3;32m'") 
            sleep(3)
    

    