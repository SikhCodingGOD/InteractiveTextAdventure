class Item():
    def __init__(self,name,description,value,takeable):
        self.name = name
        self.description = description
        self.value = value
        self.takeable = True
#takeable changes to false when the item has been taken from a room

#how an item will output to the user
    def __str__(self):
        return "{}\n{}\nValue: {} gold".format(self.name,self.description,self.value)

class Potion(Item):
    def __init__(self):
        super().__init__(name="Potion",
                         description="A potion that restores 10 health.",
                         value=20,
                         takeable=True)

#base weapon class; adds the 'damage' variable
class Weapon(Item):
    def __init__(self,name,description,value,takeable,damage):
        self.damage = damage
        super().__init__(name,description,value,takeable)

    def __str__(self):
        return "{}\n{}\nValue: {} gold\nDamage: {}".format(self.name,self.description,self.value,self.damage)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A sharp-edged sword.",
                         value=15,
                         takeable=True,
                         damage=5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A steel dagger.",
                         value=10,
                         takeable=True,
                         damage=2)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A rock a little smaller than your fist.",
                         value=0,
                         takeable=True,
                         damage=1)

class Battleaxe(Weapon):
    def __init__(self):
        super().__init__(name="Battleaxe",
                         description="A large, two-handed battleaxe.",
                         value=45,
                         takeable=True,
                         damage=14)

class Mace(Weapon):
    def __init__(self):
        super().__init__(name="Mace",
                         description="A large weapon suitable for bludgeoning.",
                         value=30,
                         takeable=True,
                         damage=10)

class Broadsword(Weapon):
    def __init__(self):
        super().__init__(name="Broadsword",
                         description="A large sword wielded with two hands.",
                         value=22,
                         takeable=True,
                         damage=8)

class Warhammer(Weapon):
    def __init__(self):
        super().__init__(name="Warhammer",
                         description="A long rod with a deadly spiked hammer attached.",
                         value=60,
                         takeable=True,
                         damage=17)

class Flail(Weapon):
    def __init__(self):
        super().__init__(name="Flail",
                         description="A chain with a huge spiked ball attached, used for bashing skulls.",
                         value=85,
                         takeable=True,
                         damage=20)

#does not function yet
class Longbow(Weapon):
    def __init__(self):
        super().__init__(name="Longbow",
                         description="A curved piece of wood with a taunt string attached, used to launch arrows great distances.",
                         value=40,
                         takeable=True,
                         damage=2)

