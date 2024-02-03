import discord
from discord.ext import commands
from valve.rcon import RCON, RCONError

intents = discord.Intents.default()
intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

YOUR_USER_ID = 1234567890 # put your user id in discord
IP_SERVER = 'put your ip server'
PORT_SERVER = 12345 # put your server port
RCON_SERVER = 'put your rcon password'
BOT_TOKEN = 'put your discord bot token'

@bot.command(name="rcon")
async def rcon(ctx, *args):
    if ctx.author.id == YOUR_USER_ID:
        command = " ".join(*args)
        try:
            with RCON((IP_SERVER, PORT_SERVER), RCON_SERVER):
                result = rcon(command)
                if result != "":
                    await ctx.send(result)
                else:
                    await ctx.send("Command send, but not given result")
        except RCONError as e:
            print(e)
            await ctx.send("Connected to rcon not sucsesful!!!!")
    else:
        await ctx.send("You not have access to this command")

bot.run(BOT_TOKEN)