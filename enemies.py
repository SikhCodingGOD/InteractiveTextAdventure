class Enemy():
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin",hp=2,damage=1)

class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Spider",hp=4,damage=2)

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider",hp=10,damage=3)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre",hp=15,damage=5)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon",hp=50,damage=20)
