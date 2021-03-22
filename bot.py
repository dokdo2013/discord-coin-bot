import discord
from discord.ext import commands
import os
import yatchacha
import hangang
yt = yatchacha.yatchacha
hg = hangang.hangang

gm = discord.Game('!도움말')
app = commands.Bot(command_prefix='$', activity=gm)

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online)


@app.command()
async def 도움말(ctx):
    embed_도움말 = discord.Embed(title='도움말', description='현재 업비트 시세정보만 이용하실 수 있습니다', color=0x00ff00)
    embed_도움말.add_field(name='$업비트 {코인명}', value='사용예시 : $업비트 비트코인', inline=False)
    embed_도움말.add_field(name='$한강', value='사용예시 : $한강', inline=False)
    await ctx.send(embed=embed_도움말)

@app.command()
async def 업비트(ctx, name):
    if name == '':
        await ctx.send('형식에 맞게 입력해주세요 : $업비트 {코인명}')
    else:
        nowData = yt.get(name)
        if nowData[0] == -1:
            await ctx.send('검색 결과가 없습니다.')
        else:
            target_data = nowData[0]
            target_text = nowData[1]
            updown = nowData[2]
            target_title = nowData[3]
            if updown == 1:
                target_color = 0xff0000
            elif updown == -1:
                target_color = 0x0000ff
            else:
                target_color = 0xffffff
            embed_data = discord.Embed(title=target_title, description=target_text, color=target_color)
            for k, v in target_data.items():
                embed_data.add_field(name=k, value=v, inline=True)
            await ctx.send(embed=embed_data)

@app.command()
async def 한강(ctx):
    temperature, data, color = hg.openapi()
    if color == -1:
        await ctx.send('API 호출에 실패했습니다 ({})'.format(data))
    else:
        target_title = '한강수온 {}°C'.format(temperature)
        target_text = '측정 정보 : {} {}'.format(data[0], data[1])
        target_color = color
        embed_hg = discord.Embed(title=target_title, description=target_text, color=target_color)
        await ctx.send(embed=embed_hg)

@app.command()
async def 일봉(ctx, name):
    if name == '':
        await ctx.send('형식에 맞게 입력해주세요 : $일봉 {코인명}')
    else:
        dir = yt.chart(name, 'd')
        dirctory = os.path.dirname(__file__)
        file = discord.File(dirctory + "/" + dir)
        await ctx.send(file=file)

@app.command()
async def 분봉(ctx, name1 = '', name2 = ''):
    if name1 == '' or name2 == '':
        await ctx.send('형식에 맞게 입력해주세요 : $분봉 {코인명} {조회단위} (예시. $분봉 비트코인 1)')
    else:
        dir = yt.chart(name1, 'm', name2)
        dirctory = os.path.dirname(__file__)
        file = discord.File(dirctory + "/" + dir)
        await ctx.send(file=file)

@app.command()
async def 주봉(ctx, name):
    if name == '':
        await ctx.send('형식에 맞게 입력해주세요 : $주봉 {코인명}')
    else:
        dir = yt.chart(name, 'w')
        dirctory = os.path.dirname(__file__)
        file = discord.File(dirctory + "/" + dir)
        await ctx.send(file=file)

@app.command()
async def 월봉(ctx, name):
    if name == '':
        await ctx.send('형식에 맞게 입력해주세요 : $월봉 {코인명}')
    else:
        dir = yt.chart(name, 'mo')
        dirctory = os.path.dirname(__file__)
        file = discord.File(dirctory + "/" + dir)
        await ctx.send(file=file)


@app.command()
async def 버전(ctx):
    data = '버전 0.1.5 (분봉, 주봉, 월봉 기능 추가)'
    await ctx.send(data)

@app.command()
async def hellothisisverification(ctx):
    await ctx.send('현우#1000')
    
app.run('')
