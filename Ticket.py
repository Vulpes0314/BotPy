import discord
from discord.ext import commands
from discord.ext.commands import has_permissions



class DiscordModule(commands.Cog, name="Ticket System"):
    @commands.command()
    async def ticket(self, ctx, *, arg = ""):
        Author = ctx.author.name
        Discriminator = ctx.author.discriminator

        # Check if the args are empty and giving the right response
        if arg == "":
            print(Author + '#' + Discriminator + 'created a ticket')
            embed = discord.Embed(title='Ticket Creation',description='Ticket is being created, ' + Author, colour=1752220)
            await ctx.channel.send(embed=embed)
        else:
            print(Author + '#' + Discriminator + ' created a ticket, named: ' + arg)
            embed = discord.Embed(title='Ticket Creation',description='Ticket named: ' + '**' + arg + '**' + ' is being created, ' + Author, colour=1752220)
            await ctx.channel.send(embed=embed)

        # Check if there already is a category named "Tickets", if not it will make one
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False, view_channel=False)}
        category = discord.utils.get(ctx.guild.channels, name="Tickets") or await ctx.guild.create_category('Tickets', overwrites=overwrites)

        # Check if the args are empty and creating the right text channel name
        if arg == "":
            overwrites = {
                ctx.author: discord.PermissionOverwrite(read_messages=True, view_channel=True, send_messages=True, manage_channels=True),
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False, view_channel=False, read_messages=False, manage_channels=False)
            }
            newchannel = await ctx.guild.create_text_channel(Author + '-' + Discriminator, category=category, overwrites=overwrites)
        else:
            overwrites = {
                ctx.author: discord.PermissionOverwrite(read_messages=True, view_channel=True, send_messages=True, manage_channels=True),
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False, view_channel=False, read_messages=False, manage_channels=False)
            }
            newchannel = await ctx.guild.create_text_channel(arg + "-" + Author, category=category, overwrites=overwrites)
        await toggle_perms(ctx.author, newchannel, permission=True)

    async def toggle_perms(member, channel, permission=False):
        newperms = discord.PermissionOverwrite()
        newperms.read_messages = permission
        newperms.manage_channels = permission
        await channel.set_permissions(member, overwrite=newperms)

    @commands.command()
    @has_permissions(manage_channels=True)
    async def close(self, ctx):
        channel = ctx.message.channel
        category = channel.category
        author = ctx.message.author

        # Check if the channel is in the category named Tickets
        if category.name == "Tickets":
            await channel.delete()
