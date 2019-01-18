import items, world, tiles
import random

class Player():
    def __init__(self):
        self.inventory = [items.Potion()]
        self.hp = 20
        self.location_x, self.location_y = world.starting_position
        #sets the player's starting position to the StartingRoom tile
        self.victory = False
        self.in_battle = False
        self.in_shop = False
        self.currency = 20

    def is_alive(self):
        return self.hp > 0

    def has_potion(self):
        return any(item.name == "Potion" for item in self.inventory)

    def print_currency(self):
        print("\nYou have {} gold.\n".format(self.currency))

    def print_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("")
            for item in self.inventory:
                print(item,"\n")

    #base class for all movements
    def move(self,dx,dy):
        self.location_x += dx
        self.location_y += dy

    def move_north(self):
        self.move(dx=0,dy=-1)

    def move_south(self):
        self.move(dx=0,dy=1)

    def move_east(self):
        self.move(dx=1,dy=0)

    def move_west(self):
        self.move(dx=-1,dy=0)

    def attack(self,enemy):
        best_weapon = None
        max_dmg = 0
        self.in_battle = True
        #check player inventory for the weapon w/ the highest damage
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        print("You use your {} against the {}!".format(best_weapon.name,enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed the {}!".format(enemy.name))
            self.in_battle = False
        else:
            print("The {} has {} HP left.".format(enemy.name,enemy.hp))

    #the code can call this function and add an action function within the parameters
    def do_action(self,action,**kwargs):
        action_method = getattr(self,action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self,tile):
        #Moves the player randomly to an adjacent tile
        available_moves = tile.adjacent_moves()
        r = random.randint(0,len(available_moves)-1)
        self.do_action(available_moves[r])

    def take(self,item):
        self.inventory.append(item)
        item.takeable = False
        print("You took the {}.".format(item))

    def enter_shop(self):
        self.in_shop = True
        #sets room variable to the tile the player is located at
        room = world.tile_exists(self.location_x,self.location_y)
        while self.in_shop == True:
            print("\n'Welcome!' says the blacksmith.\n'Here is what I have available for sale:'\n")
            shop_list = room.shop_list()
            for item in shop_list:
                print(item,"\n")
            purchase = input("What would you like to purchase? (You have {} gold.)\n".format(self.currency))
            for item in shop_list:
                if purchase == item.name:
                    if self.currency >= item.value:
                        self.currency -= item.value
                        self.inventory.append(item)
                        print("Sold.")
                        break
                    else:
                        print("You do not have enough gold.")
                        break
            if purchase != item.name:
                print("I do not have that for sale.")
            shopping = input("Would you like to make more purchases?\n")
            if shopping == "yes":
                continue
            else:
                print("\nCome back soon!\n")
                self.in_shop = False
                break
            
    def use_potion(self):
        print("You use a potion to restore 10 health.")
        if self.hp < 10:
            self.hp += 10
        else:
            self.hp = 20
        #removes the instance of the potion class from the player's inventory
        for i, item in enumerate(self.inventory):
            if item.name == "Potion":
                del self.inventory[i]
                break
