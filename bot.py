import discord
import os
import requests
import json
from dotenv import load_dotenv
import sys
from PIL import Image
import ast
from RaccoonPG import *
import asyncio
import random
import copy
from Combat import Battle
from NonRaccoon import *

#from decimal import Decimal

load_dotenv()

client = discord.Client()

_raccoonArray = {}
canJoin = False
fighterIDs = []

def addFighter(id):
    fighterIDs.append(id)

def getRaccoon(str):
    arrVal = str.split(", ")
    if(arrVal[0] == "swordsman"):
        #LVL, name, HP, MP, ATTK, DEF, MATTK, MDEF, DODGE, SPD, EXP, EXPcap, POWER, CRIT, turn, inCombat, money
        return Swordsman(int(arrVal[1]), arrVal[2], int(arrVal[3]), int(arrVal[4]), int(arrVal[5]), int(arrVal[6]), int(arrVal[7]),
                    int(arrVal[8]), int(arrVal[9]), int(arrVal[10]), float(arrVal[11]), float(arrVal[12]), int(arrVal[13]), int(arrVal[14]),
                    arrVal[15], arrVal[16], int(arrVal[17]))
    if(arrVal[0] == "tank"):
        return Tank(int(arrVal[1]), arrVal[2], int(arrVal[3]), int(arrVal[4]), int(arrVal[5]), int(arrVal[6]), int(arrVal[7]),
                    int(arrVal[8]), int(arrVal[9]), int(arrVal[10]), float(arrVal[11]), float(arrVal[12]), int(arrVal[13]), int(arrVal[14]),
                    arrVal[15], arrVal[16], int(arrVal[17]))
    if(arrVal[0] == "healer"):
        return Healer(int(arrVal[1]), arrVal[2], int(arrVal[3]), int(arrVal[4]), int(arrVal[5]), int(arrVal[6]), int(arrVal[7]),
                    int(arrVal[8]), int(arrVal[9]), int(arrVal[10]), float(arrVal[11]), float(arrVal[12]), int(arrVal[13]), int(arrVal[14]),
                    arrVal[15], arrVal[16], int(arrVal[17]))
    if(arrVal[0] == "archer"):
        return ArcGun(int(arrVal[1]), arrVal[2], int(arrVal[3]), int(arrVal[4]), int(arrVal[5]), int(arrVal[6]), int(arrVal[7]),
                    int(arrVal[8]), int(arrVal[9]), int(arrVal[10]), float(arrVal[11]), float(arrVal[12]), int(arrVal[13]), int(arrVal[14]),
                    arrVal[15], arrVal[16], int(arrVal[17]))
    if(arrVal[0] == "mage"):
        return Mage(int(arrVal[1]), arrVal[2], int(arrVal[3]), int(arrVal[4]), int(arrVal[5]), int(arrVal[6]), int(arrVal[7]),
                    int(arrVal[8]), int(arrVal[9]), int(arrVal[10]), float(arrVal[11]), float(arrVal[12]), int(arrVal[13]), int(arrVal[14]),
                    arrVal[15], arrVal[16], int(arrVal[17]))

def read():
    global _raccoonArray
    l = open("saves.txt", "r")
    Lines = l.readlines()
    l.close()
    dummy = {}
    for line in Lines:
        vals = line.split(":")
        curr_dic = {int(vals[0].strip()[1:]): getRaccoon(str(vals[1].strip()[:-1]))}
        dummy = curr_dic | dummy
    _raccoonArray = copy.deepcopy(dummy)
    return dummy




def update(players):
    w = open("saves.txt", "w")
    for key in players:
        w.write("{" + str(key) + ":" + str(players[key]) + "}\n")



