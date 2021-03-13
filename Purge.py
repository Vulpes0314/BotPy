import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class DiscordModule(commands.Cog, name="Ticket System"):
    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        Author = ctx.author.name
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(title='Purge Messages', description=f'Purged {limit} messages.', colour='3066993')
        await ctx.send(embed=embed, delete_after=5)
        print('Embed has been sent')
        await asyncio.sleep(5)
        await ctx.message.delete


    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title='Purge Messages', description="You don't have permissions to purge messages. ", colour='15158332')
            await ctx.send(embed=embed)
