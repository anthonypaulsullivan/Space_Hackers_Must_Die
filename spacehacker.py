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
screen1 = Item("screen", "\nA blank \033[3;31mscreen\033[3;32m. It doesn't seem to be working.\n", False)
uniform = Item("uniform", "\nA Military \033[3;31muniform\033[3;32m that is unfamiliar to you.\n", True)
shelf = Item("shelf", "\nAn empty shelf... Well except for a little space dust.\n", False)
        
# Control Room Items
guard = Item("guard", "\nThe \033[3;31mguard\033[3;32m looks friendly enough...for now...", False)
weapon = Item("weapon", "\nA standard issue \033[3;31mweapon\033[3;32m for this quadrant.\nThe \033[1;32mHammond Elite Forces Special\033[0m\033[3;32m, with built in WiFi...", True)
electronic_lock = Item("lock", "\nThis seems to control access to the airlock. You notice an \033[3;31mid\033[3;32m scanner attached", False)
id = Item("id", "\nExamining the \033[3;31mid\033[3;32m you notice a code of some kind at the bottom.\nIt reads: '\033[3;33m706c616e6574\033[3;32m'\nPeculiar...", True)

# Airlock Items
spacesuit = Item("spacesuit", "\nThe \033[3;31mspacesuit\033[3;32m will protect you from the vastness of space, probably.\n...and has \033[1;32mbuilt in WiFi\033[0m\033[3;32m.\n", True)
button = Item("button", "\nThe large \033[3;31mbutton\033[3;32m on the wall is clearly labelled '\033[1;32mWARNING - OUTER DOOR\033[0m\033[3;32m'.\n", False)
computer = Item("computer" , "\nAhh, the '\033[1;32mBates 2000\033[0m\033[3;32m' \033[3;31mcomputer\033[3;32m. Built to last forever.\n", False)

# Kitchen Items
robot = Item("robot", "\nOne of those ancient \033[3;31mrobot\033[3;32m chef things. What are they called again? \nMaybe you could '\033[1;32mtalk\033[0m\033[3;32m' to it.", False)
sign = Item("sign", "\nAn unmissable \033[3;31msign\033[3;32m on the wall reads \033[3;37m'No Hacking Allowed!'\033[3;32m", False)
broucher = Item("broucher", "\nThis must be the \033[3;31mrobot\033[3;32m's menu. Odd choices...\n\n'\033[3;33mHex\033[3;32m soup - 150 credits'\n'\033[3;33mRot13\033[3;32m rissoles - 200 credits'\n'\033[3;33mBase64\033[3;32m burritos - 850 credits'", True)
thermostat = Item("thermostat", "\nA temperature control device i probably shouldn't mess with...\nProbably", False)

# Fridge Items
carcass = Item("carcass", "\nA stripped out carcass of a large, unknown animal swings by chains. You feel hungry!", False)
mushrooms = Item("mushrooms", "\nThese don't look like the \033[3;31mmushrooms\033[3;32m that chef \033[3;31mrobot\033[3;32m needed.\nDid he say they needed to be \033[3;33mmagic\033[3;32m?", False)
coin = Item("coin", "\nTarnished and dusty, the \033[3;31mcoin\033[3;32m looks old.\nYou turn it over and notice some characters stamped into it: \033[3;33maGFja2luZwo=\033[3;32m \nIs this another 'ingredient'? ", True)

# Bathroom Items
log = Item("log", "\nHave you ever seen a \033[1;32mCargo Ship\033[0m\033[3;32m stuck sideways in a \033[1;32mCanal\033[0m\033[3;32m?", False)
sink = Item("sink", "\nYou wash your hands for twenty minutes", False)
sign = Item("sign", "\nAn unmissable \033[3;31msign\033[3;32m on the wall reads '\033[1;32m\033[1m\033[4mNo Hacking Allowed!\033[0m\033[3;32m'", False)
ticket = Item("ticket", "\nThere's a \033[3;31mticket\033[3;32m stub seemingly discarded on the floor.\nA single, hand-written word stands out: '\033[3;33mrirel\033[3;32m'.\nWhat the heck does that mean?", True)

# Outside Items
planet = Item("planet", "\nYou're amazed at how close you are to a large, desert planet", False)
pod = Item("pod", "\nNo idea what i was thinking here", False)
vastness = Item("vastness", "\nThe shear amount of vastness is vast", False)

