# Python 3.10.8
import os

import discord
from dotenv import load_dotenv

import restaurant

load_dotenv()
TOKEN = os.getenv('PUPLE_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 퍼플이 인사
    if message.content == "퍼플이 안녕":
        await message.channel.send(f"{message.author.mention}도 안녕안녕~")

    # 식당 랜덤 선택
    if message.content.startswith("!식당"):
        await message.channel.send(f"어은동에 있는 식당을 무작위로 선택합니다.")

        rest = restaurant.choose_random("어은동 음식점")

        embed=discord.Embed(title="식당 랜덤 선택 결과", color=0x8621ca)
        embed.add_field(name="선택된 식당", value=rest['place_name'], inline=False)
        embed.add_field(name="주소", value=f"{rest['road_address_name']} ({rest['address_name']})", inline=False)
        embed.add_field(name="전화번호", value=rest['phone'], inline=False)
        embed.add_field(name="링크", value=rest['place_url'], inline=False)
        await message.channel.send(embed=embed)


client.run(TOKEN)


