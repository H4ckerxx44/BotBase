"""
A failing extension
"""

from nextcord.ext import commands

from main import CustomBot


class FailingExtension(commands.Cog):
    """
    This extension is supposed to fail
    """

    def __init__(self, bot: CustomBot):
        self.bot: CustomBot = bot
        self.abc: int = "Hello!"


def setup(bot):
    """
    Setup function to add the cog to the bot
    :param bot: the bot
    :return: None
    """
    bot.add_cog(FailingExtension(bot))
