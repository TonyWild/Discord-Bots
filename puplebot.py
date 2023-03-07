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
    if message.content == '퍼플이 안녕':
        await message.channel.send(f"{message.author.mention}도 안녕안녕~")


    message_token = message.content.split(' ')

    # 식당 랜덤 선택
    if message_token[0] == '!식당':
        # `!식당`
        if len(message_token) == 1:
            query = '어은동'
        # `!식당 궁동`
        else:
            query = message_token[1]

        await message.channel.send(f"{query}에 있는 식당을 무작위로 선택합니다.")

        rest = restaurant.choose_random(f'{query} 음식점')

        embed=discord.Embed(title="식당 랜덤 선택 결과", color=0x8621ca)
        embed.add_field(name="선택된 식당", value=rest['place_name'], inline=False)
        embed.add_field(name="주소", value=f"{rest['road_address_name']} ({rest['address_name']})", inline=False)
        embed.add_field(name="전화번호", value=rest['phone'], inline=False)
        embed.add_field(name="링크", value=rest['place_url'], inline=False)
        await message.channel.send(embed=embed)


client.run(TOKEN)


