from hero import Hero # (panggil class hero)

class Archer(Hero):
    def __init__(self, name, level, hp, mana):
        # super() = memanggil class parent (Hero)
        # set role sebagai archer (default)
        super().__init__(name, level, hp, mana, role="Archer")
    
    def critical(self, target):
        dmg = 60
        print(f"🔥 {self.name} menggunakan: ARROW RAIN!")
        print(f"👹 {target.name} terkena critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
