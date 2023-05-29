import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import datetime
import json, random
with open("./data/strings.json","r",encoding="utf-8") as string_data:
    strings=json.load(string_data)  

class BotInfo(Cog_Extension):
    @commands.hybrid_command(name="ping",pass_context=True,description="Send My Ping")
    async def ping(self,ctx:commands.Context):
        print(datetime.datetime.now()-ctx.message.created_at())
        await ctx.send(f"bot.latency= {round(self.bot.latency*1000)}ms")
        return

    @commands.hybrid_command(name="github",description=f"My GitHub Link")
    async def github_link(self,ctx):
        await ctx.reply(strings["GithubLink"])
        return 

    """ @commands.hybrid_command("help",pass_context=True,discription=strings["bot_name"]+" 使用指南")
    async def help(self,ctx):
        help_string="Commands\n"
        ctx.context
        for cog in self.bot.cogs:
            if cog.lower() == input[0].lower():
                    # making title - getting description from doc-string below class
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=discord.Color.green())
                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    # found cog - breaking loop
                    break
        return"""

async def setup(bot):
    await bot.add_cog(BotInfo(bot))