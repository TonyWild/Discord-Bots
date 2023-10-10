# Python 3.10.8
import os

import discord
from dotenv import load_dotenv

import restaurant
import minesweeper

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
    message_token = message.content.split(' ')
    if message.author == client.user:
        return

    # 퍼플이 인사
    if message.content == '퍼플이 안녕':
        await message.channel.send(f"{message.author.mention}도 안녕안녕~")

    # 식당 랜덤 선택
    if message_token[0] == '!식당':
        # `!식당`
        if len(message_token) == 1:
            query = '어은동'
        # `!식당 궁동`
        else:
            query = message_token[1]

        await message.channel.send(f"{query}에 있는 식당 10개를 무작위로 선택합니다.")
        rest_list = restaurant.choose_random(f'{query} 맛집')

        embed=discord.Embed(title='식당 랜덤 선택 결과', color=0x8621ca)
        for rest in rest_list:
            embed.add_field(name=rest['place_name'], value=rest['category_name'].split(' > ')[-1], inline=False)

        await message.channel.send(embed=embed)

    # 지뢰찾기
    if message_token[0] == '!지뢰찾기':
        colNum = None
        rowNum = None
        mineNum = None
        liar = False

        # '!지뢰찾기 초급' (뒤에 텍스트가 더 와도 상관이 없다)
        if message_token[1] == "초급":
            colNum, rowNum, mineNum = 9, 9, 10

        # '!지뢰찾기 중급' (뒤에 텍스트가 더 와도 상관이 없다)
        elif message_token[1] == "중급":
            colNum, rowNum, mineNum = 16, 16, 40

        # '!지뢰찾기 고급' (뒤에 텍스트가 더 와도 상관이 없다)
        elif message_token[1] == "고급":
            colNum, rowNum, mineNum = 30, 16, 99
        
        try:
            if message_token[2] == "라이어":
                liar = True
        except IndexError:
            pass

        await message.channel.send(f"지뢰는 총 {mineNum}개 있어요.")
        msg = minesweeper.createboard(colNum, rowNum, mineNum, liar)
        for i in range(rowNum):
            await message.channel.send("".join(msg[i]))
        await message.channel.send("보드가 완성되었습니다!")

client.run(TOKEN)