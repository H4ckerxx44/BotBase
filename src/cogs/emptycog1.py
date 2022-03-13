"""
An empty extension
"""

from nextcord.ext import commands

from main import CustomBot


class EmptyCog1(commands.Cog):
    """
    This is an Empty cog to just have more loaded for testing of internal things
    """

    def __init__(self, bot: CustomBot):
        self.bot: CustomBot = bot


def setup(bot) -> None:
    """
    Setup function to add the cog to the bot
    :param bot: the bot
    :return: None
    """
    bot.add_cog(EmptyCog1(bot))
