class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.desc = None
    
    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    
    def get_desc(self):
        return self.desc
    
    def set_desc(self, item_desc):
        self.desc = item_desc
        
    def describe(self):
        print("The [" + self.name + "] is here - " + self.desc)