import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from spooknchill import random_movie
from makemelaugh import random_meme
from creepmeup import random_creepypasta
from dressmeup import random_costume
from trickortreat import random_candy, random_trick

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('!'),
    help_command = help_command
)
client = discord.Client()

@bot.command(name='spook_n_chill', help='Suggests you creepy movies for u to spook n chill.')
async def movie_embed(ctx):
    movie = random_movie()
    embed=discord.Embed(title=movie["title"], url=movie["link"], description=movie["desc"], color=discord.Color.orange())
    embed.set_image(url=movie["image"])
    await ctx.send(embed=embed)

@bot.command(name='make_me_laugh', help='Makes you laugh with creepy memes.')
async def meme_embed(ctx):
    meme = random_meme()
    embed=discord.Embed(title="Here's a creepy meme for your ugly laughter", color=discord.Color.green())
    embed.set_image(url=meme)
    await ctx.send(embed=embed)

@bot.command(name='creep_me_up', help='Sends some creepy pasta for you to creep up.')
async def creepypasta_embed(ctx):
    pasta = random_creepypasta()
    embed=discord.Embed(title=pasta["title"], description=pasta["story"], color=discord.Color.red())
    embed.set_image(url=pasta["link"])
    await ctx.send(embed=embed)

@bot.command(name='dress_me_up', help='Sends some great halloween costume ideas')
async def costume_embed(ctx):
    costume = random_costume()
    embed=discord.Embed(title=costume["title"], color=discord.Color.blue())
    embed.set_image(url=costume["image"])
    await ctx.send(embed=embed)

@bot.command(name='trick_or_treat', help='Play trick or treat with Pumpkin Head')
async def trick_or_treat_embed(ctx):
    choice = random.choice(["trick","treat", "treat", "treat"])
    if choice == "treat":
      candy = random_candy()
      embed=discord.Embed(title="Here's a treat for you!", color=discord.Color.purple())
      embed.set_image(url=candy)
    else:
      trick = random_trick()
      embed=discord.Embed(title="You tricked ME!", description=trick, color=discord.Color.purple())
    await ctx.send(embed=embed)

bot.run(TOKEN)