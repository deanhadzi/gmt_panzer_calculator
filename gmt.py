from dice import Die

d6 = Die(6)

class Tank:
    def __init__(self, name, gun, armor, health = 10):
        self.name = name
        self.health = health
        self.gun = gun
        self.armor = armor

    def __repr__(self):
        return f"{self.name}, {self.health}, {self.gun}, {self.armor}"

    def attack(self, defender):
        attackDamage = self.gun.damage + d6.roll_dice()
        defenderDamage = defender.takeHit(attackDamage)
        if defender.isAlive():
            print(f"{defender.name} is still alive")
        else:
            print("BOOM, you killed it!")
    
    def takeHit(self, attack):
        hitAmount = attack - self.armor.protection
        if hitAmount > 0:
            self.health -= hitAmount
            print(f"damage: {hitAmount}")
            return hitAmount
        else:
            return 0
    
    def isAlive(self):
        return self.health > 0

class Gun:
    def __init__(self, name, damage = 1):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return f"{self.name}, {self.damage}"

class Armor:
    def __init__(self, name, protection = 5):
        self.name = name
        self.protection = protection

    def __repr__(self):
        return f"{self.name}, {self.protection}"


