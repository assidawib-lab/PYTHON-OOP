from hero import Hero
from mage import Mage

alucard = Hero("alucard", 1, 100, 100, "Warrior")
alok = Mage("alok", 1, 100, 100, "Healer")

alok.attack(alucard)
alucard.damaged(10)
alok.critical(alucard)
alucard.critical(alok)
print(alucard)
print(alok)