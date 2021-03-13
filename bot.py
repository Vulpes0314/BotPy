import discord
import time
from discord.ext import commands


# Import Modules
import Ticket
import Purge

bot = commands.Bot(command_prefix='.')

# Register Modules
Modules = [Ticket.DiscordModule,
            Purge.DiscordModule,
            ]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Joey for education"))
    print('Bot is ready')

for cog in Modules:
    bot.add_cog(cog(bot))

bot.run('Njg4MTQ5MzMwODc5OTcxNDE4.XxWsJA.fgHvIPkaRmzOfBQqoDmGPgq0SCI')
