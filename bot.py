import discord
import random
from bot_mantik import gen_pass 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



def yazi_tura_at():
    return random.choice(["Yazı!", "Tura!"])

def rastgele_emoji():
    emojiler = ["😀", "🚀", "🌟", "🍕", "🎮", "💻", "⛏️"] 
    return random.choice(emojiler)



@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
        
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
        
    elif message.content.startswith('$yazitura'):
        await message.channel.send(yazi_tura_at())
        
    elif message.content.startswith('$emoji'):
        await message.channel.send(rastgele_emoji())
        
    elif message.content.startswith('$sifre'):

        await message.channel.send(f"Senin için şifre: {gen_pass(10)}")
        
    else:

        await message.channel.send(message.content)


client.run("MTQ3MjI1ODY4OTQ5Mzg5NzI5OA.GNW9_B.tEwY1eQNNMiVd4ya_jdMVr_3Zl9ezHzF6x3sag")
