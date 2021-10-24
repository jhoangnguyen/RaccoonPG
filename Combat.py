from RaccoonPG import *
from NonRaccoon import *
import random, math
class combat():
    def __init__(self, party, enemies):
        self.party = party
        self.enemies = enemies

    def get_party(self):
        return self.party

    def get_enemies(self):
        return self.enemies

    def raccoonList(self, combatants):
        result = []
        for item in combatants:
            if isinstance(item, Raccoon):
                result.append(item)
        return result

    def numRaccoons(self, combatants):
        return len(combatants) - self.num_enemies(combatants)

    def num_enemies(self, combatants):
        count = 0
        for item in combatants:
            if isinstance(item, Enemy):
                count += 1
        return count

    def turnCycle(self):
        result = []
        combatants = []
        for member in self.get_party():
            combatants.append(member)
        for enemy in self.get_enemies():
            combatants.append(enemy)
        result = sorted(combatants, key = lambda x: x.SPD, reverse = True)
        return result

    def highestLVL(self):
        level = 0
        for member in self.get_party():
            if isinstance(member, Raccoon):
                if member.getLVL() > level:
                    level = member.getLVL()
        return level

    def money_formula(self, enemy, raccoons):
        total = 0
        base = 100
        bonus = 1
        if enemy.isBoss:
            base = 500
        total = ((base * self.highestLVL() *  bonus * (raccoons - 1)) / raccoons) // 1
        return total

    def active_xp_formula(self, enemies):
        gain = (((((5 / 3) * (self.LVL ** 4)) + (10 * (self.LVL ** 2)) + (100 * self.LVL))) / 5)
        for item in enemies:
            if item.isBoss:
                gain *= 5
        return gain


    def winners(self, enemy, combatants):
        # If boss.HP <= 0, raccoons win and end combat
        # ELSE IF all raccoons HP <= 0 and boss.HP > 0, raccoons lose and end combat
        # ELSE worry about this case later (what happens if a few party members die? split exp? set cooldown
        # for raccoon to wake up?)
        party = self.raccoonList(combatants)
        if all(item == isinstance(item, Raccoon) for item in combatants) and len(combatants) > 0:
            print("Some game-ending function for raccoon's victory")
            enemy_num = self.num_enemies(combatants)
            to_gain_money = self.money_formula(enemy_num, len(combatants) - enemy_num)
            to_gain_exp = self.active_xp_formula(self.get_enemies)
            for raccoon in party:
                raccoon.money += to_gain_money
                raccoon.EXP += to_gain_exp
        elif all(item == isinstance(item, Enemy) for item in combatants):
            print("Some game-ending function for when raccoons lose")
<<<<<<< HEAD
            # elif enemy.HP > 0 and

    # def check_status(self, turnorder):
=======
            # elif enemy.HP > 0 and 
        
    def clear_unc(self, combatants):
        for combatant in combatants:
            if combatant.HP <= 0:
                combatants.pop(combatant)
        return combatants

    # def battle(self, combatants):
    #     while not (all(item == isinstance(item, Raccoon) for item in combatants) or all(item == isinstance(item, Enemy) for item in combatants)):
    #         for combatant in combatants:
    #             #something something accept turn input here for each thingy#
            
>>>>>>> 9486f944838d5e46edb4bac444d5d97fd12ccac7
