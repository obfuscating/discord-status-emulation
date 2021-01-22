# imports
import discord, os, asyncio, pytz

from discord.ext import tasks, commands

# yes break discord tos
client = commands.Bot(
  self_bot=True,
  command_prefix='\\'
)


@client.event
async def on_connect():

  # just to give you the assurance it ran and your status is showing
  print('hi')
  print('running')

  # UNCOMMENT THESE BELOW BY REMOVING THE #
  # choose 1 to use (ONE AT A TIME) to emulate whatever status you want
  # playing, watching, listening, streaming

  #await client.change_presence(activity = discord.Activity(type=discord.ActivityType.playing, name = "put something here"))

  #await client.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name = "put something here"))

  #await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name = "put something here"))

  await client.change_presence(activity = discord.Streaming(name = 'put something here', url = "https://twitch.tv/music"))

client.run("your token", bot=False)
