
class Tank:
    def __init__(self, name, gun, armor, health = 10):
        self.name = name
        self.health = health
        self.gun = gun
        self.armor = armor

    def __repr__(self):
        return f"{self.name}, {self.health}"

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


