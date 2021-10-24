from RaccoonPG import *
import random, math
import Combat

class Enemy(Animal):
    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        super().__init__(LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money)
        self.isBoss = False
        self.POWER = 50
        self.inCombat = True

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


    def LVL_calculator(self, party):
        #Uses max level of raccoon as reference#
        toUse = 1
        for member in party:
            if member.LVL > toUse:
                toUse = member.LVL
        self.LVL = toUse


    def is_boss(self):
        self.isBoss = True

    def deal_damage(self, raccoon):
        damage = Animal.damage_formula(self, raccoon, self.POWER, self.LVL, self.ATTK, self.CRIT)
        raccoon.HP -= damage
        if raccoon.HP <= 0:
            raccoon.inCombat == False

    def nonRacctargeting(self, raccoon_array):
        raccoon_to_hit = random.randint(1, self.get_party.length())
        self.deal_damage(raccoon_array[raccoon_to_hit])

class Encounter(Enemy):
    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money):
        super().__init__(LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money)

    def highestLVL(self, raccoons):
        result = 0
        raccoons = sorted(raccoons, key = lambda x: x.LVL)
        for raccoon in raccoons:
            if raccoon.LVL > result:
                result = raccoon.LVL
        return result

    def STAT_calculator(self, raccoons):
        level = self.highestLVL(raccoons)
        scalar = 0.04
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
            self.HP += (self.HP * scalar)
            self.MP += (self.MP * scalar)
            self.ATTK += (self.ATTK * scalar)
            self.DEF += (self.DEF * scalar)
            self.MATTK += (self.MATTK * scalar)
            self.MDEF += (self.MDEF * scalar)
            self.DODGE += (self.DODGE * scalar)
            self.SPD += (self.SPD * scalar)
            self.CRIT += (self.CRIT * scalar)

        self.HP //= 1
        self.MP //= 1
        self.ATTK //= 1
        self.DEF //= 1
        self.MATTK //= 1
        self.MDEF //= 1
        self.DODGE //= 1
        self.SPD //= 1
        self.CRIT //= 1



class Boss(Enemy):
    def __init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, POWER, CRIT, turn, inCombat):
        super().__init__(LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, POWER, CRIT, turn, inCombat)
        self.isBoss = True

        def STAT_calculator(self):
            scalar = 0.02
            self.HP = random.randint(200, 300)
            self.MP = random.randint(150, 200)
            self.ATTK = random.randint(80, 100)
            self.DEF = random.randint(70, 80)
            self.MATTK = random.randint(90, 125)
            self.MDEF = random.randint(25, 50)
            self.DODGE = random.randint(1, 5)
            self.SPD = random.randint(1, 3)
            self.CRIT = random.randint(1, 5)

            for i in range(1, self.LVL):
                self.HP += (self.HP * scalar)
                self.MP += (self.MP * scalar)
                self.ATTK += (self.ATTK * scalar)
                self.DEF += (self.DEF * scalar)
                self.MATTK += (self.MATTK * scalar)
                self.MDEF += (self.MDEF * scalar)
                self.DODGE += (self.DODGE * scalar)
                self.SPD += (self.SPD * scalar)
                self.CRIT += (self.CRIT * scalar)

            self.HP //= 1
            self.MP //= 1
            self.ATTK //= 1
            self.DEF //= 1
            self.MATTK //= 1
            self.MDEF //= 1
            self.DODGE //= 1
            self.SPD //= 1
            self.CRIT //= 1