@client.event
async def on_ready():
    global fighterIDs
    async def showEnemies(arr):
        imageNames = []
        for key in arr:
            imageNames.append("./images/" + key.getName() + ".png")
        images = [Image.open(x) for x in imageNames]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGBA', (total_width, max_height))

        x_offset = 0
        for im in images:
          new_im.paste(im, (x_offset,0))
          x_offset += im.size[0]

        new_im.save('./images/enemies.png')

        await message.channel.send(file = discord.File( "./images/enemies.png"))

    async def showPlayers(arr):
        imageNames = []
        player_names = ""
        for key in arr:
            imageNames.append("./images/" + _raccoonArray[int(key.getName())].getType().split(".")[1].replace("'>", "") + ".png")
            player_names += "<@{}>".format(key.getName()) + ", "
        images = [Image.open(x) for x in imageNames]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGBA', (total_width, max_height))

        x_offset = 0
        for im in images:
          new_im.paste(im, (x_offset,0))
          x_offset += im.size[0]

        new_im.save('./images/players.png')

        await message.channel.send(file = discord.File( "./images/players.png"))
        await message.channel.send("In order: " + player_names)

        fightIDs = []

    async def startFight():
        #.join to join fight
        #Randomly spawn an enemy
        chan = client.get_channel(901363239605116989)
        global fighterIDs
        await chan.send("WE ARE GOING TO FIGHT SOON")
        canJoin = True
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await chan.send("10 SECONDS TO JOIN")
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        canJoin = False

        numEms = random.random() * 2 + 2
        totEms = []

        for i in range(int(numEms)):
            if(random.random() * 10 < 2):
                totEms.append(Encounter(0, "kanye", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, False, False)) #
            else:
                totEms.append(Encounter(0, "zombie", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, False, False)) #

        await chan.send("There are " + str(len(totEms)) + " enemies: \n")
        await showEnemies(totEms)

        fighters = []
        for ids in fighterIDs:
            fighters.append(_raccoonArray[ids])

        await chan.send("Players: \n")
        await showPlayers(fighters)

        for item in totEms:
            item.STAT_calculator(fighters)


        combat = Battle(fighters, totEms)
        combatants = combat.turnCycle()

        win = combat.winners(0, combatants)
        i = 0
        while True:
            if(i >= len(combatants)):
                i -= len(combatants)
            await message.channel.send("It is " + str("<@{}>".format(combatants[i].getName())) +  "'s turn!")

            if isinstance(combatants[i], Raccoon):
                def checkAttack(m):
                    return (m.content.split(" ")[0] == '.attack' and m.channel == message.channel) or (m.content.split(" ")[0] == '.stats' and m.channel == message.channel)
                invalid = True
                while invalid:

                    try:
                        msg = await client.wait_for('message', check=checkAttack)
                        cont = msg.content.split(" ")
                        input = int(cont[1])
                    except ValueError:
                        await message.channel.send('Wrong input, target a valid enemy (insert an integer)')
                    else:
                        if len(cont) != 2:
                            await message.channel.send('Wrong input, target a valid enemy using ".attack (int)"')
                        elif int(combatants[i].getName()) != msg.author.id:
                            await message.channel.send("Not your turn!")
                        elif int(cont[1]) >= len(totEms) or int(cont[1]) < 0:
                            await message.channel.send('Please pick a valid index')
                        else: invalid = False

                combatants[i].deal_damage(totEms[int(cont[1])])
                await message.channel.send(str(totEms[int(cont[1])].getName()) + " has " + str(totEms[int(cont[1])].getHP()) + " hp left")

            elif isinstance(combatants[i], Enemy):
                hitRac = combatants[i].nonRacctargeting(fighters)
                await message.channel.send(str("<@{}>".format(fighters[hitRac].getName())) + " got hit!")
                await message.channel.send(fighters[hitRac].get_stats(str("<@{}>".format(fighters[hitRac].getName()))))

            for numberino in range(len(combatants)):
                if combatants[numberino].HP <= 0:
                    combatants.pop(numberino)
                    break


            i += 1

            if(combat.winners(0, combatants)):
                break

        if(issubclass(type(combatants[0]), Raccoon)):
            await client.get_channel(901363239605116989).send("Raccoons win the fight!")
            enemy_num = len(totEms)
            mon_gain = combat.money_formula(enemy_num, len(fighters))
            for raccoon in fighters:
                exp_gain = combat.active_xp_formula(raccoon, totEms)
                _raccoonArray[int(raccoon.name)].money += mon_gain
                await message.channel.send(str(_raccoonArray[int(raccoon.name)].EXP))
                _raccoonArray[int(raccoon.name)].EXP += exp_gain
                await message.channel.send(str(_raccoonArray[int(raccoon.name)].EXP))
                update(_raccoonArray)

        elif isinstance((combatants[0]), Encounter):
            await client.get_channel(901363239605116989).send("Oh no! You lost!")


        await client.get_channel(901363239605116989).send("End of Combat")


        #DOREALCOMBAT

        fighterIDs = []
        inFight = False

    read()
    fight = False
    inFight = False
    await client.get_channel(901363239605116989).send("We're live! Be prepared for random battles!")
    await client.get_channel(901363239605116989).send(file=discord.File('./images/bonjour.gif'))

    while(True):
        await asyncio.sleep(random.random() * 1000 + 120)
        if not inFight:
            startFight()
          #await client.get_channel(901363239605116989).send("whoah look boss??") #put boss function/call here
            inFight = True


