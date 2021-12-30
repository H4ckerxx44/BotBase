from nextcord.ext import commands

from main import CustomBot


class EmptyCog2(commands.Cog):
    def __init__(self, client: CustomBot):
        self.client: CustomBot = client


def setup(client):
    client.add_cog(EmptyCog2(client))
