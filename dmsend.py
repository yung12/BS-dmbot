import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('흠샵 서버관리중')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    await asyncio.sleep(8)
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="흠샵.com", value=msg, inline=True)
                        embed.set_footer(text="HMM SHOP공지")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzUzOTkxNjYwMTczNTI1MTIy.X1uPdA.PD4SgIaZBGtFQUd7U-vn5VH445g')
