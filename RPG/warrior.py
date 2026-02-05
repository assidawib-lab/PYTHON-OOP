from hero import Hero # (panggil class hero)

class Warrior(Hero):
    def __init__(self, name, level, hp, mana):
        # super() = memanggil class parent (Hero)
        # set role sebagai warrior (default)
        super().__init__(name, level, hp, mana, role="Warrior")
    
    def critical(self, target):
        dmg = 80
        print(f"🔥 {self.name} menggunakan: GIGANTIC SLASH!")
        print(f"👹 {target.name} terkena critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
