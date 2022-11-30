# ^(\s)*$\n (detecta linhas em branco)
import discord
import random
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = discord.Client()
client = commands.Bot(command_prefix= ".", case_insensitive = True)
@client.event
async def on_ready():
    print("logado {0.user}".format(client))
@client.command( )
async def ola(ctx):
    await ctx.send(f"Ola {ctx.author}")
@client.command()
async def dado(ctx,num : int ,ap:int):
    #ap é o nivel da perícia ( limite 15 --nao mudar) (Calculos internos)
    NS = random.randint(1,int(num))
    SB = int(ap/3)    #taxa sucesso bom (um terço no nivel da pericia)
    SE = int( ap/5)  # taxa sucesso extremo ( um quinto do nivel da pericia)
    TD = 14+SE          # taxa de desastre
    await ctx.send(f"[ {NS} ]")
    if NS <= SE:
        await ctx.send("Sucesso extremo")
    elif NS <= SB:
        await ctx.send("Sucesso Bom")
    elif NS <= ap:
        await ctx.send("Sucesso Normal")
        # se o numero q cair no dado for menor ou igual que a taxa do sucesso normal é um sucesso normal
    elif ap <  NS <= TD:
        await ctx.send ("Fracasso")
# se o dado caiu  maior que o nivel da pericia e (menor ou igual) a taxa de desastre é um fracasso normal
    elif NS > TD:
        await ctx.send("Desastre")
        #se o dado caiu maior que a taxa de desaste foi um desastre
    else:
        await ctx.send("error")
@client.command()
async def escolha(ctx, choices: str):
    await ctx.send(random.choice(choices))
@client.command()
async def roll(ctx, num ):
    dad= random.randint(1,int(num))
    await ctx.send(f' O Dado caiu em: {dad}')
@client.command()
async def menu(ctx):
        menu = discord.Embed(
        title = " ",
        description = "Pistola",
        colour = 11837242,
        )
        menu.set_thumbnail(url="https://media.discordapp.net/attachments/926060881584988200/926352161317740594/e69f2a62717116424a2f28c7b0a29023.jpg")
        menu.set_author(name=" Desert Eagle", icon_url= "https://media.discordapp.net/attachments/926060881584988200/927638993200369774/Screenshot_20220103-160601.jpg")
        msg= await ctx.send(embed=menu)
        await msg.add_reaction("1️⃣")
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
