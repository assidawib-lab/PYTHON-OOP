class Hero:
    # self = dirinya sendiri / internal
    # __init__ = dipanggil pertama kali
    def __init__(self, name, level, hp, mana, role):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.role = role
        print(f"✨ Hero {self.name} telah di-summon!")

    # mengganti print objek dari bentuk memori 0x100..
    # menjadi format string, biar lebih enak dibaca
    def __str__(self):
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI"
            
        return f"[{self.name}] | HP: {self.hp} | STATUS: {status}"

    def damaged(self, damage):
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage!")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi!")
    
    def attack(self, enemy):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")

    def heal(self, amount):
        self.hp += amount
        print(f"💊 {self.name} mendapat heal +{amount}!")

    def critical(self, target):
        print(f"💥 {self.name} terkena 0 DMG!!")
        
# # panggil/summon hero-nya (buat objek)
# alucard = Hero("Alucard", 10, 100, 100)
# eudora = Hero("Eudora", 10, 100, 100)
# print("--- BATTLE START ---")
# alucard.attack(eudora)
# eudora.damaged(10)
# # di balas bwaang
# eudora.attack(alucard)
# alucard.damaged(5)
# alucard.damaged(5)
# alucard.damaged(5)
# # cek status terkini
# print(alucard)
# print(eudora)
# alucard.attack(eudora)
# print(">>> SKILL 1 API MANYALA BANG")
# eudora.damaged(80)
# print(eudora)
# eudora.heal(50)
# eudora.attack(alucard)
# print(">>> SKILL 1 ES BATU")
# alucard.damaged(80)
# print(alucard)
# alucard.heal(10)

# print("--BATTLE TERKINI--")
# print(eudora)
# print(alucard)
