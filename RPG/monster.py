class Monster:
    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        print(f"✨ Hero {self.name} telah di-summon!")

    def __str__(self):
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI"
            
        return f"[Monster] {self.name} | HP: {self.hp} | STATUS: {status}"
    
    def damaged(self, damage):
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage!")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi!")