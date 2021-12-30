"""
A failing extension
"""

from nextcord.ext import commands

from main import CustomBot


class FailingExtension(commands.Cog):
    """
    This extension is supposed to fail
    """

    def __init__(self, client: CustomBot):
        self.client: CustomBot = client
        self.abc: int = "Hello!"


def setup(client):
    """
    Setup function to add the cog to the client
    :param client: the client
    :return: None
    """
    client.add_cog(FailingExtension(client))
