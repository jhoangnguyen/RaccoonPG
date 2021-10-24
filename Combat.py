from RacoonPG import *
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
    
    def highestLVL(self, combatants):
        for item in Animal.combatants:
            if isinstance(item, Raccoon):
                if item.getLVL() > level:
                    level = item.getLVL()
        return level

    # def speedcheck(self, enemy):

    # Have to implement still 
    # - inCombat, turn