# Your Ship Items
chair = Item("chair", "\nThe Captains \033[3;31mchair\033[3;32m ...with built in Wifi.", False)
coffee_machine = Item("coffee", "\nThe \033[3;31mcoffee\033[3;32mmachine sits worthless in the corner.\nMaybe you need to solve something to hack into it.  you ponder the \033[3;33mclues\033[3;32m you've found.", False)
scanner = Item("scanner", "Your trusty '\033[1;32mScan-U-Later\033[0m\033[3;32m'. Now, how do i '\033[1;32muse\033[0m\033[3;32m' it again?", False)
sign2 = Item("sign", "You proudly read in bold letters: \033[1;32m\033[1m\033[4mSpace Hackers Are Awesome!\033[0m\033[3;32m", False)


# Create Rooms
# Closet
closet = Room("Closet", "You are in a small, dimly lit room. Probably a \033[1;32mcloset\033[0m\033[3;32m.")
closet.items.append(uniform)
closet.items.append(screen1)
closet.items.append(shelf)

# Control Room
control_room = Room("The Control Room", "You see an airlock door to the east. There's a kitchen to the \033[3;31mnorth\033[3;32m.")
control_room.items.append(guard)
control_room.items.append(weapon)
control_room.items.append(electronic_lock)
control_room.items.append(id)

# Kitchen
kitchen = Room("Kitchen", "\nYou are in a bright, industrial looking \033[1;32mkitchen\033[0m\033[3;32m.\nThere is a refridgerator to your \033[3;31meast\033[3;32m and a bathroom to your \033[3;31mwest\033[3;32m.\n\033[3;31msouth\033[3;32m is the control room")
kitchen.items.append(robot)
kitchen.items.append(sign)
kitchen.items.append(broucher)
kitchen.items.append(thermostat)

# Fridge
fridge = Room("Fridge", "\nYou're in a large \033[1;32mrefridgerator\033[0m\033[3;32m. Strange meat hangs from the ceiling.\nThere isn't much on the shelves. You shiver in the cold.")
fridge.items.append(carcass)
fridge.items.append(mushrooms)
fridge.items.append(coin)

# Bathroom
bathroom = Room("Bathroom", "\nYou are in a clean yet foul smelling \033[1;32mbathroom\033[0m\033[3;32m.\nLooking to your left you recoil at the unflushed toilet.\n'I think we found the \033[1;32mCaptains Log\033[0m\033[3;32m', you say to yourself.")
bathroom.items.append(log)
bathroom.items.append(sink)
bathroom.items.append(sign)
bathroom.items.append(ticket)

# Airlock
airlock = Room("The Airlock", "You've entered the \033[1;32mairlock\033[0m\033[3;32m. You peer out a small window at the vastness of space. \nThe airlock door is to the \033[3;31mwest\033[3;32m.")
airlock.items.append(spacesuit)
airlock.items.append(button)
airlock.items.append(computer)

# Outside
outside = Room("Space", "You are now in \033[1;32mSpace\033[0m\033[3;32m. Real \033[1;32mSpace\033[0m\033[3;32m. Not movie \033[1;32mSpace\033[0m\033[3;32m.\nYou see your spaceship to the \033[3;31mnorth\033[3;32m. The airlock is to the \033[3;31mwest\033[3;32m.")
outside.items.append(planet)
outside.items.append(pod)
outside.items.append(vastness)

# Your Ship
your_ship = Room("Ship", "The sleek, modern \033[1;32mspacecraft\033[0m\033[3;32m you call home. A real \033[1;32mbeauty\033[0m\033[3;32m!")
your_ship.items.append(chair)
your_ship.items.append(scanner)
your_ship.items.append(coffee_machine)
your_ship.items.append(sign2)


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
#flag1 = "a"
#flag2 = "b"
#flag3 = "c"
#encflag1 = "aGFja2luZwo="
#encflag2 = "rirel"
#encflag3 = "706c616e6574"
#password = flag1 + flag2 + flag3


# Typing function
def type(text):
  words = text
  for char in words:
    time.sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

print("\n\033[3;32m**  \033[1;32mRemote connection detected\033[0m  \033[3;32m  **\n")
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

sleep(2)

