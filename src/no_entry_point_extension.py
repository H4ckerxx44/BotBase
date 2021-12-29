import nextcord
from nextcord.ext import commands

from main import CustomBot


class NoEntryPointExtension(commands.Cog):
    def __init__(self, client: CustomBot):
        self.client: CustomBot = client
