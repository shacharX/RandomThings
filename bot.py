
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    print('RN is online!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! oh you want your ping? ok: {round(client.latency * 1000)}ms')

@client.command()
async def hello(ctx):
    await ctx.send('he...llo?')

@client.command()
async def server(ctx):
    await ctx.send('The Discord of my maker is this: https://discord.gg/yeaMQUt')

@client.command()
async def whomadeyou(ctx):
    await ctx.send('The Holy Arilbot!')

@client.command()
async def meow(ctx):
    await ctx.send('MEOW MEOW IM A CAT')

@client.command()
async def woof(ctx):
    await ctx.send('I cant say that. try #meow')

@client.command()
async def name(ctx):
    await ctx.send('my name is RN or RandomThings!')

@client.command()
async def dingdong(ctx):
    await ctx.send('you wired guy you know?')

@client.command()
async def something(ctx):
    await ctx.send('Fan Fact: meow')

@client.command()
async def HelloWorld(ctx):
    await ctx.send('You trying to use my maker custom status!?!?')

@client.command()
async def no(ctx):
    await ctx.send('yes')

@client.command()
async def yes(ctx):
    await ctx.send('no')

@client.command()
async def minecraft(ctx):
    await ctx.send('you want to play?')

@client.command()
async def youRN(ctx):
    await ctx.send('i think')

@client.command()
async def youstupid(ctx):
    await ctx.send('you worse')

@client.command()
async def stop(ctx):
    await ctx.send('start')

@client.command()
async def meow2(ctx):
    await ctx.send('MEOW2')

client.run('NzYwNTc5NjEwMjY1MTI0ODg1.X3OG9Q.rNI_o01Zj655FCccwJhG1aUL47g')