"""
Another empty extension
"""

from nextcord.ext import commands

from main import CustomBot


class EmptyCog2(commands.Cog):
    """
    This is an Empty cog to just have more loaded for testing of internal things
    """

    def __init__(self, client: CustomBot):
        self.client: CustomBot = client


def setup(client) -> None:
    """
    Setup function to add the cog to the client
    :param client: the client
    :return: None
    """
    client.add_cog(EmptyCog2(client))
