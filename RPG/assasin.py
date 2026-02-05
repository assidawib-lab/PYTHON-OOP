from hero import Hero # (panggil class hero)

class Assasin(Hero):
    def __init__(self, name, level, hp, mana):
        # super() = memanggil class parent (Hero)
        # set role sebagai assasin (default)
        super().__init__(name, level, hp, mana, role="Assasin")
    
    def critical(self, target):
        dmg = 70
        print(f"🔥 {self.name} menggunakan: SHADOW KILL!")
        print(f"👹 {target.name} terkena critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
