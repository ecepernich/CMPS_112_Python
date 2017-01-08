#Elizabeth Cepernich
#eceperni@ucsc.edu // 1316976
#CMPS112 Winter 2016
#Final Project
#3/11/2016

import random
#prints HP bars for player and monster (used in fightStance)
def healthString(health,maxHealth):
    healthBar=""
    #iterates over max health to get full bar
    current=maxHealth
    while current>0:
        #print @ to indicate a health point
        if (health>0):
            healthBar=healthBar+"@"
            health=health-1
            current=current-1
            #print _ to indicate health lost
        else:
            healthBar=healthBar+"_"
            health=health-1
            current=current-1
    return healthBar
#ascii printing method that shows player and monster health bars (uses healthString)
def fightStance(monsterHealth, playerHealth):
    print"                          FIGHT!"
    print"          |\\|\\                              ___"
    print"         /  @V@\\___                   ^    /.v.\\ "
    print"         \\____vvvv/                   |    \\_^_/  "
    print"         |\\    |===K        VS        |___//|  \\\\    "
    print"     /\\  | \\==K|                      @---  |__||"
    print"     \\ \\_|  /\\  \\|\\                         / ^`@"
    print"      \\___\\/__\\__\\_\\\\___                 __/_/ \\_\\__"
    print
    print"      HP:",healthString(monsterHealth/2,10),"                 HP:",healthString(playerHealth,10)
#calculates attack damage based on weapon multiplier and drunkenness
#better weapons have higher multipliers, and drunkenness increases your chance of missing
def attack(monsterHealth,multiplier,drunk):
    chance=0
    #calculate chance of failing your attack - higher if drunk variable is true
    if drunk == True:
        chance=random.randrange(1, 12)%4
    else:
        chance=random.randrange(1, 14)%7
    if chance == 2:
        print "You stumbled and missed! The monster takes no damage."
    else:
        #do damage to monster using multiplier calculated from inventory
        monsterHealth=monsterHealth-multiplier
        print "You attack the monster and do",multiplier,"HP of damage!"
    return monsterHealth
#calculates player attack damage based on dodging and drunkenness
#drunkenness causes dodges to fail and hurt more than sober attacks
def attacked(playerHealth,drunk,dodge):
    #50% chance that monster attacks back
    chance=random.randrange(0, 10)%2
    #if you are drunk and try to dodge an attack, you fail and get hurt
    if chance == 0 and drunk == True and dodge == True:
        print "You stumble and get attacked by the monster and lose 3 HP!"
        playerHealth=playerHealth-3
        #if you are not drunk, your dodge is successful and you gain back 1HP (to make the dodge worth doing)
    elif chance == 0 and drunk == False and dodge == True:
        print "The monster lunges at you, but you roll out of the way!"
        playerHealth=playerHealth+1
        if playerHealth > 10:
            playerHealth = 10
        print "You manage to gain back 1 HP by avoiding the monster."
        #if you dodge and there's no attack, you get 1HP back while drunk for being funny
    elif chance == 1 and drunk == True and dodge == True:
        playerHealth=playerHealth+1
        if playerHealth > 10:
            playerHealth = 10
        print "You try to anticipate the monster's next move. It doesn't lunge for you, but you roll away anyway."
        print "You get 1 HP back for not being attacked."
        #if you get attacked and don't dodge, you lose more health
    elif chance == 0 and dodge == False:
        print "You failed to dodge and the monster attacks you! You lose 2 HP."
        playerHealth=playerHealth-2
    return playerHealth
#player uses a food item to heal themself if their HP get low (used in fight)
#player gains back given amount of HP, or is returned to max health if HP gained back is greater than 10
def use(item,inventory,playerHealth):
    haveItem=False
    for i in range (0,len(inventory)):
        if inventory[i] == item:
            haveItem=True
    if haveItem==True:
        #loaf of bread returns 3HP (or to max health)
        if item == "loaf of bread":
            playerHealth=playerHealth+3
            if playerHealth > 10:
                playerHealth = 10
                print "You restore yourself to full HP!"
            else:
                print "You eat your loaf of bread and gain back 3 HP!"
                #glass of wine return 2HP (or to max health) but makes player drunk
        elif item == "glass of wine":
            playerHealth=playerHealth+2
            if playerHealth > 10:
                playerHealth = 10
                print "You restore yourself to full HP!"
            else:
                print "You drink a glass of wine and gain back 2 HP!"
            print "You are now drunk. Be careful."
            #leg of meat returns 4 HP (or to max health)
        elif item == "leg of meat":
            playerHealth=playerHealth+4
            if playerHealth > 10:
                playerHealth = 10
                print "You restore yourself to full HP!"
            else:
                print "You eat a leg of meat and gain back 4 HP!"
          #tankard of beer return 2HP (or to max health) but makes player drunk
        elif item == "tankard of beer":
            playerHealth=playerHealth+2
            if playerHealth > 10:
                playerHealth = 10
                print "You restore yourself to full HP!"
            else:
                print "You drink a tankard of beer and gain back 2 HP!"
            print "You are now drunk. Be careful."
        else:
            #error message
            print "You cannot use that item."
    else:
        #error message
        print "You do not have that item."
    return playerHealth
#takes an item out of a given inventory
def removeFromInventory(item,inventory):
    newinventory=[] #new inventory to avoid blank spaces
    #cycle through old inventory and add non-used items to new inventory
    for i in range (0,len(inventory)):
        if inventory[i] != item:
            newinventory.append(inventory[i])
    return newinventory #return new inventory without used item
#based on inventory, finds the best weapon and gives the player a multiplier based on that weapon
def calculateMultiplier(inventory):
    multiplier=1
    hasBrokenSword=False
    hasSword=False
    noSword=False
    for i in range (0,len(inventory)):
        if inventory[i]=="sword":
            hasSword=True
        if inventory[i]=="broken sword":
            hasBrokenSword=True

    if hasSword==False and hasBrokenSword==False:
        noSword = True
    if hasSword == True:
        multiplier = 3
    elif hasBrokenSword == True:
        multiplier = 2
    else:
        multiplier = 1
    return multiplier
#fight game - uses attack, dodge, use, removeFromInventory
def fight(playerHealth,monsterHealth,inventory):
    #initialize vars
    victory=False
    drunk=False
    multiplier=calculateMultiplier(inventory)
    while monsterHealth > 0 and playerHealth > 0:
        fightStance(monsterHealth,playerHealth)
        print "Your inventory:",inventory
        #reset dodge input to false every round
        dodge = False
        choice = input("What do you want to do? ('attack', 'dodge', or 'use' an item?) ")
        #run both attack and attacked methods as earlier defined
        if choice == "attack":
            monsterHealth=attack(monsterHealth,multiplier,drunk)
            playerHealth=attacked(playerHealth,drunk,dodge)
            #set dodge to true and run attacked method
        elif choice == "dodge":
            dodge = True
            playerHealth=attacked(playerHealth,drunk,dodge)
            #use the use method to gain back hp - monster doesn't attack
        elif choice == "use":
            item=input("What item do you want to use? ")
            if item=="glass of wine" or item=="tankard of beer":
                drunk=True
            playerHealth=use(item,inventory,playerHealth)
            inventory=removeFromInventory(item,inventory)
        else:
            #error message
            print "Not a valid command."
    #end game messages
    if playerHealth < 1:
        print "You died."
        victory=False
    else:
        print "You beat the monster!"
        victory=True
    return victory