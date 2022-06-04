import discum
import json
from dhooks import Webhook, Embed
from discord.ext import commands
import asyncio
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
user_token = config["settings"]["user_token"]
bot_token = config["settings"]["bot_token"]


async def send_embed(embed_fields, ctx, error=None):
    embed = Embed(
        title=embed_fields[3]['name'] + ' ' + embed_fields[3]['value'],
        type='rich',
        color=3066993
    )

    if error is not None:
        embed.add_field(name=embed_fields[7]['name'], value=error[1]['fields'][0]['value'])  # ⚔️Атака:
        embed.add_field(name=embed_fields[8]['name'], value=error[2]['fields'][0]['value'])  # 🛡️Защита:
        ...
    else:
        embed.add_field(name=embed_fields[7]['name'], value=embed_fields[7]['value'])  # ⚔️Атака:
        embed.add_field(name=embed_fields[8]['name'], value=embed_fields[8]['value'])  # 🛡️Защита:
    embed.add_field(name=embed_fields[9]['name'], value=embed_fields[9]['value'])  # Результат
    embed.add_field(name=embed_fields[10]['name'], value=embed_fields[10]['value'])  # MVP
    embed.add_field(name=embed_fields[11]['name'], value=embed_fields[11]['value'])  # Значение
    embed.add_field(name=embed_fields[12]['name'], value=embed_fields[12]['value'])  # Никнейм
    await ctx.send(embed=embed)


async def get_channel(channelID, ctx):
    token = user_token
    bot = discum.Client(token=token, log=False)
    s = bot.getMessages(channelID=channelID).text
    mess = json.loads(s)
    if len(mess[0]['embeds']) == 1:
        embed_fields = mess[0]['embeds'][0]['fields']
        if len(embed_fields) == 9:
            await ctx.send("Результатов нет")
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=1)
        else:
            print(mess[0])
            await send_embed(embed_fields, ctx)
    elif len(mess[0]['embeds']) == 3:
        embed_fields = mess[0]['embeds'][0]['fields']
        if len(embed_fields) == 9:
            await ctx.send("Результатов нет")
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=1)
        else:
            print(mess[0])
            await send_embed(embed_fields, ctx, error=mess[0]['embeds'])


def main1(channelID, messageID):
    token = user_token
    bot = discum.Client(token=token, log=False)

    s = bot.getMessage(channelID, messageID).text
    mess = json.loads(s)
    embed_fields = mess[0]['embeds'][0]['fields']
    if len(embed_fields) == 9:
        print("Результатов нет")
    else:
        print(mess[0])
        send_embed(embed_fields)


if __name__ == '__main__':
    data = {
        'dt_cpt': '690778601905324052',
        'dt_biz': '690778600202305557',
        'str_cpt': '865675392588709908',
        'str_biz': '865676617141846036',
        'vv_cpt': '865683470616887368',
        'vv_biz': '865683628721963018',
        'bb_cpt': '862081859295117363',
        'bb_biz': '862081945957564426',
        'insquad_cpt': '865681207605985300',
        'insquad_biz': '865681253092163594',
        'sunrise_cpt': '690796395082547211',
        'sunrise_biz': '690796370055004191',
        'rainbow_cpt': '697534270163648622',
        'rainbow_biz': '697533926910066688',
        'richman_cpt': '701558951183122462',
        'richman_biz': '701558900708868148',
        'eclipse_cpt': '865678009242746890',
        'eclipse_biz': '865678137197985812',
        'lamesa_cpt': '714492912439787660',
        'lamesa_biz': '714492644230693657',
        'burton_cpt': '899405591674515506',
        'burton_biz': '899405616206979093',
        'rockford_cpt': '905190786667262012',
        'rockford_biz': '905202554932191282',
        'alta_cpt': '940309241342869534',
        'alta_biz': '940309018029752376'
    }

    client = commands.Bot(command_prefix='.')
    client.remove_command('help')


    @client.event
    async def on_ready():
        print("bot started")


    @client.command(pass_context=True)
    async def help(ctx):
        embed = Embed(
            title='Навигация по командам',
            # type='rich',
            color=3066993,
        )
        embed.add_field(name='.get server_cpt', value='Получить информацию по последнему капту')
        embed.add_field(name='.get server_biz', value='Получить информацию по последнему бизвару')
        servers = ''
        serv = []
        for k, v in data.items():
            s1 = k.split('_')[0]
            if s1 in serv:
                ...
            else:
                serv.append(s1)
                servers += s1 + '\n'
        embed.add_field(name='Список серверов', value=str(servers))
        await ctx.send(embed=embed)


    @client.command(pass_context=True)
    async def get(ctx, arg, amount=1):
        await ctx.channel.purge(limit=amount)
        if arg in data.keys():
            await get_channel(data[arg], ctx)
        else:
            print('no channel')


    @client.command(pass_context=True)
    async def get_mes(ctx, arg, amount=1):
        await ctx.channel.purge(limit=amount)
        print(arg)
        chan = arg.split('_')[0]
        mess = arg.split('_')[1]
        main1(chan, mess)



    client.run(bot_token)
