"""
This is supposed to have no entry point
"""

from nextcord.ext import commands

from main import CustomBot


class NoEntryPointExtension(commands.Cog):
    """
    A cog without an entry point
    """

    def __init__(self, bot: CustomBot):
        """
        Setup function to add the cog to the bot
        :param bot: the bot
        :return: None
        """
        self.bot: CustomBot = bot
