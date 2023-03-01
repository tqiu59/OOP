from rpginfo import RPGInfo
from room import Room
from item import Item
from character import Enemy
from character import Character
from character import Friend
from time import sleep


spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()

#########creating rooms#########
kitchen = Room("kitchen")
dining_hall = Room("dining hall")
ballroom = Room("ballroom")
bathroom = Room("Bathroom")
guest_room = Room("GuestRoom")

print("There are " + str(Room.no_rooms) + " rooms to explore")

#########giving room desc#########
kitchen.desc = "A dank and dirty room buzzing with flies and crawling with roachs!"
ballroom.desc = "A vast room with a shiny wooden floor; huge candlesticks guard the entrance"
dining_hall.desc = "A large and beautifully ornamented room with sparkling crystals and exquiset decore"
guest_room.desc = "A cozy and comfortable environment that engulfs you with a beautifull scent of flowers"

#########setting room links#########
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

ballroom.link_room(dining_hall,"east")
dining_hall.link_room(ballroom,"west")

#########creating items#########
cheese = Item("cheese")
cheese.set_desc("A strangely weapon-like block of cheese")
kitchen.set_item(cheese)

book = Item("book")
book.set_desc("A mysterious book with words you do not understand")
dining_hall.set_item(book)

#########creating enemies#########
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("hello there")
dave.set_weak("cheese")
dining_hall.set_char(dave)

bob = Friend("Bob", "A friendly ghost")
bob.set_conversation("general kenobi")
ballroom.set_char(bob)

#########player 'attributes'#########
backpack = []
current_room = kitchen

#########runtime code#########
dead = False
while dead == False:
    print("\n")
    current_room.get_details()
    item = current_room.get_item()
    if item is not None:
        item.describe()
        
    inhabitant = current_room.get_char()
    if inhabitant is not None:
        inhabitant.describe()
    
    command = input("> ")
    if command in ["north", "east", "south", "west"]:
        current_room = current_room.move(command)
        
    elif command in ["talk", "fight"] and inhabitant is None:
        print("you can't " + command + " here, there is no one around!")
        
    elif command == "talk":
        Enemy.talk(inhabitant)
    
    elif command == "fight":
        print(backpack)
        weapon = input("what item would you like to attack with?")
        if weapon not in backpack:
            weapon = "air"
        survive = inhabitant.fight(weapon)
        if survive is False:
            dead = True
        else:
            current_room.set_char(None)
            if Enemy.defeat_thres == 0:
                print("woo you killed everything bad, well done, have a cookie")
                print("\n---------COOKIE--------\n")
                dead = True
        sleep(1)
            
    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")
        sleep(1)
        
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
