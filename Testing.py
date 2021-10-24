from RaccoonPG import *
from NonRaccoon import *
from Combat import *
# Stats- LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money
warrior = Raccoon(1, "Ike", 50, 30, 75, 65, 40, 50, 70, 80, 0, ((5/3)+10+100), 35, 50, False, False, 25)
warrior2 = Raccoon(1, "Marth", 50, 30, 75, 65, 40, 50, 70, 70, 0, ((5/3)+10+100), 35, 50, False, False, 25)
enemy = Enemy(0, "Kanye", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, False, 0)
combat = Combat([warrior, warrior2], [enemy])
# print(warrior)
# print(warrior.get_stats())

for i in combat.turnCycle():
    print(i)