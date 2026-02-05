# class Hero:
#     def __init__(self, name, job, hp, hero_type="hero"):
#         self.name = name
#         self.job = job
#         self.hp = hp
#         # hero / normal / boss
#         self.type = hero_type
#         print(f"✨ {self.name} memasuki arena!")

#     def is_alive(self):
#         return self.hp > 0

#     def attack(self, enemy, damage):
#         # TODO:
#         # - cek hero masih hidup
#         if not self.is_alive():
#             print(f"{self.name} udah mati")
#         # - cek damage valid
#         if damage <= 0:
#             print(f"Damage tidak valid")
#             return
#         # - boss rage mode jika HP <= 50%
#         if self.hero_type == "boss" and self.hp < self.max_hp / 2:
#             self.rage_mode = True
#             print(f"😈 Raja Iblis memasuki RAGE MODE (SERIUS ANJAYY!!!!)")

#         return(f"{self.name} menyerang {enemy.name} dengan damage {damage}")
#         pass

#     def take_damage(self, damage):
#         # TODO:
#         # - kurangi HP
#         self.hp -= damage
#         print(f"{self.name} terkena {damage} damage")
#         # - HP tidak boleh < 0
#         if damage <= 0:
#             print(f"{self.name} sudah mati")
#         # - tampilkan pesan jika mati
#         if damage <= 0:
#             print(f"{self.name} sudah mati")
#         pass

#     def heal(self, Heal):
#         # TODO:
#         # - hero mati tidak bisa heal
#         if self.hp <= 0:
#             print(f"{self.name} sudah mati dan tidak bisa heal")
#         # - heal sesuai role
#         if self.job == "healer":
#             self.hp += Heal * 2
#             print(f"❤️ {self.name} melakukan heal sebesar {Heal*2} HP")
#         else:
#             self.hp += Heal
#             print(f"♥️ {self.name} melakukan heal sebesar {Heal} HP")
#         pass

# cici = Hero("CICI", "FIHTER", 100)
# xavier = Hero("XAVIER", "MAGE", 100)
# floryn = Hero("FLORYN", "HEALER", 100)
# ling = Hero("LING", "ASSASIN", 120)

# print("\n--- PARTY MEMASUKI DUNGEON ---\n")
# print("💫 CICI MASUK DUNGEON")
# print("💫 XAVIER MASUK DUNGEON")
# print("💫 FLORYN MASUK DUNGEON")

# print("\n--- GOBLIN MUNCUL !!! ---\n")
# goblin = Hero("GOBLIN", "MONSTER", 200)

# print("\n--- BATTLE START !!! ---\n")
# cici.attack(goblin, 30)
# cici.take_damage(30)
# print(f"SISA HP GOBLIN: {goblin.hp}\n")
# cici.attack(goblin, 50)
# goblin.take_damage(50)
# print(f"SISA HP GOBLIN: {goblin.hp}\n")
# goblin.attack(cici, 50)
# cici.take_damage(50)
# cici.heal(45)
# print(f"SISA HP CICI: {cici.hp}\n")
# cici.attack(goblin, 200)
# goblin.take_damage(200)
# print(f"SISA HP GOBLIN: {goblin.hp}\n")

# # monyet hama (MASBOY)

# print("\n--- MASBOY MUNCUL !!! ---\n")
# masboy = Hero("MASBOY", "PENJAGA DUNGEON", 600)

# print("\n--- BATTLE START !!! ---\n")
# ling.attack(masboy, 95)
# ling.take_damage(95)
# ling.heal(30)
# print(f"SISA HP MASBOY: {masboy.hp}\n")
# floryn.attack(masboy, 20)
# masboy.take_damage(20)
# print(f"SISA HP MASBOY: {masboy.hp}\n")
# cici.attack(masboy, 45)
# masboy.take_damage(45)
# print(f"SISA HP MASBOY: {masboy.hp}\n")
# masboy.attack(ling, 80)
# ling.take_damage(80)
# print(f"SISA HP LING: {ling.hp}\n")
# ling.heal(40)
# print(f"SISA HP LING: {ling.hp}\n")
# cici.attack(masboy, 300)
# masboy.take_damage(300)
# masboy.heal(100)
# masboy.attack(cici, 50)
# cici.take_damage(50)
# masboy.attack(floryn, 70)
# floryn.take_damage(70)

