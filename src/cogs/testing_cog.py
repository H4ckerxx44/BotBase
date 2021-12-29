import nextcord
from nextcord.ext import commands

from main import CustomBot


class Test(commands.Cog):
    def __init__(self, client: CustomBot):
        self.client: CustomBot = client
        self.error_color = nextcord.Color.red()

    @commands.is_owner()
    @commands.command(aliases=["l"], hidden=True)
    async def load(self, ctx: commands.Context, *extensions) -> None:
        # TODO: add functionality with internals in mind
        return

    @commands.is_owner()
    @commands.command(aliases=["ul"], hidden=True)
    async def unload(self, ctx: commands.Context, *extensions) -> None:
        # TODO: add functionality with internals in mind
        return

    @commands.is_owner()
    @commands.command(aliases=["rl"], hidden=True)
    async def reload(self, ctx: commands.Context, *extensions) -> None:
        # TODO: add functionality with internals in mind
        return

    # Commands
    @commands.command()
    async def test0(self, ctx: commands.Context):
        await ctx.send("hi")

    @commands.command()
    async def test1(self, ctx: commands.Context, a):
        await ctx.send(f"{a=}")

    @commands.command()
    async def test2(self, ctx: commands.Context, a, b):
        await ctx.send(f"{a=} {b=}")

    @commands.command()
    async def test3(self, ctx: commands.Context, a, b, c):
        await ctx.send(f"{a=} {b=} {c=}")

    @commands.is_owner()
    @commands.command()
    async def not_owner(self, ctx: commands.Context):
        await ctx.send("If you see this you are the bot owner.")

    @commands.command()
    async def member_not_found(self, ctx: commands.Context, member: nextcord.Member):
        await ctx.send(str(member))

    @commands.has_role(731275569471422485)
    @commands.command()
    async def missing_role(self, ctx: commands.Context):
        await ctx.send("")

    @commands.command()
    async def bad_argument(self, ctx: commands.Context, a: int):
        await ctx.send(str(a))

    @commands.command()
    async def guild_not_found(self, ctx: commands.Context, guild: nextcord.Guild):
        await ctx.send(str(guild))

    @commands.command()
    async def too_many_arguments(self, ctx: commands.Context, a, b):
        await ctx.send(f"{a=}, {b=}")

    @commands.command()
    async def role_not_found(self, ctx: commands.Context, role: nextcord.Role):
        await ctx.send(str(role))

    @commands.command()
    async def message_not_found(self, ctx: commands.Context, message: nextcord.Message):
        await ctx.send(str(message))

    @commands.command()
    async def channel_not_found(self, ctx: commands.Context, channel):
        await ctx.send(str(channel))

    @commands.command()
    async def string_errors(self, ctx: commands.Context, *, text: str):
        await ctx.send(text)

    @commands.dm_only()
    @commands.command()
    async def private_message_only(self, ctx: commands.Context):
        await ctx.send("DM Only")

    @commands.guild_only()
    @commands.command()
    async def no_private_message(self, ctx: commands.Context):
        await ctx.send("Guild only")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def missing_permissions(self, ctx: commands.Context):
        await ctx.send("Admin only")

    @commands.bot_has_permissions(administrator=True)
    @commands.command()
    async def xbot_missing_permissions(self, ctx: commands.Context):
        await ctx.send("Bot admin only.")

    @commands.command()
    async def missing_any_role(self, ctx: commands.Context):
        await ctx.send("Missing any role.")

    @commands.command()
    async def xbot_missing_any_role(self, ctx: commands.Context):
        await ctx.send("Bot missing any role.")

    @commands.command()
    async def xbot_missing_role(self, ctx: commands.Context):
        await ctx.send("Bot missing role.")

    @commands.is_nsfw()
    @commands.command()
    async def nsfw_only(self, ctx: commands.Context):
        await ctx.send("NSFW only.")

    @commands.command(enabled=False)
    async def disabled_command(self, ctx: commands.Context):
        await ctx.send("Disabled command.")

    @commands.cooldown(1, 5)
    @commands.command()
    async def command_on_cooldown(self, ctx: commands.Context):
        await ctx.send("Command on cooldown.")

    @commands.command()
    async def extension_already_loaded(self, ctx: commands.Context):
        self.client.load_extension("jishaku")

    @commands.command()
    async def extension_not_loaded(self, ctx: commands.Context):
        self.client.unload_extension("jishaku")
        self.client.unload_extension("jishaku")

    @commands.command()
    async def extension_failed(self, ctx: commands.Context):
        self.client.load_extension("failing_extension")

    @commands.command()
    async def extension_not_found(self, ctx: commands.Context):
        self.client.load_extension("cogs.not_to_be_found")

    @commands.command()
    async def no_entry_point_error(self, ctx: commands.Context):
        self.client.load_extension("no_entry_point_extension")

    @commands.command()
    async def channel(self, ctx: commands.Context, channel: nextcord.TextChannel):
        await ctx.send(str(channel))

    @commands.command()
    async def member(self, ctx: commands.Context, member: nextcord.Member):
        await ctx.send(str(member))

    @commands.command()
    async def guild(self, ctx: commands.Context, guild: nextcord.Guild):
        await ctx.send(str(guild))

    @commands.command()
    async def message(self, ctx: commands.Context, message: nextcord.Message):
        await ctx.send(str(message))

    @commands.command()
    async def role(self, ctx: commands.Context, role: nextcord.Role):
        await ctx.send(str(role))

    # Groups
    @commands.group()
    async def group_test(self, ctx: commands.Context):
        if not ctx.invoked_subcommand:
            await ctx.send("I am a group!")

	@group_test.command(name="a")
	async def group_test_a(self, ctx: commands.Context):
		await ctx.send("I am a sub command of group `group_test`")

    @group_test.command(name="b")
    async def group_test_b(self, ctx: commands.Context, a):
        await ctx.send(f"I am a sub command with a parameter {a}")


def setup(client):
	client.add_cog(Test(client))
