from hero import Hero # {panggil class hero}

class Mage(Hero):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana, role="Mage")

    def critical(self, target):
        dmg = 50
        print(f"💥 {target.name} terkena {dmg} DMG!!")
        self.attack(target)
        target.damaged(dmg)