from RaccoonPG import *
import random, math
class Combat(Animal):
    def __init__():
        super().__init__(self, LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money)
    def turnCycle(self, SPD):
        for key in _raccoonArray.keys():
            if _raccoonArray[key].inCombat:
                combatants.append(_raccoonArray[key])
        for key in _enemyArray.keys():
            if _enemyArray[key].inCombat:
                combatants.append(_enemyArray[key])

        combatants.sort(key = max(SPD))
        #stuff to allow specific order of inputs from specific raccoon#
        return combatants

    def numRaccoons(self, combatants):
        count = 0
        for item in combatants:
            if isinstance(item, Raccoon):
                count += 1
        return count

    def highestLVL(self, combatants):
        for item in combatants:
            if isinstance(item, Raccoon):
                if item.getLVL() > level:
                    level = item.getLVL()
        return level

    def money_formula(self, enemy, combatants):
        numRaccoons = self.numRaccoons(combatants)
        total = 0
        base = 100
        bonus = 1
        if enemy.isBoss:
            base = 500
        total = ((base * self.highestLVL(combatants) *  bonus * (numRaccoons - 1)) / numRaccoons) // 1
        return total

    def winners(self, enemy, combatants):
        # If boss.HP <= 0, raccoons win and end combat
        # ELSE IF all raccoons HP <= 0 and boss.HP > 0, raccoons lose and end combat
        # ELSE worry about this case later (what happens if a few party members die? split exp? set cooldown
        # for raccoon to wake up?)
        if enemy.HP <= 0:
            return True
        


    # def speedcheck(self, enemy):

    # Have to implement still 
    # - inCombat, turn