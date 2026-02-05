class Hero:
    # self = dirinya sendiri / internal
    # __init__ = dipanggil pertama kali
    def __init__(self, name, level, hp, mana, role):
        # __namaAttr = maksudnya private atribute
        self.name = name
        self.level = level
        self.__hp = hp
        self.mana = mana
        self.role = role
        print(f"✨ Hero {self.name} telah di-summon!")

    # mengganti print objek dari bentuk memori 0x100..
    # menjadi format string, biar lebih enak dibaca
    def __str__(self):
        status = "🟢 HIDUP" 
        if self.__hp == 0:
            status = "💀 MATI"
            
        return f"[{self.role}] {self.name} | HP: {self.__hp} | STATUS: {status}"

    def damaged(self, damage):
        self.__hp -= damage
        print(f"💥 {self.name} terkena {damage} damage!")
        if self.__hp == 0:
            print(f"🚫 {self.name} tereliminasi!")
    
    def attack(self, enemy):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")

    def heal(self, amount):
        self.__hp += amount
        print(f"💊 {self.name} mendapat heal +{amount}!")

    def critical(self, target):
        print(f"💥 {self.name} terkena 0 DMG!!")
        
    # getter : mangambil attribute yang private
    def get_hp(self):
        return self.__hp
    
    # setter : memperbarui attribute yang private dari luar class
    def set_hp(self, add_hp):
        # tambahan validasi jangan sampe lewat max dari 100 hp
        self.__hp += add_hp