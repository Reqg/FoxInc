import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
from keep_alive import keep_alive


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name=' met vossen'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!Sollicitatie':
        await client.send_message(message.channel,'Je kunt via deze link gemakkelijk solliciteren: http://bit.ly/FoxSollicitatie')
    if message.content == '!Solliciteren':
        await client.send_message(message.channel,'Je kunt via deze link gemakkelijk solliciteren: http://bit.ly/FoxSollicitatie')
    if message.content == '!Twitter':
        await client.send_message(message.channel,'Via deze link komt u op onze twitter pagina terecht: https://twitter.com/FoxIncMT')
    if message.content == '!Winkels':
        await client.send_message(message.channel,':fox: **Fox Incorperated** :fox: \n \n :shirt:[Fox Clothes]:shirt: \n { Atlanta } X -400 Z -1770 \n \n :shirt:[Fox Clothes]:shirt: \n { Sunnyville } X 1195 Z 450 \n \n :shirt:[Fox Clothes]:shirt: \n { Downtown } X -280 Z -1200 \n \n :race_car: [Fox Circuit]:race_car: \n { Downtown } X 10 Z -2020 \n \n :fish:[Fox Fish]:fish: \n { DeKaap } X 1285 Z -540 \n \n :fish:[Fox Fish]:fish: \n { Atlanta } X -400 Z -1630 \n \n :office:[Fox Headquarters]:office: \n { Downtown } X -280 Z -1200')
    if message.content == '!Coords':
        await client.send_message(message.channel,':fox: **Fox Incorperated** :fox: \n \n :shirt:[Fox Clothes]:shirt: \n { Atlanta } X -400 Z -1770 \n \n :shirt:[Fox Clothes]:shirt: \n { Sunnyville } X 1195 Z 450 \n \n :shirt:[Fox Clothes]:shirt: \n { Downtown } X -280 Z -1200 \n \n :race_car: [Fox Circuit]:race_car: \n { Downtown } X 10 Z -2020 \n \n :fish:[Fox Fish]:fish: \n { DeKaap } X 1285 Z -540 \n \n :fish:[Fox Fish]:fish: \n { Atlanta } X -400 Z -1630 \n \n :office:[Fox Headquarters]:office: \n { Downtown } X -280 Z -1200')
    if message.content == '!Vos':
        await client.send_message(message.channel,'De vos (Vulpes vulpes) (ook wel gewone of rode vos genoemd) is een lid van de hondachtigen. De wetenschappelijke naam van de soort werd als Canis vulpes in 1758 gepubliceerd door Carl Linnaeus.')
    if message.content == '!Sinaasappel':
        await client.send_message(message.channel,'De sinaasappel (ook wel appelsien genoemd) is de vrucht van de sinaasappelboom (Citrus sinensis), die tot het geslacht Citrus behoort. De soort wordt ook wel zoete sinaasappel genoemd, om hem te onderscheiden van de zure of bittere sinaasappel (Citrus aurantium). De boom werd vroeger in koudere klimaatgebieden in een overwinteringsvertrek gehouden, dat daaraan de naam oranjerie ontleent.')
    if message.content == '!Oranje':
        await client.send_message(message.channel,'Oranje is een kleur die zich in het spectrum tussen rood en geel bevindt, bij golflengtes tussen 620 en 585 nanometer. De kleur kan dan ook door menging van geel en rood verkregen worden. In de (niet-wetenschappelijke) traditionele kleurenleer is het een secundaire hoofdkleur. De complementaire kleur is ultramarijnblauw.')
client.run('NTU4NzY1Nzk3MTk2MDM4MTQ0.D3bsXA.PoNKYgeQJ1Zugt3wJNXY3pnOboU')
