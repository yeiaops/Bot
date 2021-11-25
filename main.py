import nextcord
import datetime

client = nextcord.Client()

@client.event
async def on_ready():
    now = datetime.datetime.now()
    print("Bot is Online")
    print("Discord BOT NAME:" + client.user.name)
    print("Discord BOT ID:" + str(client.user.id))
    print("Login Time:"+str(datetime.datetime.today()))
    print("Discord.py Version:" + str(nextcord.__version__))
    s = len(client.guilds)
    print('------')
    await client.change_presence(status=nextcord.Status.online, activity=discord.Game("Active on {} servers".format(s)))



@client.event
async def on_message(message):
    if message.author.bot:
        return None
    msg = message.content #msg == "" or message.content == ""

    
    if msg == "!ping":
        await message.channel.send("pong")
      
client.run("Your Token")
