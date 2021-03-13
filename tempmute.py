import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class DiscordModule(commands.Cog, name="TempMute"):
    @commands.command()
    @has_permissions(ban_members=True)
    async def TempMute(self, ctx, member: discord.Member=None, time: int):
        if not member:
            embed = discord.embed(title='TempMute', Description='No person mentioned, please mention a member of this server')
            await ctx.send(embed=embed)
        if time == '0':
            embed = discord.embed(title='TempMute', description='Please specify a time.')
            await ctx.send(embed=embed)
