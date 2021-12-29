import nextcord
from nextcord.ext import commands

from main import CustomBot


class Test(commands.Cog):
	def __init__(self, client: CustomBot):
		self.client: CustomBot = client
		self.error_color = nextcord.Color.red()

	@commands.command(aliases=["l"], hidden=True)
	@commands.is_owner()
	async def load(self, ctx: commands.Context, *extensions) -> None:
		# TODO: add functionality with internals in mind
		return

	@commands.command(aliases=["ul"], hidden=True)
	@commands.is_owner()
	async def unload(self, ctx: commands.Context, *extensions) -> None:
		# TODO: add functionality with internals in mind
		return

	@commands.command(aliases=["rl"], hidden=True)
	@commands.is_owner()
	async def reload(self, ctx: commands.Context, *extensions) -> None:
		# TODO: add functionality with internals in mind
		return

	@commands.command()
	async def test0(self, ctx):
		await ctx.send("hi")

	@commands.command()
	async def test1(self, ctx, a):
		await ctx.send(f"hi {a}")

	@commands.command()
	async def test2(self, ctx, a, b):
		await ctx.send(f"hi {a} {b}")

	@commands.command()
	async def test3(self, ctx, a, b, c):
		await ctx.send("hallo")
		await ctx.send(f"hi {a} {b} {c}", delete_after=15.0)
		await ctx.send("hallo")

	@commands.is_owner()
	@commands.command()
	async def yeet(self, ctx):
		await ctx.send(str(self.client.uptime()))

	@commands.command()
	async def channel_id(self, ctx, channel: nextcord.TextChannel):
		await ctx.send(channel.id)

	@commands.group()
	async def group_test(self, ctx: commands.Context):
		if not ctx.invoked_subcommand:
			await ctx.send("I am a group!")

	@group_test.command(name="a")
	async def group_test_a(self, ctx: commands.Context):
		await ctx.send("I am a sub command of group `group_test`")


def setup(client):
	client.add_cog(Test(client))