class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    
class Enemy(Character):
    
    defeat_thres = 0
    def __init__(self, char_name, char_desc):
        super().__init__(char_name, char_desc)
        self.weakness = None
        self.want = None
        self.tired = None
        
        Enemy.defeat_thres += 1
        
    def get_weak(self):
        return self.weakness
        
    def set_weak(self, enemy_weak):
        self.weakness = enemy_weak
        
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Enemy.defeat_thres -=1
            return True
        elif combat_item == "air":
            print("you swipe wildly with an imaginary object, but " + self.name + " is a better fighter, sorry")
            return False
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
        
    
    def get_tired(self):
        return self.tired
    
    def set_tired(self, sleep_item):
        self.tired = sleep_item
    
    def sleep(self, sleep_item):
        if sleep_item == self.tired:
            print("you successfully put " + self.name + " to sleep with the " + sleep_item)
        else:
            print("unlucky, " + self.name + " didn't fall asleep")
            
            
    def steal(self):
        print("You steal from " + self.name)
        
        
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(self.name + " hugs you back!")
