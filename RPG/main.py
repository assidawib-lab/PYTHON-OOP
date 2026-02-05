from mage import Mage
from warrior import Warrior
from archer import Archer
from assasin import Assasin
from monster import Monster

print('\n----- SUMMON SEMUA HERO -----\n')
alucard = Warrior("alucard", 80, 100, 100)
alok = Mage("alok", 85, 100, 100)
layla = Archer("layla", 80, 100, 100)
hayabusa = Assasin("hayabusa", 83, 100, 100)

print('\n----- SUMMON MONSTER -----\n')
salamander = Monster("Salamander", 100, 1000, 1000)

print('== MULAI GUILD PARTY ==')
guild_party = [
    alucard,
    alok,
    layla,
    hayabusa
]
print(f"Komandan: 'Pasukan siap!'")
print(f"Total {len(guild_party)} pahlawan")

print("\n⚔️ --- RAID DIMULAI --- ⚔️\n")
# alok.critical(salamander)
# alucard.critical(salamander)

# # pasang cheat hp +1000
# alucard.name = "Bambang"
# # ambil hp  doang
# print(f"HP alucard: {alucard.get_hp()}")
# alucard.set_hp(100)

# print(alucard)
# print(alok)
# print(layla)
# print(hayabusa)
# print(salamander)

running = True
while running:
    print(salamander)
    print("1. Attack, 2. Heal, 3. Exit")
 
    aksi = int(input(">> Pilih Aksi :"))
    if aksi == 1:
        dmg = 10
        # alucard.attack(salamander)
        # alok.attack(salamander)
        # layla.attack(salamander)
        # hayabusa.attack(salamander)
        # salamander.damaged(dmg * 4)
        for party in guild_party:
            party.attack(salamander)
            salamander.damaged(dmg)

        # cek jika hp 0 = akhir permainan
        if (salamander.hp == 0):
            print("Monster dah mati, dahan bee")
            running = False
        
    elif aksi == 2:
        alok.heal(10)
        # boleh yang lain heal juga ntar
        # ...

    elif aksi == 3:
        print("Game Berakhir, Bye Bye!")
        running = False