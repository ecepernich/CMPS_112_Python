#Elizabeth Cepernich
#eceperni@ucsc.edu // 1316976
#CMPS112 Winter 2016
#Final Project
#3/11/2016


#import other functions and objects
import ascii
import Room
import Fight

#room creation
#Room.Room(roomnumber,items,up,down,left,right)
one=Room.Room(1,[],None,None,None,None)
two=Room.Room(2,['torch'],None,None,one,None)
three=Room.Room(3,[],None,None,two,None)
four=Room.Room(4,["loaf of bread","leg of meat","tankard of beer","glass of wine"],None,None,three,None)
five=Room.Room(5,["sword"],None,None,four,None)
six=Room.Room(6,["dungeon key"],three,None,None,None)
seven=Room.Room(7,[],None,None,six,None)
eight=Room.Room(8,["broken sword"],five,None,seven,None)
nine=Room.Room(9,[],eight,None,None,None)
ten=Room.Room(10,[],None,None,None,nine)
eleven=Room.Room(11,[],None,None,None,ten)
twelve=Room.Room(12,["chest key"],None,None,None,eleven)
thirteen=Room.Room(13,["gold"],None,None,nine,None)
fourteen=Room.Room(14,[],nine,None,None,None)

#extra hallway assignments
one.right=two
two.right=three
three.right=four
four.right=five
three.down=six
six.right=seven
seven.right=eight
five.down=eight
eight.down=nine
nine.left=ten
ten.left=eleven
eleven.left=twelve
nine.down=fourteen
nine.right=thirteen

#remove an item from inventory (for take and drop)
def removeFromInventory(item,inventory):
    newinventory=[]
    for i in range (0,len(inventory)):
        if inventory[i] != item:
            newinventory.append(inventory[i])
    return newinventory

#check if a list contains an item (for moving, take, drop)
def contains(list,item):
    hasItem=False
    for i in range (0,len(list)):
        if list[i] == item:
            hasItem = True
    return hasItem

#prints list of commands - made a function to avoid repetition
def commands():
    print "Commands"
    print "u - go up"
    print "d - go down"
    print "l - go left"
    print "r - go right"
    print "map - check your position"
    print "look - look around the room"
    print "take - take things you find"
    print "drop - drop things from your inventory"
    print "inventory - look at your inventory"
    print "help - see the list of commands"
    print "exit - quit your game"

#start values
current=one
ascii.map(current.roomnumber)
inventory=[]
fight=False
endgame=False
#start game
commands()
choice = input("\nEnter a command: ")
#cycle until exit status
while choice != "exit":
    if (choice == "u"): #move up
        if (current.up is None):
            print "There is no up door"
        else:
            current=current.up
    elif (choice == "d"): #move down
        if (current.down is None):
            print "There is no down door"
        else:
            #locked room checks
            if current.roomnumber==8 and current.down.roomnumber==9:
                #no key
                if contains(inventory,"dungeon key")==False:
                    print "You need a key for this door. Go back and find one."
                    current=current
                #key
                else:
                    #initiate fight - this only happens one time
                    if fight==False:
                        #set up fight from fight file
                        alive=Fight.fight(10,20,inventory)
                        #check if you won the fight - if you did, keep playing
                        if alive==True:
                            fight=True
                            current=current.down
                            ascii.map(current.roomnumber)
                            #if you died, end the game
                        else:
                            endgame=True
                            break
                    else:
                        current=current.down
                        #more locked room checks
            elif current.roomnumber == 9 and current.down.roomnumber==14:
                if contains(inventory,"chest key")==False:
                    print "You need a key for this door. Go back and find one."
                else:
                    current=current.down
                    print "You've falled down a hole and died! Bad luck."
                    endgame=true
                    break
            else:
                current=current.down
    elif (choice == "l"): #move left
        if (current.left is None):
            print "There is no left door"
        else:
            current=current.left
    elif (choice == "r"): #move right
        if (current.right is None):
            print "There is no right door"
        else:
            #locked room check
            if current.roomnumber==9 and current.right.roomnumber==13:
                if contains(inventory,"chest key") == False:
                    print "You need a key for this door. Go back and find one."
                else:
                    current=current.right
                    print "You've found a tresure chest. I wonder what's inside..."
            else:
                current=current.right
    elif (choice == "map"): #look at your current position on a map
        ascii.map(current.roomnumber)
    elif (choice == "look"): #look at the contents of a room
        print current.lookAtRoom()
    elif (choice == "take"): #take something from a room (if the room has items)
        if len(current.items) == 0:
            print "There is nothing to take."
        else:
            print current.items
            item=input("What item do you want to take? ")
            #use check methods to update player inventory and check for victory
            if contains(current.items, item):
                print "You have taken a",item+"."
                inventory.append(item)
                current.items=removeFromInventory(item,current.items)
                if item == "gold":
                    print "You win!"
                    endgame=True
                    break
            else:
                #error message
                print "That item does not exist in this room."
    elif (choice == "drop"): #drop something from your inventory (if your inventory has items)
        if (len(inventory)) == 0:
            print "You don't have anything in your inventory."
        else:
            print inventory
            item=input("What item do you want to drop? ")
            #get user input on drops
            if contains(inventory, item):
                print "You have dropped your "+item+"."
                #add item to room inventory and remove from player inventory
                current.items.append(item)
                inventory=removeFromInventory(item,inventory)
            else:
                #error message
                print "You do not have that item."
    elif (choice == "inventory"): #look at your inventory
        print inventory
    elif (choice == "help"): #print command prompts
        commands()
    else: #base case for command errors
        print "Not a valid command."

    #check if game has been terminated at some point - if not, keep playing. if so, kill them game
    if endgame == False:
        choice = input("\nEnter a command (type help to see command list): ")
    else:
        choice == "exit"
