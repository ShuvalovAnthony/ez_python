# ФП - функциональное прогр
# ООП - объектно-ориент прогр


class Hero:    
    def __init__(self, name: str, lvl: int=1, hp: int=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def lvlUp(self):
        self.lvl += 1

    def setName(self, newName: str):
        self.name = newName

    def getDmg(self, dmg: int):
        self.hp -= dmg


class Swordsman(Hero):
    def __init__(self, name, lvl = 1, hp = 100, protectRate: float=0.8):
        self.protectRate = protectRate
        super().__init__(name, lvl, hp)

    def getDmg(self, dmg):
        self.hp -= self.protectRate*dmg


class Archer(Hero):
    ...


mickey = Swordsman("Mickey")

alex = Archer("Alex")