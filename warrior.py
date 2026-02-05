from hero import Hero # {panggil class hero}

class Warrior(Hero):
    def __init__(self, name, level, hp, mana):
        super().__init__(name, level, hp, mana, role="Warrior")

    def critical(self, target):
        dmg = 50
        print(f"💥 {target.name} terkena {dmg} DMG!!")
        self.attack(target)
        target.damaged(dmg)