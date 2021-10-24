import random, math

class Animal:
    def __init__ (self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        self.name = name
        self.LVL = LVL
        self.HP = HP
        self.MP = MP
        self.ATTK = ATTK
        self.DEF = DEF
        self.MATTK = MATTK
        self.MDEF = MDEF
        self.DODGE = DODGE
        self.SPD = SPD
        self.EXP = EXP
        self.EXPcap = 0
        self.POWER = POWER
        self.turn = False
        self.inCombat = False
        self.money = 0


        combatants = []

    def getType(self):
        return str(type(self)).lower().split(".")[1].replace(">", "").replace("'", "")

    def getLVL(self):
        return self.LVL

    def getATTK(self):
        return self.ATTK

    def getDEF(self):
        return self.DEF

    def getMATTK(self):
        return self.MATTK

    def getMDEF(self):
        return self.MDEF

    def getSPD(self):
        return self.SPD

    def getPOWER(self):
        return self.POWER


    def set_slow_xp(self, EXPcap, LVL):
        self.EXPcap += ((((5 / 3) * (self.LVL ** 4)) + (10 * (self.LVL ** 2)) + (100 * self.LVL)))

    def set_medium_xp(self, EXPcap, LVL):
        self.EXPcap += ((self.LVL ** 4) + (20 * (self.LVL ** 2)) + (100 * self.LVL))

    def set_fast_xp(self, EXPcap, LVL):
        self.EXPcap += (((4 / 5) * (self.LVL ** 4)) + ((self.LVL ** 3) * 5) + (100 * self.LVL))

    def damage_formula(self, enemy, POWER, LVL, ATTK, CRIT):
        roll = random.randit(1, 100)
        bonus = 1
        if roll <= self.CRIT:
            bonus = 1.5
        damage = ((((((2 * LVL) / 5) + 2) * self.POWER * (self.ATTK / enemy.getDEF)) / 50) * bonus) // 1
        return damage

    def target(self, combatants):
        targets = ''
        for i in combatants:
            targets += 'Target: {i}\n'.format(combatants[i])
        return targets

    def __str__(self):
        stats = ' (Level: {0}, Name: {1}, Health: {2}, Mana: {3}, Attack: {4}, Defense: {5}, M_Attack: {6}, M_Defense: {7}, Dodge: {8}, Speed: {9}, EXP: {10}, EXPcap: {11}, Power: {12}, CRTchance: {13}, Turn: {14}, inCombat: {15}, Money: {16}'.format(self.LVL, self.name, self.HP, self.MP, self.ATTK, self.DEF,  self.MATTK, self.MDEF, self.DODGE, self.SPD, self.EXP, self.EXPcap, self.POWER, self.CRIT, self.turn, self.inCombat, self.money)
        return stats






class Raccoon(Animal):
    def __init__ (self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        super().__init__(name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, CRIT, turn, inCombat, money)
        self.POWER = 35
        self.LVL = 1

    def join_combat(self):
        self.inCombat = True

    def reduce_health(self, enemy):
        damage = Animal.damage_formula(self, enemy, POWER, LVL, ATTK, CRIT)
        self.HP -= damage
        if self.HP <= 0:
            self.inCombat == False

    def lvl_up(self, EXP, EXPcap, LVL):
        temp = 0
        if self.EXP > self.EXPcap:
            temp = self.EXP - self.EXPcap
            LVL += 1
            self.EXPcap = 0
            self.EXP = temp



    #TO BE USED ON BOT RESTART#
    def passive_xp(self, num_msg):
        self.exp += (num_msg * (1/100000))

    #TO BE USED WHEN ACTIVE#
    def passive_xp_type(self):
        self.exp += 1/100000

class Swordsman(Raccoon):

    def set_slow_xp(self, EXPcap, LVL):
        self.EXPcap += ((((5 / 3) * (self.LVL ** 4)) + (10 * (self.LVL ** 2)) + (100 * self.LVL)))

    def set_medium_xp(self, EXPcap, LVL):
        self.EXPcap += ((self.LVL ** 4) + (20 * (self.LVL ** 2)) + (100 * self.LVL))

    def set_fast_xp(self, EXPcap, LVL):
        self.EXPcap += (((4 / 5) * (self.LVL ** 4)) + ((self.LVL ** 3) * 5) + (100 * self.LVL))

    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        self.name = name
        self.HP = 65
        self.MP = 45
        self.ATTK = 50
        self.DEF = 35
        self.MATTK = 40
        self.MDEF = 25
        self.DODGE = 2
        self.CRIT = 3
        self.SPD = 10
        self.EXP = EXP
        self.EXPcap = 0
        self.POWER = POWER
        self.turn = False
        self.inCombat = False
        self.money = 0
        self.LVL = 1
        self.set_slow_xp(EXPcap, LVL)

    def reduce_health(self, enemy):
        damage = Animal.damage_formula(self, enemy, POWER, LVL, ATTK, CRIT)
        self.HP -= damage
        if self.HP <= 0:
            self.inCombat == False

    def __str__(self):
        stats = 'swordsman, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}'.format(self.LVL, self.name, self.HP, self.MP, self.ATTK, self.DEF,  self.MATTK, self.MDEF, self.DODGE, self.SPD, self.EXP, self.EXPcap, self.POWER, self.CRIT, self.turn, self.inCombat, self.money)
        return stats



class Tank(Raccoon):
    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        self.name = name
        self.HP = 90
        self.MP = 30
        self.ATTK = 25
        self.DEF = 50
        self.MATTK = 25
        self.MDEF = 50
        self.DODGE = 1
        self.CRIT = 3
        self.SPD = 5
        self.EXP = EXP
        self.EXPcap = 0
        self.POWER = POWER
        self.turn = False
        self.inCombat = False
        self.money = 0
        self.LVL = 1

        self.set_fast_xp(EXPcap, LVL)

    def set_fast_xp(self, EXPcap, LVL):
        self.EXPcap += (((4 / 5) * (self.LVL ** 4)) + ((self.LVL ** 3) * 5) + (100 * self.LVL))

    def reduce_health(self, enemy):
        damage = Animal.damage_formula(self, enemy, POWER, LVL, ATTK, CRIT)
        self.HP -= damage
        if self.HP <= 0:
            self.inCombat == False

    def __str__(self):
        stats = 'tank, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}'.format(self.LVL, self.name, self.HP, self.MP, self.ATTK, self.DEF,  self.MATTK, self.MDEF, self.DODGE, self.SPD, self.EXP, self.EXPcap, self.POWER, self.CRIT, self.turn, self.inCombat, self.money)
        return stats

class Mage(Raccoon):
    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        self.name = name
        self.HP = 50
        self.MP = 60
        self.ATTK = 25
        self.DEF = 30
        self.MATTK = 65
        self.MDEF = 25
        self.DODGE = 2
        self.CRIT = 3
        self.SPD = 9
        self.EXP = EXP
        self.EXPcap = 0
        self.POWER = POWER
        self.turn = False
        self.inCombat = False
        self.money = 0
        self.LVL = 1

        self.set_medium_xp(EXPcap, LVL)


    def set_medium_xp(self, EXPcap, LVL):
        self.EXPcap += ((self.LVL ** 4) + (20 * (self.LVL ** 2)) + (100 * self.LVL))

    def reduce_health(self, enemy):
        damage = Animal.damage_formula(self, enemy, POWER, LVL, ATTK, CRIT)
        self.HP -= damage
        if self.HP <= 0:
            self.inCombat == False

    def __str__(self):
        stats = 'mage, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}'.format(self.LVL, self.name, self.HP, self.MP, self.ATTK, self.DEF,  self.MATTK, self.MDEF, self.DODGE, self.SPD, self.EXP, self.EXPcap, self.POWER, self.CRIT, self.turn, self.inCombat, self.money)
        return stats



class Healer(Raccoon):
    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        self.name = name
        self.HP = 40
        self.MP = 70
        self.ATTK = 25
        self.DEF = 25
        self.MATTK = 65
        self.MDEF = 25
        self.DODGE = 2
        self.CRIT = 3
        self.SPD = 9
        self.EXP = EXP
        self.EXPcap = 0
        self.POWER = POWER
        self.turn = False
        self.inCombat = False
        self.money = 0
        self.LVL = 1

        self.set_medium_xp(EXPcap, LVL)


    def set_medium_xp(self, EXPcap, LVL):
        self.EXPcap += ((self.LVL ** 4) + (20 * (self.LVL ** 2)) + (100 * self.LVL))

    def reduce_health(self, enemy):
        damage = Animal.damage_formula(self, enemy, POWER, LVL, ATTK, CRIT)
        self.HP -= damage
        if self.HP <= 0:
            self.inCombat == False

    def __str__(self):
        stats = 'healer, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}'.format(self.LVL, self.name, self.HP, self.MP, self.ATTK, self.DEF,  self.MATTK, self.MDEF, self.DODGE, self.SPD, self.EXP, self.EXPcap, self.POWER, self.CRIT, self.turn, self.inCombat, self.money)
        return stats



class ArcGun(Raccoon):
    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        self.name = name
        self.HP = 50
        self.MP = 50
        self.ATTK = 50
        self.DEF = 25
        self.MATTK = 50
        self.MDEF = 25
        self.DODGE = 4
        self.CRIT = 5
        self.SPD = 12
        self.EXP = EXP
        self.EXPcap = 0
        self.POWER = POWER
        self.turn = False
        self.inCombat = False
        self.money = 0
        self.LVL = 1

        self.set_slow_xp(EXPcap, LVL)

    def set_slow_xp(self, EXPcap, LVL):
        self.EXPcap += ((((5 / 3) * (self.LVL ** 4)) + (10 * (self.LVL ** 2)) + (100 * self.LVL)))

    def reduce_health(self, enemy):
        damage = Animal.damage_formula(self, enemy, POWER, LVL, ATTK, CRIT)
        self.HP -= damage
        if self.HP <= 0:
            self.inCombat == False

    def __str__(self):
        stats = 'archer, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}'.format(self.LVL, self.name, self.HP, self.MP, self.ATTK, self.DEF,  self.MATTK, self.MDEF, self.DODGE, self.SPD, self.EXP, self.EXPcap, self.POWER, self.CRIT, self.turn, self.inCombat, self.money)
        return stats
