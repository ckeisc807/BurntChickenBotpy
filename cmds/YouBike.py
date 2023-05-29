import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from classes.Time import Time
from classes.YouBikeSearcher import YouBikeSearcher, YouBikeStation
from classes.City import City
import asyncio, json
table="""
剩餘YouBike
  | 剩餘空車架
  |   | 版本
  |   | | 站點名稱
"""
with open("./data/strings.json","r",encoding="utf-8") as string_data:
    strings=json.load(string_data)
searcher=YouBikeSearcher(limit=50)
station=YouBikeStation()
class YouBike(Cog_Extension):
    @commands.hybrid_command(name="youbike",description="get youbike information")
    async def youbike_name(self,ctx,city:City,name:str):
        await ctx.defer()
        string=await searcher.name_get(city.value,name)+f"\n資料來源https://tdx.transportdata.tw/\n`{Time()}`"
        if(len(string)>=2000): await ctx.reply("超出discord長度限制")
        await ctx.reply(string)
        return 
    
    @commands.hybrid_command(name="youbike_source")
    async def youbike_source(self,ctx:commands.Context):
        with open("./data/pictures/tdxlogo.png","rb") as pic:
            picture=discord.File(pic)
            await ctx.reply(file=picture,content=f"資料來源:{strings['TDXLink']}")
    """ @commands.hybrid_command(name="add-common",description="add common used youbike station to your list")
    async def add_common(ctx,id_name):
        return """



async def setup(bot):
    await bot.add_cog(YouBike(bot))