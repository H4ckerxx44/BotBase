"""
This is my exception handler
"""

import datetime
import traceback
from typing import Union

import nextcord
from nextcord.ext import commands

from main import CustomBot


# noinspection PyPep8Naming
class ExceptionHandler(commands.Cog):
    """
    This is the exception handler cog
    """

    def __init__(self, client: CustomBot):
        self.client: CustomBot = client
        self.error_color = nextcord.Color.red()

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context) -> None:
        """
        Fires when a command gets executed
        :param ctx: The context
        :return: None
        """
        self.client.log_event("on_command", "event")

    @commands.Cog.listener()
    async def on_command_completion(self, ctx: commands.Context) -> None:
        """
        Fires when a command was executed
        :param ctx: The context
        :return: None
        """
        self.client.log_command_stats(str(ctx.command.qualified_name), "SUCCESS")
        self.client.log_event("on_command_completion", "event")

    @commands.Cog.listener()
    async def on_command_error(
        self, ctx: commands.Context, error
    ) -> Union[nextcord.Message, None]:
        """
        This fires whenever a command throws an exception
        :param ctx: The context
        :param error: The error
        :return: The message that got sent
        """

        err = error
        if isinstance(err, commands.CommandInvokeError):
            err = error.original

        if isinstance(err, commands.CommandNotFound):
            return

        if isinstance(err, commands.MissingRequiredArgument):
            usage = f"`{ctx.clean_prefix}{ctx.command.qualified_name} {ctx.command.signature}`"
            emb = nextcord.Embed(
                title="Missing parameter!",
                description=f"You are missing `{err.param.name}`.\n"
                f"Usage: `{usage}`",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.NotOwner):
            emb = nextcord.Embed(
                title="Not Owner!",
                description="Only the bot-owner can execute self command.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.MemberNotFound):
            emb = nextcord.Embed(
                title="Member not found!",
                description=f"The given member ({err.argument}) could not be found.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.MissingRole):
            role = ctx.guild.get_role(err.missing_role)
            emb = nextcord.Embed(
                title="Missing role!",
                description=f"You are missing {role.mention} to use self command.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.GuildNotFound):
            emb = nextcord.Embed(
                title="Guild not found!",
                description=f"The given guild ({err.argument}) could not be found.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.TooManyArguments):
            emb = nextcord.Embed(
                title="Too many argument!",
                description=f"You supplied too many arguments. ({err.args})",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.RoleNotFound):
            emb = nextcord.Embed(
                title="Role not found!",
                description=f"The given role ({err.argument}) could not be found.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.MessageNotFound):
            emb = nextcord.Embed(
                title="Message not found!",
                description=f"The given message ({err.argument}) could not be found.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.ChannelNotFound):
            emb = nextcord.Embed(
                title="Channel not found!",
                description=f"The given channel ({err.argument}) could not be found.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.UnexpectedQuoteError):
            # TODO: add text
            emb = nextcord.Embed(
                title="",
                description="",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.InvalidEndOfQuotedStringError):
            emb = nextcord.Embed(
                title="Invalid end of quoted string!",
                description="The quoted string you have provided is invalid. "
                "Perhaps you got \" and/or ' mixed up?",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.ExpectedClosingQuoteError):
            emb = nextcord.Embed(
                title="Expected closing quote!",
                description="The quoted string you have provided is invalid. "
                "Perhaps you forgot to end the string with \" or '",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.PrivateMessageOnly):
            emb = nextcord.Embed(
                title="Private message only!",
                description="This command only works in private messages.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.NoPrivateMessage):
            emb = nextcord.Embed(
                title="No private message!",
                description="This command only works on a guild.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.MissingPermissions):
            emb = nextcord.Embed(
                title="Missing permissions!",
                description=f"You are missing "
                f"{', '.join(f'`{e}`' for e in err.missing_permissions)}",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.BotMissingPermissions):
            emb = nextcord.Embed(
                title="Bot missing permissions!",
                description=f"The bot is missing "
                f"{', '.join(f'`{e}`' for e in err.missing_permissions)}",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.MissingAnyRole):
            roles = ", ".join(x for x in err.missing_roles)
            emb = nextcord.Embed(
                title="Missing any role!",
                description=f"You are missing one of the following roles ({roles})",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.BotMissingAnyRole):
            missing_roles = (
                f"{', '.join(err.missing_roles[:-1])}, or {err.missing_roles[-1]}"
            )

            emb = nextcord.Embed(
                title="Bot missing role!",
                description=f"The bot is missing {missing_roles}",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.BotMissingRole):
            role = ctx.guild.get_role(err.missing_role)
            emb = nextcord.Embed(
                title="Bot missing role!",
                description=f"The bot is missing {role.mention}",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.NSFWChannelRequired):
            emb = nextcord.Embed(
                title="NSFW channel required!",
                description=f"This command requires {err.channel.mention} to be `NSFW`.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.DisabledCommand):
            emb = nextcord.Embed(
                title="Command disabled!",
                description="This command is currently disabled and therefor not usable.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.CommandOnCooldown):
            emb = nextcord.Embed(
                title="Command on cooldown!",
                description=f"This command is on cooldown, retry after {err.retry_after} seconds.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.ExtensionAlreadyLoaded):
            ext_name = err.name.split(".")[1]
            emb = nextcord.Embed(
                title="Extension already loaded!",
                description=f"{ext_name} is already loaded.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.ExtensionNotLoaded):
            ext_name = err.name.split(".")[1]
            emb = nextcord.Embed(
                title="Extension not loaded!",
                description=f"{ext_name} is not loaded.",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.ExtensionFailed):
            ext_name = err.name.split(".")[1]
            emb = nextcord.Embed(
                title=f"{ext_name} failed!",
                description="",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.ExtensionNotFound):
            emb = nextcord.Embed(
                title=f"{err.name} could not be found!",
                description="",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.NoEntryPointError):
            ext_name = err.name.split(".")[1]
            emb = nextcord.Embed(
                title=f"{ext_name} misses the setup function!",
                description="",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        elif isinstance(err, commands.BadArgument):
            failed = str(err.args[0]).replace('"', "`")
            emb = nextcord.Embed(
                title="Bad argument!",
                description=f"You provided a wrong parameter type. ({failed})",
                color=self.error_color,
                timestamp=datetime.datetime.now(),
            )

        else:
            emb = self.gen_default_embed(err)
            dennis = self.client.get_user(self.client.owner_id)
            await dennis.send(embed=self.gen_dennis_embed(err))

            self.client.log_event("on_command_error", "event")
            self.client.log_command_stats(str(ctx.command.qualified_name), "ERROR")

        return await ctx.send(embed=emb)

    def gen_default_embed(self, exception) -> nextcord.Embed:
        """
        Generates the default error embed
        :param exception: The unhandled exception
        :return: The embed to get sent into the chat
        """
        else_error = nextcord.Embed(
            title="Unhandled exception occurred!",
            description=str(exception.__class__.__name__),
            color=self.error_color,
            timestamp=datetime.datetime.now(),
        )
        else_error.set_footer(text="My Developer has been notified")
        return else_error

    def gen_dennis_embed(self, exception) -> nextcord.Embed:
        """
        Generates the embed to sent to me
        :param exception: The unhandled exception
        :return: The embed to be sent to me
        """
        exc = "".join(
            traceback.format_exception(
                etype=type(exception), value=exception, tb=exception.__traceback__
            )
        )
        dennis_error_embed = nextcord.Embed(
            title="Unhandled exception occurred!",
            description=f"```py\n{exc}```",
            color=self.error_color,
            timestamp=datetime.datetime.now(),
        )
        return dennis_error_embed


def setup(client) -> None:
    """
    Setup function to add the cog to the client
    :param client: the client
    :return: None
    """
    client.add_cog(ExceptionHandler(client))
