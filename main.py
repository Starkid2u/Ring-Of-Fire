#!/usr/bin/env/str python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
global message_counter

with open("tokenfile", "r") as tokenfile:
    token=tokenfile.read()

my_id = 472465416019771392
client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

message_counter = 0
@client.event
async def on_message(message):

    rof_armour = discord.utils.get(message.guild.roles, id = 747465352841134190)

    if message.channel.category.id == 736788095667666985:
        return
    if message.author.bot:
        return
    global message_counter
    message_counter += 1
    if message_counter == 15:
        await message.channel.send("buhnuhn")
        print (f'sending buhnuhn to {message.channel.name} in {message.guild.name}')
        message_counter = 0
    
    if not (message.author.id == my_id):
        return

    if message.content.startswith('ring attack'):
        await message.channel.send('BUHNUHNUHNUHNUHNUHNUHNUHN!')
        print(f'attacking {message.mentions[0]}')

    if message.content.startswith('ring armor'):
        await message.author.add_roles(rof_armour, reason="armoured")
        asyncio.sleep(60)
        await message.author.remove_roles(rof_armour, reason="armoured")


client.run(token)