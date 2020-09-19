#!/usr/bin/env/str python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
global message_counter
import random

with open("tokenfile", "r") as tokenfile:
    token=tokenfile.read()

my_id = 542476575875137538
client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

armourcooldown = 0
futureburncooldown = 0
futureburn = 0
message_counter = 0
@client.event
async def on_message(message):
    # linking status
    standowner = discord.utils.get(message.guild.members, id = my_id)
    try:
        if standowner.activity.name == "Spotify":
            await client.change_presence(status=standowner.status, activity=discord.Activity(name=standowner.activity.name, type=discord.ActivityType.listening))
    except AttributeError:
        await client.change_presence(status=standowner.status, activity=standowner.activity)

    maxhealth = discord.utils.get(message.guild.roles, id = 714534974916919349)
    health9 = discord.utils.get(message.guild.roles, id = 714535185273847871)
    health8 = discord.utils.get(message.guild.roles, id = 714535298729640047)
    health7 = discord.utils.get(message.guild.roles, id = 714535324759621712)
    health6 = discord.utils.get(message.guild.roles, id = 714535348046266449)
    health5 = discord.utils.get(message.guild.roles, id = 714535379675644054)
    health4 = discord.utils.get(message.guild.roles, id = 714535405843775518)
    health3 = discord.utils.get(message.guild.roles, id = 714535436143558788)
    health2 = discord.utils.get(message.guild.roles, id = 714535460860330066)
    health1 = discord.utils.get(message.guild.roles, id = 714535481928319016)
    dead = discord.utils.get(message.guild.roles, id = 714535509279637525)
    rof_armour = discord.utils.get(message.guild.roles, id = 747465352841134190)

    #linking status
    standowner = discord.utils.get(message.guild.members, id = my_id)
    playing = standowner.activity
    await client.change_presence(status=standowner.status, activity=playing)
    
    if message.channel.category.id == 736788095667666985:
        return
    if message.author.bot:
        return
    global message_counter
    message_counter += 1
    if message_counter == 15:
        try:
            await message.channel.send("buhnuhn")
            print (f'sending buhnuhn to {message.channel.name} in {message.guild.name}')
            message_counter = 0
        except discord.errors.Forbidden:
            print(f"i cannot talk in {message.channel.name}")
            message_counter = 14

    if message.content.startswith('ring attack'):
        if not (message.author.id == my_id):
           return
        await message.channel.send('BUHNUHNUHNUHNUHNUHNUHNUHN!')
        print(f'attacking {message.mentions[0]}')

    global armourcooldown
    if message.content.startswith("ring armor"):
        if armourcooldown == 1:
            return
        if not (message.author.id == my_id):
            return
        await message.author.add_roles(rof_armour, reason="armoured")
        armourcooldown = 1
        await asyncio.sleep(60)
        await message.author.remove_roles(rof_armour, reason="armoured")
        await asyncio.sleep(20)
        armourcooldown = 0

    global futureburncooldown
    global futureburn
    if message.content.startswith("future burn"):
        if futureburncooldown == 1:
            return
        if message.author.id != my_id:
            return
        futureburn = random.randrange(30, 120, 1)
        print(f"attacking {message.mentions[0].name} in {futureburn} seconds")
        await message.delete()
        await asyncio.sleep(futureburn)
        if futureburn in range(30, 60): #1 damage
            futureburn = 1
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health9,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health8,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health7,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
        if futureburn in range(61, 90): #2 damage
            futureburn = 2
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health8,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health7,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
        if futureburn in range(91, 120): #3 damage
            futureburn = 3
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health7,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
        await message.channel.send(f"{message.mentions[0].mention} you were attacked for {futureburn} damage")
        futureburncooldown = 1
        await asyncio.sleep(10)
        futureburncooldown = 0

@client.event
async def on_member_update(before, after):
    if after.id == my_id:
        try:
            if after.activity.name == "Spotify":
                await client.change_presence(status=after.status, activity=discord.Activity(name=after.activity.name, type=discord.ActivityType.listening))
        except AttributeError:
            await client.change_presence(status=after.status, activity=after.activity)

client.run(token)