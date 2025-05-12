from random import randint
from time import sleep


class Hero:    
    def __init__(self, name: str, dmg: int, hp: int=100):
        self.name = name
        self.dmg = dmg
        self.hp = hp
        self.defaultHp = hp

    def changeHp(self, deltaHpAmount: int):
        self.hp += deltaHpAmount
        if self.hp >= self.defaultHp:
            self.hp = self.defaultHp
        if self.hp <= 0:
            self.hp = 0
            self.death()

    def attack(self, target):
        target.changeHp(-1*self.dmg)
        print(self.name, "hit", target.name, "left him with", target.hp, "hp")

    def death(self):
        print(self.name, 'has been killed')


class Swordsman(Hero):
    def __init__(self, name, lvl = 1, hp = 100, protectRate: float=0.8):
        self.protectRate = protectRate
        super().__init__(name, lvl, hp)


    # def changeHp(self, deltaHpAmount):
    #     self.hp += self.protectRate*deltaHpAmount

    def changeHp(self, deltaHpAmount):
        return super().changeHp(deltaHpAmount*self.protectRate)
        

class Archer(Hero):
    ...


class Assasin(Hero):
    def __init__(self, name, dmg, hp = 100, critRate = 2.5):
        self.critRate = critRate
        super().__init__(name, dmg, hp)

    def attack(self, target):
        chance = randint(1, 100)

        if chance <= 25:
            target.changeHp(-1*self.dmg*self.critRate)
            print(self.name, "hit with crit", target.name, "left him with", target.hp, "hp")
        else:
            target.changeHp(-1*self.dmg)
            print(self.name, "hit", target.name, "left him with", target.hp, "hp")


class Priest(Hero):
    def __init__(self, name: str, dmg: int, healAmount: int, hp = 100):
        self.healAmount = healAmount
        super().__init__(name, dmg, hp)

    def heal(self, target):
        target.changeHp(self.healAmount)
        print(self.name, "healed", target.name, "left him with", target.hp, "hp")



mickey = Swordsman("Mickey", 30)
roberto = Priest("Roberto", 5, 25, 70)

alex = Archer("Alex", 20)
dima = Assasin('Dima', 30, 50)


def attackQueue(attacker, targets: list):
    if attacker.hp > 0:
        for target in targets:
            if target.hp > 0:
                attacker.attack(target)
                return
    return


def healQueue(healer, targets: list):
    if healer.hp > 0:
        targets = sorted(targets, key=lambda x: x.hp)
        targets = [i for i in targets if i.hp > 0]
        if targets:
            healer.heal(targets[0])
            return
    return


while True:
    sleep(5)

    if 0 < mickey.hp < 50:
        healQueue(roberto, [mickey])
    else:
        attackQueue(roberto, [dima, alex])
    
    

# while mickey.hp > 0:
#     sleep(1)
#     chance = randint(1, 100)

#     if chance < 50:
#         dima.attack(mickey)
#     else:
#         roberto.heal(mickey)

# print(mickey.hp)