# print(f"SISA HP MINOTAURUS: {masboy.hp}\n")
# xavier.attack(masboy, 40)
# masboy.take_damage(40)
# print(f"SISA HP MASBOY: {masboy.hp}\n")
# ling.attack(masboy, 300)
# masboy.take_damage(300)

# # MATI KAN LU MONYET HAMA
# print(f"\nPERTEMPURAN SELESAI !!!")

class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        self.job = job.lower()
        self.hp = hp
        self.max_hp = hp
        self.type = hero_type
        self.rage_mode = False
        print(f"✨ {self.name} memasuki arena!")

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy, damage):

        if not self.is_alive():
            print(f"{self.name} sudah mati")
            return

        if damage <= 0:
            print("Damage tidak valid")
            return

        # Rage Mode
        if self.type == "boss" and self.hp <= self.max_hp / 2 and not self.rage_mode:
            self.rage_mode = True
            print(f"\n😈 {self.name} MEMASUKI RAGE MODE !!!")
            print("Aura merah menyelimuti tubuh boss...\n")

        if self.rage_mode:
            damage *= 2

        print(f"⚔️ {self.name} menyerang {enemy.name} dengan {damage} damage")
        enemy.take_damage(damage)

    def take_damage(self, damage):

        if not self.is_alive():
            return

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        print(f"💥 {self.name} terkena {damage} damage (HP: {self.hp})")

        if self.hp == 0:
            print(f"☠️ {self.name} telah mati!")

    def heal(self, amount):

        if not self.is_alive():
            print(f"{self.name} sudah mati dan tidak bisa heal")
            return

        if self.job == "healer":
            amount *= 2

        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"❤️ {self.name} heal {amount} HP (HP: {self.hp})")

print("\n🌌 LEGENDA DUNGEON KEGELAPAN")
print("Portal misterius muncul di kerajaan Aetheria...")
print("Empat pahlawan dikirim untuk menghentikan ancaman.\n")


cici = Hero("CICI", "fighter", 100)
xavier = Hero("XAVIER", "mage", 100)
floryn = Hero("FLORYN", "healer", 100)
ling = Hero("LING", "assassin", 120)

print("\n🛡️ Party memasuki dungeon terkutuk...\n")


print("👹 Seekor Goblin penjaga muncul!\n")
goblin = Hero("GOBLIN", "monster", 200)

print("\n⚔️ PERTEMPURAN DIMULAI!\n")

cici.attack(goblin, 30)
goblin.attack(cici, 25)

cici.attack(goblin, 50)
goblin.take_damage(50)

goblin.attack(cici, 40)
cici.take_damage(40)

cici.heal(30)

cici.attack(goblin, 200)
goblin.take_damage(200)

print("\nGoblin berhasil dikalahkan...\n")


print("🌋 Tanah dungeon bergetar...")
print("Sosok raksasa muncul dari kegelapan!\n")

masboy = Hero("MASBOY", "penjaga dungeon", 600, "boss")

print("\n😈 MASBOY MENANTANG PARTY!\n")

ling.attack(masboy, 95)
ling.take_damage(95)
ling.heal(30)

floryn.attack(masboy, 20)
masboy.take_damage(20)

cici.attack(masboy, 45)
masboy.take_damage(45)

masboy.attack(ling, 80)
ling.take_damage(80)

ling.heal(40)

cici.attack(masboy, 300)
masboy.take_damage(300)

# Rage kemungkinan aktif di sini

masboy.heal(100)
masboy.attack(cici, 50)
cici.take_damage(50)

masboy.attack(floryn, 70)
floryn.take_damage(70)

xavier.attack(masboy, 40)
masboy.take_damage(40)

ling.attack(masboy, 300)
masboy.take_damage(300)

print("\n🌅 MASBOY TUMBANG!")
print("Portal kegelapan mulai menutup...")
print("Namun bayangan misterius terlihat di dalam portal...\n")

print("🏆 PERTEMPURAN SELESAI!")