type("\n\033[3;32m>  You've been compromised... ")
sleep(1)
type("\n>  They found out you were learning to become a \033[1;32mhacker\033[0m\033[3;32m... ")
sleep(1)
type("\n>  You have to get off the ship \033[1;32mimmediately!\033[0m\033[3;32m ")
sleep(1)
type("\n>  I've left \033[3;33mclues\033[3;32m for you to help \033[1;32mhack\033[0m\033[3;32m their system... ")
sleep(1)
type("\n>")
sleep(1)
type("\n>  Remember: '\033[3;31mlook\033[3;32m' carefully, '\033[3;31mget\033[3;32m' cracking and don't forget to take '\033[3;31minv\033[3;32mentory' ")
sleep(2)
type("\n>")
sleep(1)
type("\n>  Good luck, Candidate! ")
sleep(0.5)
type(" We're all counting on you !\n\n")
sleep(2)
type(">>\033[1;32m  Consciousness Relocation APplication (\033[0m\033[3;32m\033[3;31mC.R.A.P\033[3;32m) \033[1;32mactivating...\033[0m\033[3;32m\n\n")

def loading():
    for i in range(0, 100):
        time.sleep(0.05)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%  ")
        sys.stdout.flush()
    print
    
loading()

time.sleep(2)
type("\033[3;31m** Activation complete **\033[3;32m")
sleep(3)
clear()
sleep(1)
print("\nYou awaken \033[1;32mdizzy\033[0m\033[3;32m and \033[1;32mdisoriented\033[0m\033[3;32m. Was that a dream?")
sleep(1)

def success():
    clear()
    sleep(1)
    print("\n>>  Firewall: ", end="")
    sleep(1)
    type("      \033[5m\033[1;32mOPERATIONAL\033[0m\033[3;32m   <<\n")
    sleep(1)
    print(">>  Security System: ", end="")
    sleep(1)
    type("  \033[5m\033[1;32mACTIVATED\033[0m\033[3;32m  <<\n")
    sleep(1)
    print(">>  Coffee Machine: ", end="")
    sleep(1)
    type("     \033[5m\033[1;32mBREWING\033[0m\033[3;32m  <<\n")
    sleep(2)
    type("\n\033[3;32m>  Congratulations Candidate... ")
    sleep(1)
    type("\n>  You have successfully patched the system, escaped the ship \n>  and found the path to become a \033[1;32mhacker\033[0m\033[3;32m... ")
    sleep(2)
    print("\n\nAs you power on the ship your screens come to life. ")
    sleep(1)
    print("An incredibly bright light blinds you...\n\n")
    sleep(2)
    type(">>\033[1;32m  Consciousness Relocation APplication (\033[0m\033[3;32m\033[3;31mC.R.A.P\033[3;32m) \033[1;32mactivating...\033[0m\033[3;32m\n\n")
    loading()
    time.sleep(2)
    type("\033[3;31m** Activation complete **\033[3;32m")
    sleep(3)
    clear()
    sleep(2)
    print("\nYou awaken \033[1;32mdisoriented\033[0m\033[3;32m and \033[1;32mdizzy\033[0m\033[3;32m, inside a different closet...")
    sleep(3)
    print("\n\n\033[1;32mGAME OVER\033[3;32m\n\n")
    sleep(3)
    sys.exit()

