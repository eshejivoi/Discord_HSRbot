from email import message

from discord.types import embed
from model import detect_cuteNoRcute
import discord
import requests
from discord import Embeds
import random
import os
from discord.ext import commands


intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


commands_list = ['hello', 'heh', 'secretURL', 'kawaii', 'helps', 'check']


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def secretURL(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на кота",
        url='https://imgur.com/gallery/eslTP',
    )
    await ctx.send(embed=embed)


@bot.command()
async def kawaii(ctx):
    await ctx.send(f'Пользователь, я считаю вы очень милы :з')


@bot.command()
async def helps(ctx):
    await ctx.send(commands_list)



@bot.command()
async def mem(ctx):
    with open('imeges/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


def get_duck_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def fox(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def rare(ctx):
    with open('imeges/mem1.jpg', 'rb') as f:
        picture = discord.File(f)

#@bot.command()
#async def caption(ctx, caption_text):
#    if ctx.message.attachments:
#        image_url = ctx.message.attachments[0].url
##
#
#@bot.command()
#async def send_image(ctx):
#    embed = discord.Embed(title="Your attached image")
#    if len(message.attachments):
#        embed.set_image(url=ctx.message.attachments[0].url)
#    await ctx.send(embed=embed)
#
#@bot.command()
#async def readURL(ctx):
#    attachment = ctx.message.attachments[0]
#    print(attachment.url)
#
#@bot.command()
#async def save(ctx):
#    for attach in ctx.message.attachments:
#        await attach.save(f"./{attach.filename}")


#@bot.command()
#async def check(ctx):
#    if ctx(message.attachments):
#        for i in ctx.message.attachments:
#            embed.set_image(url=ctx.message.attachments[0].url)
#            await save()
#            await ctx.send(detect_cuteNoRcute(model_path="./keras_model.h5", lable_path="./labels.txt", image_path="./{i.filname}"))
#    else:
#        await ctx.send("картиночка где? :3")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(detect_cuteNoRcute(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Вы забыли загрузить картинку :(")

bot.run("MTE0OTAwODMwMjM4MzA1OTExNg.GMRFSc.QiXg2_6qJl2ZMwuFBhhYu1289ANBkytde9Hd7w")