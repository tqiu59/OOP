class Room:
    
    no_rooms = 0
    
    def __init__(self, room_name):
        self.name = room_name
        self._desc = None
        self.linked_rooms = {}
        self.char = None
        self.item = None
        
        Room.no_rooms += 1
        
        
    def get_name(self):
        return self.name
    
    def set_name(self, room_name):
        self.name = room_name
        
              
    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, room_desc):
        self._desc = room_desc

    def describe(self):
        print(self.description)
        
        
    def get_char(self):
        return self.char
    
    def set_char(self, new_char):
        self.char = new_char
          
    def get_item(self):
        return self.item

    def set_item(self, item_name):
        self.item = item_name
        
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print(self.name + " linked rooms : " + repr(self.linked_rooms))
    
    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.desc)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
            
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("you can't go that way")
            return self
        
        