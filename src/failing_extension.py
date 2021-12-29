import nextcord
from nextcord.ext import commands

from main import CustomBot


class FailingExtension(commands.Cog):
    def __init__(self, client: CustomBot):
        self.client: CustomBot = client
        self.a: int = "Hello!"


def setup(client):
    client.add_cog(FailingExtension(client))
