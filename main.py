#!/usr/bin/env python3
import os
import disnake
from disnake.ext import commands, tasks
import requests

bot = commands.InteractionBot()

@bot.event
async def on_ready():
    if not loop.is_running():
        loop.start()

@tasks.loop(seconds=5)
async def loop():
    try:
        result = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=myria&vs_currencies=USD&include_24hr_change=true").json()
        usd_value=result['myria']['usd']
        usd_change=result['myria']['usd_24h_change']
        await bot.change_presence(activity=disnake.Game(name=f'24h: {usd_change:.0f}%'))
        for guild in bot.guilds:
            await guild.me.edit(nick=f'MYRIA: ${usd_value:.5f}')
    except:
        print("error trying to get current value")

bot.run(os.getenv("BOT_TOKEN"))
