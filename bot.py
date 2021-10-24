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
from Combat import *
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
    async def startFight():
        #.join to join fight
        #Randomly spawn an enemy
        chan = client.get_channel(901363239605116989)
        global fighterIDs
        await chan.send("WE ARE GOING TO FIGHT SOON")
        canJoin = True
        await asyncio.sleep(50)
        await chan.send("10 SECONDS TO JOIN")
        await asyncio.sleep(10)
        canJoin = False
        await chan.send("NO LONGER CAN JOIN")

        await chan.send(fighterIDs)

        numEms = random.random() * 2 + 1
        totEms = []
        for i in range(int(numEms)):
            totEms.append(Encounter()) #0, i, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, False, False
        chan.send(totEms)

        fighters = []
        for ids in fighterIDs:
            fighters.append(_raccoonArray[ids])
        chan.send(fighters)

        for item in totEms:
            item.STAT_calculator(0, fighters)

        await client.get_channel(901363239605116989).send("ready for next boss")
        inFight = False

    read()
    fight = False
    inFight = False
    await client.get_channel(901363239605116989).send("We're live! Be prepared for random battles!")
    while(True):
        await asyncio.sleep(random.random() * 1000 + 120)
        if not inFight:
            startFight()
          #await client.get_channel(901363239605116989).send("whoah look boss??") #put boss function/call here
            inFight = True


@client.event
async def on_message(message):
    global fighterIDs

    async def startFight():
        #.join to join fight
        #Randomly spawn an enemy
        global fighterIDs
        chan = client.get_channel(901363239605116989)

        await chan.send("WE ARE GOING TO FIGHT SOON")
        canJoin = True
        await asyncio.sleep(0)
        await chan.send("10 SECONDS TO JOIN")
        await asyncio.sleep(10)
        canJoin = False
        await chan.send("NO LONGER CAN JOIN")

        await chan.send(fighterIDs)

        numEms = random.random() * 2 + 1
        totEms = []
        for i in range(int(numEms)):
            totEms.append(Encounter()) #0, i, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, False, False
        chan.send(totEms)

        fighters = []
        for ids in fighterIDs:
            fighters.append(_raccoonArray[ids])
        chan.send(fighters)

        for item in totEms:
            item.STAT_calculator(0, fighters)

        await client.get_channel(901363239605116989).send("ready for next boss")
        inFight = False




    def addPlayer(name, author):
        read()
        xp = getMessages(author)
        if name == "swordsman":
            _raccoonArray[author] = Swordsman(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 35, 3, False, False, 0)

        if name == "tank":
            _raccoonArray[author] = Tank(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 35, 1, False, False, 0)
        if name == "mage":
            _raccoonArray[author] = Mage(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 35, 2, False, False, 0)
        if name == "archer":
            _raccoonArray[author] = ArcGun(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 35, 5, False, False, 0)

        if name == "healer":
            _raccoonArray[author] = Healer(1, author, 0, 0, 0, 0, 0,
                                            0, 0, 0, xp, 0, 35, 2, False, False, 0)
        w = open("saves.txt", "a")
        w.write("{" + str(author) + ":" + str(_raccoonArray[author]) + "}\n")

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
                addPlayer("swordsman", message.author.id)

            elif msg[1] == "tank":
                addPlayer("tank", message.author.id)


            elif msg[1] == "mage":
                addPlayer("mage", message.author.id)


            elif msg[1] == "healer":
                addPlayer("healer", message.author.id)


            elif msg[1] == "archer":
                addPlayer("archer", message.author.id)

            else:
                await message.channel.send('Pick one of the right classes')
                return
            await message.add_reaction('\N{THUMBS UP SIGN}')
        else:
            await message.channel.send("you already made a raccoon foulle")

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
        await message.channel.send(_raccoonArray[message.author.id].get_stats())

    if msg[0] == ".join" and not message.author.id in fighterIDs:
        if(not isPlaying(message.author.id)):
            message.channel.send("You must have a raccon to play!")
            return
        addFighter(message.author.id)
        await message.add_reaction('\N{THUMBS UP SIGN}')


    if msg[0] == ".startBattle" and admin:
        await startFight()

    #if msg[0] == ".startBoss" and admin:
        #startBossFight()

    #if msg[0] == ".attack" and players[message.author.id].Attack:
        #reduce health
        #await message.channel.send(str(enemy.name) + "has taken {} damage!".format(damage))

TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)
