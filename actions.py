from Player import Player

#base class
class Action():
    def __init__(self,method,name,**kwargs):
        self.method = method
        self.name = name
        self.kwargs = kwargs
    #**kwargs allows a varying amount of arguments

    #how all actions will be outputted to the user
    def __str__(self):
        return "{}".format(self.name)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north,name="go north")

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south,name="go south")

class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east,name="go east")

class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west,name="go west")

class ViewInventory(Action):
    #Prints the player's inventory
    def __init__(self):
        super().__init__(method=Player.print_inventory,name="check inventory")

class Attack(Action):
    def __init__(self,enemy):
        super().__init__(method=Player.attack,name="attack")

class Flee(Action):
    def __init__(self,tile):
        super().__init__(method=Player.flee,name="flee",tile=tile)

class Take(Action):
    #takes available the item from the room and adds it to player's inventory
    def __init__(self,item):
        super().__init__(method=Player.take,name="take item",item=item)

class EnterShop(Action):
    def __init__(self):
        super().__init__(method=Player.enter_shop,name="enter shop")

class ViewCurrency(Action):
    def __init__(self):
        super().__init__(method=Player.print_currency,name="check currency")

class UsePotion(Action):
    def __init__(self):
        super().__init__(method=Player.use_potion,name="use potion")