while True:
    #    print(player.location.name)
    print(player.location.description)
    sleep(1)
    print("\nYou see the following: \033[3;31m")
    for item in player.location.items:
        sleep(0.3)
        print(item.name)
    sleep(1)
    print("\033[3;32mHere are the exits: \033[3;31m")
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
    if verb in ["look", "search", "check"]:
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)                

    # Get
    if verb in ["get", "take", "grab"]:
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
    if verb in ["drop", "remove"]:
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
        sleep(1)

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
        if id in player.inventory:
            print("You \033[1;32mswipe\033[0m\033[3;32m the \033[3;31mid\033[3;32m and the \033[1;32mairlock opens\033[0m\033[3;32m to the \033[3;31meast\033[3;32m.")
            control_room.exits["east"] = airlock
         
    if player.location == control_room:
        if verb in ["get", "take", "grab"] and noun == "weapon":
            sleep(2)
            print("He knew you were a \033[1;32mspy\033[0m\033[3;32m and booby-trapped the \033[3;31mweapon\033[3;32m.")
            sleep(2)
            print("\nAs you feel a \033[1;32mmillion volts\033[0m\033[3;32m course through your body,")
            sleep(2)
            print("your last thoughts are ")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(2)
            print("...\033[1;32mDoes anybody smell bacon?\033[0m\033[3;32m")
            sleep(3)
            print("\n\n\033[3;32mGame Over\033[3;32m\n\n")
            sleep(2)
            sys.exit()


    # Airlock
    #if player.location == airlock:
     #   if "west" in airlock.exits:
      #      del(airlock.exits["west"])
       #     print("The airlock door closes! You are trapped.  There is no lock on this side.")
            
    if player.location == airlock:
        if verb in ["press", "push"] and noun == "button":
            if spacesuit in player.inventory:
                sleep(1)
                print("\nYou quickly put on the \033[3;31mspacesuit\033[3;32m and push the large \033[3;31mbutton\033[3;32m.")
                sleep(1)
                print("You hear a \033[1;32mwhooshing\033[0m\033[3;32m sound as the outer airlock door opens...")
                sleep(2)
                print("\nAs you float gently out into space you are grabbed \nroughly by an \033[1;32mAlien Tentacle\033[0m\033[3;32m.")
                sleep(2)
                print("Numerous other \033[1;32mTentacles\033[0m\033[3;32m, all holding \033[1;32mprobes\033[0m\033[3;32m, surround you.")
                sleep(2)
                print("\nYou keep repeating to yourself: \n'\033[1;32mButtons aren't toys... Buttons aren't toys...\033[0m\033[3;32m'")
                sleep(3)
                print("\n\nGame Over\n\n")
                sleep(2)
                sys.exit()
            else:
                sleep(2)
                print("\nThe outer airlock door opens with a whoosh and you are forcefully sucked into the vastness of space.")
                sleep(2)
                print("\nAs your body freezes you look back at the \033[3;31mspacesuit\033[3;32m hanging on the wall.")
                sleep(3)
                print("\n\n\033[3;31mGame Over\033[3;32m\n\n")
                sleep(3)
                sys.exit()

    if player.location == airlock:
        if id in player.inventory and coin in player.inventory and ticket in player.inventory and spacesuit in player.inventory:
            print("\n\033[1;32mYou've succeeded in finding all the clues and unlocking space\033[0m\033[3;32m\n")
            airlock.exits["east"] = outside

    # Kitchen
    if player.location == kitchen:
        if verb in ["talk", "chat", "speak"] and noun == "robot":
            sleep(1)
            print("\nYou hear some crackling, notice some sparks and smell burning...")
            sleep(2)
            print("\n'\033[1;32mBeep-beep boop-boop\033[0m\033[3;32m'")
            sleep(1)
            print("'Welcome to the \033[3;33mCyberChef\033[3;32m 3000'")
            sleep(1)
            print("'Currently OFFLINE due to lack of ingredients' ")
            sleep(1)
            print("'\033[3;33mGoogle\033[3;32m me if you find anything to \033[3;33mbake\033[3;32m'")
            sleep(1)
            print("'We apologise for any...\033[1;32mBeep-Boop-Boooooooo....\033[0m\033[3;32m'") 
            sleep(2)
            if id in player.inventory and coin in player.inventory and ticket in player.inventory:
                print("\n\033[1;32mThey fixed the airlock!\033[0m\033[3;32m\nYou should be able to escape if you have a \033[3;31mspacesuit\033[0m\033[3;32m.\nJust remember: \n\033[1;32mButtons aren't toys!\033[0m\033[3;32m")
                
    # Your Ship
    if player.location == your_ship:
        if verb in ["use", "operate", "push", "press", "feed"] and noun == "scanner":
            sleep(2)
            print("\nThe '\033[1;32mScan-U-Later\033[0m\033[3;32m' humms to life.")
            sleep(2)
            print("\n'\033[1;32mBeep-beep boop-boop...\033[0m\033[3;32m'")            
            sleep(1)
            print("'Analyzing all \033[3;33mclues\033[3;32m found...'\n")
            sleep(1)
            print("      Analyzing coin - \033[3;33maGFja2luZwo=\033[3;32m  ", end="")
            loading()
            print("\n\033[5m\033[1;32mBase64 detected !\033[0m\033[3;32m\n")
            sleep(1)
            print("      Analyzing id   - \033[3;33m706c616e6574\033[3;32m  ", end="")
            loading()
            print("\n\033[5m\033[1;32mHex detected !\033[0m\033[3;32m\n")
            sleep(1)
            print("      Analyzing ticket - \033[3;33mrirel\033[3;32m  ", end="")
            loading()
            print("\n\033[5m\033[1;32mRot13 detected !\033[0m\033[3;32m\n")
            sleep(3)
            print("\n\n\033[3;32m**  \033[1;32mRemote connection detected\033[0m  \033[3;32m  **\n")
            sleep(3)
            success()

