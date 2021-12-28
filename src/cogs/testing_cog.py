import nextcord
from nextcord.ext import commands

from main import CustomBot


class DebugCog(commands.Cog):
	def __init__(self, client: CustomBot):
		self.client: CustomBot = client

	@commands.command()
	async def _debug(self, ctx: commands.Context) -> None:
		return


def setup(client: CustomBot):
	client.add_cog(DebugCog(client))