@client.event
async def on_message(message):
    global fighterIDs


    async def showEnemies(arr):
        imageNames = []
        for key in arr:
            imageNames.append("./images/" + key.getName() + ".png")
        images = [Image.open(x) for x in imageNames]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGBA', (total_width, max_height))

        x_offset = 0
        for im in images:
          new_im.paste(im, (x_offset,0))
          x_offset += im.size[0]

        new_im.save('./images/enemies.png')

        await message.channel.send(file = discord.File( "./images/enemies.png"))

    async def showPlayers(arr):
        imageNames = []
        player_names = ""
        for key in arr:
            imageNames.append("./images/" + _raccoonArray[int(key.getName())].getType().split(".")[1].replace("'>", "") + ".png")
            player_names += "<@{}>".format(key.getName()) + ", "
        images = [Image.open(x) for x in imageNames]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGBA', (total_width, max_height))

        x_offset = 0
        for im in images:
          new_im.paste(im, (x_offset,0))
          x_offset += im.size[0]

        new_im.save('./images/players.png')

        await message.channel.send(file = discord.File( "./images/players.png"))
        await message.channel.send("In order: " + player_names)

        fightIDs = []

    async def startFight():
        #.join to join fight
        #Randomly spawn an enemy
        chan = client.get_channel(901363239605116989)
        global fighterIDs
        await chan.send("WE ARE GOING TO FIGHT SOON")
        canJoin = True
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await asyncio.sleep(2) #change later
        await chan.send("10 SECONDS TO JOIN")
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        canJoin = False

        numEms = random.random() * 2 + 2
        totEms = []
        for i in range(int(numEms)):
            if(random.random() * 10 < 2):
                totEms.append(Encounter(0, "kanye", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, False, False)) #
            else:
                totEms.append(Encounter(0, "zombie", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, False, False)) #

        await chan.send("There are " + str(len(totEms)) + " enemies: \n")
        await showEnemies(totEms)

        fighters = []
        for ids in fighterIDs:
            fighters.append(_raccoonArray[ids])

        await chan.send("Players: \n")
        await showPlayers(fighters)

        for item in totEms:
            item.STAT_calculator(fighters)


        combat = Battle(fighters, totEms)
        combatants = combat.turnCycle()

        win = combat.winners(0, combatants)
        i = 0
        while True:
            if(i >= len(combatants)):
                i -= len(combatants)
            await message.channel.send("It is " + str("<@{}>".format(combatants[i].getName())) +  "'s turn!")

            if isinstance(combatants[i], Raccoon):
                def checkAttack(m):
                    return (m.content.split(" ")[0] == '.attack' and m.channel == message.channel) or (m.content.split(" ")[0] == '.stats' and m.channel == message.channel)
                invalid = True
                while invalid:

                    try:
                        msg = await client.wait_for('message', check=checkAttack)
                        cont = msg.content.split(" ")
                        input = int(cont[1])
                    except ValueError:
                        await message.channel.send('Wrong input, target a valid enemy (insert an integer)')
                    else:
                        if len(cont) != 2:
                            await message.channel.send('Wrong input, target a valid enemy using ".attack (int)"')
                        elif int(combatants[i].getName()) != msg.author.id:
                            await message.channel.send("Not your turn!")
                        elif int(cont[1]) >= len(totEms) or int(cont[1]) < 0:
                            await message.channel.send('Please pick a valid index')
                        else: invalid = False

                combatants[i].deal_damage(totEms[int(cont[1])])
                await message.channel.send(str(totEms[int(cont[1])].getName()) + " has " + str(totEms[int(cont[1])].getHP()) + " hp left")

            elif isinstance(combatants[i], Enemy):
                hitRac = combatants[i].nonRacctargeting(fighters)
                await message.channel.send(str("<@{}>".format(fighters[hitRac].getName())) + " got hit!")
                await message.channel.send(fighters[hitRac].get_stats(str("<@{}>".format(fighters[hitRac].getName()))))

            for numberino in range(len(combatants)):
                if combatants[numberino].HP <= 0:
                    combatants.pop(numberino)
                    break


            i += 1

            if(combat.winners(0, combatants)):
                break

        if(issubclass(type(combatants[0]), Raccoon)):
            await client.get_channel(901363239605116989).send("Raccoons win the fight!")
            enemy_num = len(totEms)
            mon_gain = combat.money_formula(enemy_num, len(fighters))
            for raccoon in fighters:
                exp_gain = combat.active_xp_formula(raccoon, totEms)
                _raccoonArray[int(raccoon.name)].money += mon_gain
                await message.channel.send(str(_raccoonArray[int(raccoon.name)].EXP))
                _raccoonArray[int(raccoon.name)].EXP += exp_gain
                await message.channel.send(str(_raccoonArray[int(raccoon.name)].EXP))
                update(_raccoonArray)

        elif isinstance((combatants[0]), Encounter):
            await client.get_channel(901363239605116989).send("Oh no! You lost!")


        await client.get_channel(901363239605116989).send("End of Combat")


        #DOREALCOMBAT

        fighterIDs = []
        inFight = False


    async def addPlayer(name, author):
        read()
        xp = await getMessages(author)
        if name == "swordsman":
            _raccoonArray[author] = Swordsman(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 50, 3, False, False, 0)

        if name == "tank":
            _raccoonArray[author] = Tank(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 50, 1, False, False, 0)
        if name == "mage":
            _raccoonArray[author] = Mage(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 50, 2, False, False, 0)
        if name == "archer":
            _raccoonArray[author] = ArcGun(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 50, 5, False, False, 0)

        if name == "healer":
            _raccoonArray[author] = Healer(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 50, 2, False, False, 0)

        update(_raccoonArray)
        await asyncio.sleep(0)

    async def getMessages(id):
        count_channel = client.get_channel(901288004394557463)
        messages = await count_channel.history(limit=500, oldest_first = False).flatten()
        tot = []
        for m in messages:
            if id == m.author.id:
                tot.append(m)
        return len(tot)

    def isPlaying(id):
        if id in _raccoonArray.keys():
            return True
        return False

    admin = False
    adminList = [259512440612585472, 128293175470063616]

    if message.author.id in adminList:
        admin = True

    if message.author == client.user:
        return

    tot_messages = await getMessages(message.author.id)

    players = read()


    msg = message.content.split(" ")

    if isPlaying(message.author.id) and message.channel.id == 901288004394557463:
        players[message.author.id].passive_xp_type()
        update(players)

    if msg[0] == ".add":
        if len(msg) != 3:
            return
        await message.channel.send(int(msg[1]) + int(msg[2]))

    if msg[0] == ".pic":
        await message.channel.send(file=discord.File('./images/god.png'))

    if msg[0] == ".kanye":
        await message.channel.send(file=discord.File('./images/kanye.png'))

    if msg[0] == ".showAllPlayers" and admin:
        players = read()
        imageNames = []
        player_names = ""
        for key in players:
            imageNames.append("./images/" + players[key].getType().split(".")[1].replace("'>", "") + ".png")
            player_names += "<@{}>".format(key) + ", "
        images = [Image.open(x) for x in imageNames]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGBA', (total_width, max_height))

        x_offset = 0
        for im in images:
          new_im.paste(im, (x_offset,0))
          x_offset += im.size[0]

        new_im.save('test.png')

        await message.channel.send(file = discord.File( "./images/test.png"))
        await message.channel.send("In order: " + player_names)

    if msg[0] == ".messages" and admin:
        await message.channel.send(tot_messages)

    if msg[0] == ".create": #.create TYPE
        if len(msg) != 2:
            await message.channel.send('Wrong size; use ".create TYPE"')
            return
        l = open("saves.txt", "r")
        Lines = l.readlines()
        l.close()

        w = open("saves.txt", "a")

        if(not any(str(message.author.id) in string for string in Lines)):

            if msg[1] == "swordsman":
                await addPlayer("swordsman", message.author.id)

            elif msg[1] == "tank":
                await addPlayer("tank", message.author.id)


            elif msg[1] == "mage":
                await addPlayer("mage", message.author.id)


            elif msg[1] == "healer":
                await addPlayer("healer", message.author.id)


            elif msg[1] == "archer":
                await addPlayer("archer", message.author.id)

            else:
                await message.channel.send('Pick one of the right classes')
                return
            await message.add_reaction('\N{THUMBS UP SIGN}')
        else:
            await message.channel.send("You already made a raccoon foul")

    if msg[0] == ".bee" and admin:
        file1 = open("bee.txt", "r")
        Lines = file1.readlines()
        file1.close()
        for line in Lines:
            if len(line) != 0 or line == "\n":
                await message.channel.send("{}".format(line.strip()))

    if msg[0] == ".allPlayers" and admin: #FIX ME
        test = read()
        final = ""
        for key in test:
            #if type(name) == "NoneType":
            final += "<@{}>".format(key) + " is a " + players[key].getType().split(".")[1].replace("'>", "") + "\n"
        await message.channel.send(final)

    if msg[0] == ".stats":
        s = "<@{}>".format(message.author.id)
        await message.channel.send(_raccoonArray[message.author.id].get_stats(s))

    if msg[0] == ".join" and not message.author.id in fighterIDs:
        global canJoin

        if(not isPlaying(message.author.id)):
            message.channel.send("You must have a raccon to play!")
            return
        addFighter(message.author.id)
        await message.add_reaction('\N{THUMBS UP SIGN}')

    if msg[0] == ".startBattle" and admin:
        await startFight()

    #if msg[0] == ".t" and admin:
    #    def check(m):
    #        return m.content.split(" ")[0] == '.attack' and m.channel == message.channel
    #    msg = await client.wait_for('message', check=check)
    #    await message.channel.send(msg.content)
    #.attack NUM
    #if msg[0] == ".attack" and message.author.id in fighterIDs: #AND IS THEIR TURN
    #    fighters[0].deal_damage(totEms[msg[1]])
    #    await message.channel.send("Enemy " + msg[1] + " has " + totEms[msg[1]].getHP() + " hp left")
    #if msg[0] == ".startBoss" and admin:
        #startBossFight()

    #if msg[0] == ".attack" and players[message.author.id].Attack:
        #reduce health
        #await message.channel.send(str(enemy.name) + "has taken {} damage!".format(damage))

TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)
