import discord
import string
import random 
import time


token = "token"
now = datetime.datetime.now()
client = discord.Client()


@client.event
async def on_ready():
    print('logs: ')
	
def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars, k=size))


@client.event
async def on_message(message):
    if message.content.startswith("!crash"):
	for _ in range(10):
		await client.send_message(message.channel,
					  '\n'.join(map(
					    lambda k: f"https://discord.gift/{k}",
					    (id_generator() for _ in range(16))
					  )))
        	time.sleep(0.2)

	
client.run(token, bot=False)
