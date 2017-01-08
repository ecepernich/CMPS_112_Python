#Elizabeth Cepernich
#eceperni@ucsc.edu // 1316976
#CMPS112 Winter 2016
#Final Project
#3/11/2016


#using quadrupally linked lists - this is the node
class Room(object):

#initialize node with a room number, an inventory, and its four linking nodes (which may be None)
    def __init__(self, roomnumber, items, up, down, left, right):
        self.roomnumber = roomnumber
        self.items = items
        self.up = up
        self.down = down
        self.left = left
        self.right = right

#show room - for testing purposes
    def showRoom(room):
        if room is None:
            print(None)
        else:
            if room.up is None:
                print
            else:
                print "up is",room.up.roomnumber
            if room.down is None:
                print
            else:
                print "down is",room.down.roomnumber
            if room.left is None:
                print
            else:
                print "left is",room.left.roomnumber
            if room.right is None:
                print
            else:
                print "right is",room.right.roomnumber

#shows a room's inventory - the cases are just for grammatical and aesthetic purposes but it reads nicely
    def lookAtRoom(room):
        result=""
        if (room) is None:
            result="This room is empty."
        else:
            contents=room.items
            if len(contents)==0:
                result="This room is empty."
            elif len(contents)==1:
                item=contents[0]
                result="This room contains a "+item+"."
            elif len(contents)==2:
                item1=contents[0]
                item2=contents[1]
                result="This room contains a " +item1+ " and a "+item2+"."
            else:
                result="This room contains "
                for i in range (0,len(contents)-1):
                    item=contents[i]
                    result=result+"a "+item+", "
                item=contents[len(contents)-1]
                result=result+"and a "+item+"."
        return result