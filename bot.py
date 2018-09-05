import discord
from discord import Game
from discord.ext.commands import Bot




prefix = ("$")
bingBong = 'NDgxMjc1OTUwMjQ0Mjk4NzYz.Dlz_iA.1JPBmSHDnbrDpEgWoOFRoaq0Fd4'
#put da token above uwu


client = Bot(command_prefix=prefix)

@client.command(name='wiki',description="Use $wiki followed by a space, then your search query to have the bot find the wikipedia article for your query.",brief="Search for a wikipedia page", pass_context=True)
async def wikiSearch(query):
	fun = query.message.content[6:]
	funboy = fun.replace(" ", "_")
	link="https://en.wikipedia.org/wiki/" + funboy
	await client.say(link)
	


    


@client.event
async def on_ready():
    print('Lesgeddit')

client.run(bingBong)