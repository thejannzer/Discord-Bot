#used replit.com (MyDCBot)
import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

name = None
did_ask_for_name = False

@bot.event
async def on_message(msg):
  global name, did_ask_for_name
  if msg.author == bot.user:
    return
  print('[New message]', msg.content)
  if did_ask_for_name:
    name = msg.content

  if not name:
    did_ask_for_name = True
    await msg.channel.send('Hey, ich kenne deinen Namen noch nicht. Wie heißt du?')

  else:
    await msg.channel.send('Hallo ' + name)


#damit Token nicht einsehbar ist (Secret)       
bot.run(os.environ['DC_Token'])
