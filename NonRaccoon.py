from RacoonPG import *
import random, math

class Enemy(Animal):
    def __init__():
        super().__init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, CRIT, turn, inCombat, money)
        self.isBoss = False
        self.inCombat = True
        self.POWER = 50

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


    def LVL_calculator(self, LVL):
        #Uses max level of raccoon as reference#
        toUse = 1
        for key in _raccoonArray.keys():
            if _raccoonArray[key].LVL > toUse:
                toUse = someplayerlist[raccoon].LVL
        self.LVL = toUse


    def is_boss(self):
        self.isBoss = True

class Encounter(Enemy):
    def __init__():
        super().__init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, POWER, CRIT, turn)

    def STAT_calculator(self, combat, combatants):
        level = combat.highestLVL(combatants)
        scalar = 0.02
        self.HP = random.randint(30, 90)
        self.MP = random.randint(30, 70)
        self.ATTK = random.randint(25, 50)
        self.DEF = random.randint(25, 50)
        self.MATTK = random.randint(25, 75)
        self.MDEF = random.randint(25, 50)
        self.DODGE = random.randint(1, 5)
        self.SPD = random.randint(1, 12)
        self.CRIT = random.randint(1, 5)
        for i in range(1, level):
            self.HP += 
            self.MP +=



class Boss(Enemy):
    def __init__():
        super().__init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, POWER, CRIT, turn)
        self.HP = random.randint(30, 90)
        self.MP = random.randint(30, 70)
        self.ATTK = random.randint(25, 50)
        self.DEF = random.randint(25, 50)
        self.MATTK = random.randint(25, 75)
        self.MDEF = random.randint(25, 50)
        self.DODGE = random.randint(1, 5)
        self.SPD = random.randint(1, 12)
        self.CRIT = random.randint(1, 5)
