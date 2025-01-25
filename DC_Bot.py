import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

name = None
did_ask_for_name = False
greeting = False

@bot.event
async def on_message(msg):
  global name, did_ask_for_name, greeting
  
  if msg.author == bot.user:
    return
    
  print('[New message]', msg.content)
  
  if did_ask_for_name:
    name = msg.content

  if not name:
    did_ask_for_name = True
    await msg.channel.send('Hey, ich kenne deinen Namen noch nicht. Wie heißt du?')
    
  else:
    if not greeting:
      await msg.channel.send('Hallo ' + name)
      greeting = True
    

  if msg.content.startswith('Wie geht es dir?'):
    await msg.channel.send('Joa ganz gut, danke für deine Frage!')
  
  if "wie" in msg.content or "Wie" in msg.content:
    await msg.channel.send('Bei Fragen dieser Art, kannst du dich gern an meinen Entwickler wenden <3')

  if "Warum" in msg.content or "warum" in msg.content:
    await msg.channel.send('Weil ich dich liebe <3')
  

#damit Token nicht einsehbar ist (Secret)       
bot.run(os.environ['DC_Token'])
