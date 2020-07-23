
    
import os
token = os.environ.get("TOKEN")

import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or

modulos = ["cogs.comando", "cogs.handler"]

client = AutoShardedBot(command_prefix="<@735610741368946748> ", case_insensitive=True)

client.remove_command("help")

@client.event
async def on_ready():
   print(f"{client.user.name} Foi iniciado em {len(client.guilds)} Servidores!")
   await client.change_presence(activity=discord.Streaming(name="Hello!", url='https://www.twitch.tv/123'))
   
if __name__ == "__main__":
   for modulo in modulos:
      client.load_extension(modulo)
      print(f"{modulo} Carregado")
        
client.run(token)