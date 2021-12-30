"""
This is supposed to have no entry point
"""

from nextcord.ext import commands

from main import CustomBot


class NoEntryPointExtension(commands.Cog):
    """
    A cog without an entry point
    """

    def __init__(self, client: CustomBot):
        self.client: CustomBot = client
