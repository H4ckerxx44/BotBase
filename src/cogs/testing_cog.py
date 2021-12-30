"""
This is a testing cog
"""

import nextcord
from nextcord.ext import commands

from main import CustomBot


class Test(commands.Cog):
    """
    This is the testing cog where all commands are found for testing
    """

    def __init__(self, client: CustomBot):
        self.client: CustomBot = client
        self.error_color = nextcord.Color.red()

    @commands.is_owner()
    @commands.command(aliases=["l"], hidden=True)
    async def load(self, ctx: commands.Context, *extensions) -> nextcord.Message:
        """
        Command to load extensions
        :param ctx: The context
        :param extensions: List of extensions to be loaded
        :return: The message that got sent
        """
        success = []

        for ext in extensions:
            try:
                self.client.load_extension(f"cogs.{ext}")
                self.client.unloaded_modules.remove(ext)
                self.client.loaded_modules.add(ext)
                success.append(f"{ext}")
            except commands.ExtensionAlreadyLoaded:
                try:
                    self.client.unloaded_modules.remove(ext)
                    self.client.errored_modules.remove(ext)
                except KeyError:
                    pass
                raise
            except (commands.ExtensionFailed, commands.NoEntryPointError):
                self.client.errored_modules.add(ext)
                raise

        loaded_exts = ", ".join(f"`{x}`" for x in success)
        return await ctx.send(f"loaded {loaded_exts} successfully")

    @commands.is_owner()
    @commands.command(aliases=["ul"], hidden=True)
    async def unload(self, ctx: commands.Context, *extensions) -> nextcord.Message:
        """
        Command to unload extensions
        :param ctx: The context
        :param extensions: List of extensions to be unloaded
        :return: The message that got sent
        """
        success = []

        for ext in extensions:
            try:
                self.client.unload_extension(f"cogs.{ext}")
                self.client.loaded_modules.remove(ext)
                self.client.unloaded_modules.add(ext)
                success.append(f"{ext}")
            except:
                raise

        unloaded_exts = ", ".join(f"`{x}`" for x in success)
        return await ctx.send(f"unloaded {unloaded_exts} successfully")

    @commands.is_owner()
    @commands.command(aliases=["rl"], hidden=True)
    async def reload(self, ctx: commands.Context, *extensions) -> nextcord.Message:
        """
        Command to reload extensions
        :param ctx: The context
        :param extensions: List of extensions to be reloaded
        :return: The message that got sent
        """
        success = []

        for ext in extensions:
            try:
                try:
                    self.client.errored_modules.remove(ext)
                except KeyError:
                    continue
                self.client.reload_extension(f"cogs.{ext}")
                success.append(f"{ext}")
            except (commands.ExtensionFailed, commands.NoEntryPointError):
                self.client.errored_modules.add(ext)
                raise

        reloaded_exts = ", ".join(f"`{x}`" for x in success)
        return await ctx.send(f"reloaded {reloaded_exts} successfully")

    # Commands
    @commands.command()
    async def test0(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command with no parameters
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("hi")

    @commands.command()
    async def test1(self, ctx: commands.Context, param1) -> nextcord.Message:
        """
        Command with 1 untyped parameter
        :param ctx: The context
        :param param1: Something
        :return: The message that got sent
        """
        return await ctx.send(f"{param1=}")

    @commands.command()
    async def test2(self, ctx: commands.Context, param1, param2) -> nextcord.Message:
        """
        Command with 2 untyped parameters
        :param ctx: The context
        :param param1: Something
        :param param2: Something
        :return: The message that got sent
        """
        return await ctx.send(f"{param1=} {param2=}")

    @commands.command()
    async def test3(
        self, ctx: commands.Context, param1, param2, param3
    ) -> nextcord.Message:
        """
        Command with 3 untyped parameters
        :param ctx: The context
        :param param1: Something
        :param param2: Something
        :param param3: Something
        :return: The message that got sent
        """
        return await ctx.send(f"{param1=} {param2=} {param3=}")

    @commands.is_owner()
    @commands.command()
    async def not_owner(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a NotOwner exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("If you see this you are the bot owner.")

    @commands.command()
    async def member_not_found(
        self, ctx: commands.Context, member: nextcord.Member
    ) -> nextcord.Message:
        """
        Command to raise a MemberNotFound exception
        :param ctx: The context
        :param member: A Member
        :return: The message that got sent
        """
        return await ctx.send(str(member))

    @commands.has_role(731275569471422485)
    @commands.command()
    async def missing_role(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a MissingRole exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("")

    @commands.command()
    async def bad_argument(
        self, ctx: commands.Context, param1: int
    ) -> nextcord.Message:
        """
        Command to raise a BadArgument exception
        :param ctx: The context
        :param param1: Something NOT int
        :return: The message that got sent
        """
        return await ctx.send(str(param1))

    @commands.command()
    async def guild_not_found(
        self, ctx: commands.Context, guild: nextcord.Guild
    ) -> nextcord.Message:
        """
        Command to raise a GuildNotFound exception
        :param ctx: The context
        :param guild: A guild
        :return: The message that got sent
        """
        return await ctx.send(str(guild))

    @commands.command()
    async def too_many_arguments(
        self, ctx: commands.Context, param1, param2
    ) -> nextcord.Message:
        """
        Command to raise a TooManyArguments exception
        :param ctx: The context
        :param param1: Something
        :param param2: Something else
        :return: The message that got sent
        """
        return await ctx.send(f"{param1=}, {param2=}")

    @commands.command()
    async def role_not_found(
        self, ctx: commands.Context, role: nextcord.Role
    ) -> nextcord.Message:
        """
        Command to raise a RoleNotFound exception
        :param ctx: The context
        :param role: A role
        :return: The message that got sent
        """
        return await ctx.send(str(role))

    @commands.command()
    async def message_not_found(
        self, ctx: commands.Context, message: nextcord.Message
    ) -> nextcord.Message:
        """
        Command to raise a MemberNotFound exception
        :param ctx: The context
        :param message: A message
        :return: The message that got sent
        """
        return await ctx.send(str(message))

    @commands.command()
    async def channel_not_found(
        self, ctx: commands.Context, channel
    ) -> nextcord.Message:
        """
        Command to raise ChannelNotFound exception
        :param ctx: The context
        :param channel: Channel
        :return: The message that got sent
        """
        return await ctx.send(str(channel))

    @commands.command()
    async def string_errors(
        self, ctx: commands.Context, *, text: str
    ) -> nextcord.Message:
        """
        Command to raise on of the string exceptions
        :param ctx: The context
        :param text: A text
        :return: The message that got sent
        """
        return await ctx.send(text)

    @commands.dm_only()
    @commands.command()
    async def private_message_only(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a PrivateMessageOnly exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("DM Only")

    @commands.guild_only()
    @commands.command()
    async def no_private_message(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a NoPrivateMessage exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Guild only")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def missing_permissions(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a MissingPermissions exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Admin only")

    @commands.bot_has_permissions(administrator=True)
    @commands.command()
    async def xbot_missing_permissions(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a BotMissingPermissions exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Bot admin only.")

    @commands.command()
    async def missing_any_role(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a MissingAnyRole exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Missing any role.")

    @commands.command()
    async def xbot_missing_any_role(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a BotMissingAnyRole exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Bot missing any role.")

    @commands.command()
    async def xbot_missing_role(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a BotMissingRole exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Bot missing role.")

    @commands.is_nsfw()
    @commands.command()
    async def nsfw_only(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a NSFWChannelRequired exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("NSFW only.")

    @commands.command(enabled=False)
    async def disabled_command(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise a DisabledCommand exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Disabled command.")

    @commands.cooldown(1, 5)
    @commands.command()
    async def command_on_cooldown(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command to raise CommandOnCooldown exception
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Command on cooldown.")

    @commands.command()
    async def extension_already_loaded(self, ctx: commands.Context) -> None:
        """
        Command to raise an ExtensionAlreadyLoaded exception
        :param ctx: The context
        :return: None
        """
        self.client.load_extension("jishaku")

    @commands.command()
    async def extension_not_loaded(self, ctx: commands.Context) -> None:
        """
        Command to raise an ExtensionNotLoaded exception
        :param ctx: The context
        :return: None
        """
        self.client.unload_extension("jishaku")
        self.client.unload_extension("jishaku")

    @commands.command()
    async def extension_failed(self, ctx: commands.Context) -> None:
        """
        Command to raise an ExtensionFailed exception
        :param ctx: The context
        :return: None
        """
        self.client.load_extension("failing_extension")

    @commands.command()
    async def extension_not_found(self, ctx: commands.Context) -> None:
        """
        Command to raise an ExtensionNotFound exception
        :param ctx: The context
        :return: None
        """
        self.client.load_extension("cogs.not_to_be_found")

    @commands.command()
    async def no_entry_point_error(self, ctx: commands.Context) -> None:
        """
        Command to raise a NoEntryPointError exception
        :param ctx: The context
        :return: None
        """
        self.client.load_extension("no_entry_point_extension")

    @commands.command()
    async def channel(
        self, ctx: commands.Context, channel: nextcord.TextChannel
    ) -> nextcord.Message:
        """
        Command to send the channel object which it got invoked with
        :param ctx: The context
        :param channel: The message
        :return: The message that got sent
        """
        return await ctx.send(str(channel))

    @commands.command()
    async def member(
        self, ctx: commands.Context, member: nextcord.Member
    ) -> nextcord.Message:
        """
        Command to send the member object which it got invoked with
        :param ctx: The context
        :param member: The message
        :return: The message that got sent
        """
        return await ctx.send(str(member))

    @commands.command()
    async def guild(
        self, ctx: commands.Context, guild: nextcord.Guild
    ) -> nextcord.Message:
        """
        Command to send the guild object which it got invoked with
        :param ctx: The context
        :param guild: The message
        :return: The message that got sent
        """
        return await ctx.send(str(guild))

    @commands.command()
    async def message(
        self, ctx: commands.Context, message: nextcord.Message
    ) -> nextcord.Message:
        """
        Command to send the message object which it got invoked with
        :param ctx: The context
        :param message: The message
        :return: The message that got sent
        """
        return await ctx.send(str(message))

    @commands.command()
    async def role(
        self, ctx: commands.Context, role: nextcord.Role
    ) -> nextcord.Message:
        """
        Command to send the role object which it got invoked with
        :param ctx: The context
        :param role: The role
        :return: The message that got sent
        """
        return await ctx.send(str(role))

    # Groups
    @commands.group()
    async def group_test(self, ctx: commands.Context) -> nextcord.Message:
        """
        Command group for testing
        :param ctx: The context
        :return: The message that got sent
        """
        if not ctx.invoked_subcommand:
            return await ctx.send("I am a group!")

    @group_test.command(name="a")
    async def group_test_a(self, ctx: commands.Context) -> nextcord.Message:
        """
        Subcommand a from group a
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("I am a sub command of group `group_test`")

    @group_test.command(name="b")
    async def group_test_b(self, ctx: commands.Context, param1) -> nextcord.Message:
        """
        Subcommand b from group a with a parameter
        :param ctx: The context
        :param param1: Something
        :return: The message that got sent
        """
        return await ctx.send(f"I am a sub command with a parameter {param1}")


def setup(client: CustomBot) -> None:
    """
    Setup function to add the cog to the client
    :param client: the client
    :return: None
    """
    client.add_cog(Test(client))
