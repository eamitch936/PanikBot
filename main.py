import discord
import os
import boto3

from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents)