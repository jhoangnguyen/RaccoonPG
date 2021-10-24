import RaccoonPG as r, NonRaccoon as n, Combat as c
# Stats- LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money
warrior = r.Raccoon(1, "Ike", 50, 30, 75, 65, 40, 50, 70, 80, 0, ((5/3)+10+100), 35, 50, False, False, 25)
print(warrior)
