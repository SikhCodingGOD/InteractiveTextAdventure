import items, enemies, actions, world
import random
from Player import Player

class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()
        #makes sure programmer does not accidentally create a tile using the base class

    def modify_player(self,player):
        raise NotImplementedError()

    def adjacent_moves(self):
        #Returns all move actions based of if there are adjacent tiles
        moves = []
        if world.tile_exists(self.x+1,self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x-1,self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x,self.y-1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x,self.y+1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self,player):
        #Returns all of the available actions in this room
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewCurrency())
        if player.has_potion():
            moves.append(actions.UsePotion())
        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return "You find yourself in a cave with a flickering torch on the wall.\n\
You can make out two paths, each equally dark and foreboding."

    def modify_player(self,player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self,x,y,item):
        self.item = item
        super().__init__(x,y)

    def add_loot(self,player):
        player.inventory.append(self.item)

    def modify_player(self,player):
        pass

    def available_actions(self,player):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewCurrency())
        if player.has_potion():
            moves.append(actions.UsePotion())
        if self.item.takeable:
            moves.append(actions.Take(item=self.item))
        return moves

class ShopRoom(MapTile):
    def __init__(self,x,y):
        super().__init__(x,y)

    def modify_player(self,player):
        pass

    def available_actions(self,player):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewCurrency())
        if player.has_potion():
            moves.append(actions.UsePotion())
        moves.append(actions.EnterShop())
        return moves
    
class EnemyRoom(MapTile):
    def __init__(self,x,y,enemy):
        self.enemy = enemy
        super().__init__(x,y)

    def modify_player(self,player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage! You have {} HP remaining.".format(self.enemy.damage, player.hp))

    def available_actions(self,player):
        if self.enemy.is_alive():
            moves = [actions.Flee(tile=self),actions.Attack(enemy=self.enemy)]
            if player.has_potion():
                moves.append(actions.UsePotion())
            return moves
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            moves.append(actions.ViewCurrency())
            if player.has_potion():
                moves.append(actions.UsePotion())
            return moves

class EnemyAndLootRoom(MapTile):
    def __init__(self,x,y,enemy,item):
        self.enemy = enemy
        self.item = item
        super().__init__(x,y)

    def add_loot(self,player):
        player.inventory.append(self.item)

    def modify_player(self,player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage! You have {} HP remaining.".format(self.enemy.damage, player.hp))

    def available_actions(self,player):
        if self.enemy.is_alive():
            moves = [actions.Flee(tile=self),actions.Attack(enemy=self.enemy)]
            if player.has_potion():
                moves.append(actions.UsePotion())
            return moves
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            moves.append(actions.ViewCurrency())
            if player.has_potion():
                moves.append(actions.UsePotion())
            if self.item.takeable:
                moves.append(actions.Take(item=self.item))
            return moves

class EmptyCavePath(MapTile):
    def intro_text(self):
        return "Another empty, unremarkable part of the cave."

    def modify_player(self,player):
        pass

class GoblinRoom(EnemyRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.Goblin())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A small goblin jumps out in front of you, lunging at you with his knife."
        else:
            return "The lifeless body of a goblin rots on the ground.\n\
The rest of the area looks empty."

class SpiderRoom(EnemyRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.Spider())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A spider jumps out at you!"
        else:
            return "A dead spider rests on the cavern floor.\n\
The rest of the area looks empty."

class GiantSpiderRoom(EnemyRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A giant spider falls on top of you!"
        else:
            return "A giant spider lies dead on the cavern floor.\n\
The rest of the area looks empty."

class OgreRoom(EnemyRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A massive ogre turns arounds to face you.\nIt swings its mace in your direction!"
        else:
            return "A dead ogre lies on the ground where it was slain.\n\
The rest of the area looks empty."

class DragonRoom(EnemyRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A mighty dragon swoops down from above, a burst of flame erupts from its jaws!"
        else:
            return "A mighty dragon lies dead on the ground.\n\
The rest of the area looks empty."

class FindSwordRoom(LootRoom):
    def __init__(self,x,y):
        super().__init__(x,y,items.Sword())

    def intro_text(self):
        if self.item.takeable == True:
            return "Looks like another empty part of the cave, until you notice something shiny in the corner. It's a sword!"
        else:
            return "Another empty, unremarkable part of the cave."

class LeaveCaveRoom(MapTile):
    #Victory tile
    def intro_text(self):
        return "You see a light in the distance... it grows bigger as you get closer...\n\
It's sunlight! You have escaped the underground, victory is yours!"

    def modify_player(self,player):
        player.victory = True

class GoblinAndDaggerRoom(EnemyAndLootRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.Goblin(),items.Dagger())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A small goblin jumps out in front of you, lunging at you with his knife."
        else:
            if self.item.takeable == True:
                return "Nothing here but a rotting, dead goblin. Oh! Looks like the goblin dropped his dagger."
            else:
                return "Nothing here but a rotting, dead goblin."

class OgreAndMaceRoom(EnemyAndLootRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.Goblin(),items.Dagger())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A massive ogre turns arounds to face you.\nIt swings its mace in your direction!"
        else:
            if self.item.takeable == True:
                return "The large body of a dead ogre lies on the dirt floor. His mace lies beside him."
            else:
                return "The large body of a dead ogre lies on the dirt floor."

class BuyWeaponsRoom(ShopRoom):
    def __init__(self,x,y):
        super().__init__(x,y)

    def intro_text(self):
        return "You see a blacksmith shop to your right.\n\
The rest of the area looks empty."

    def shop_list(self):
        return [items.Dagger(),items.Sword(),items.Broadsword(),items.Potion()]
