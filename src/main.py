"""
Main module
"""

import collections.abc
import datetime
import logging
import os
import re
import time
from typing import Optional

import aiohttp
import mysql.connector
import nextcord
from dotenv import load_dotenv
from mysql.connector import MySQLConnection
from mysql.connector.cursor_cext import CMySQLCursorBuffered
from nextcord.ext import commands

load_dotenv()

logging.basicConfig(level=logging.INFO)


class CustomBot(commands.Bot):
    """
    Subclassed Bot to implement own features tightly
    """

    def __init__(self):
        self.aiohttp_session: Optional[aiohttp.ClientSession] = None
        self.token = os.getenv("BOT_TOKEN")
        match = re.search(
            r"^(?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)$", os.getenv("BOT_VERSION")
        )
        self.version = (
            match.group("major"),
            match.group("minor"),
            match.group("patch"),
        )
        self.start_time = time.time()
        self.loaded_modules: set = set()
        self.unloaded_modules: set = set()
        self.errored_modules: set = set()
        self.main_color = 0xFFFFFF
        self.database: Optional[MySQLConnection] = None
        self.cursor: Optional[CMySQLCursorBuffered] = None
        super().__init__(
            command_prefix=commands.when_mentioned_or(os.getenv("BOT_PREFIX")),
            intents=nextcord.Intents().all(),
            owner_id=int(os.getenv("BOT_OWNER_ID")),
        )

    def log_event(self, event_name: str, event_type: str) -> None:
        """
        Log event
        :param event_name: The events name
        :param event_type: The events type
        :return: None
        """
        sql = "INSERT INTO bot_db.events(event_name, event_type) VALUES(%s, %s)"
        val = (event_name, event_type)
        self.cursor.execute(sql, val)
        self.database.commit()
        logging.info("logged %s as %s", event_name, event_type)

    def log_command_stats(self, command_name: str, command_state: str) -> None:
        """
        Log command stats
        :param command_name: The commands name
        :param command_state: The state of the command
        :return: None
        """
        sql = "INSERT INTO bot_db.command_stats(command_name, command_state) VALUES(%s, %s)"
        val = (command_name, command_state)
        self.cursor.execute(sql, val)
        self.database.commit()
        logging.info("logged %s (%s)", command_name, command_state)

    def uptime(self) -> datetime.timedelta:
        """
        Get the bots uptime
        :return: timedelta object of the current uptime
        """
        difference = int(time.time() - self.start_time)
        uptime = datetime.timedelta(seconds=difference)
        return uptime

    def load_db(self) -> None:
        """
        Load the database connection
        :return: None
        """
        try:
            self.database: MySQLConnection = mysql.connector.connect(
                host=str(os.getenv("DB_HOST")),
                database=str(os.getenv("DB_NAME")),
                user=str(os.getenv("DB_USER")),
                password=str(os.getenv("DB_PW")),
            )

            self.cursor: CMySQLCursorBuffered = self.database.cursor(buffered=True)
        except mysql.connector.errors.DatabaseError:
            raise SystemError("You forgot to start XAMPP")

    def load_dir(self, dirr) -> None:
        """
        Search a directory for cogs and load them
        :param dirr: The directory to search
        :return: None
        """
        files = [file[:-3] for file in os.listdir(dirr) if not file.startswith("__")]
        for file in files:
            ext = f"{dirr}.{file}"
            try:
                self.load_extension(ext)
                self.loaded_modules.add(file)
            except nextcord.ext.commands.ExtensionError:
                self.errored_modules.add(file)
                raise

    def load_cogs(self) -> None:
        """
        Load cogs
        :return: None
        """
        self.load_dir("cogs")
        self.load_extension("jishaku")
        logging.info("loading extensions finished")

    def load_tasks(self) -> None:
        """
        Load tasks
        :return: None
        """
        self.load_dir("tasks")
        logging.info("loading tasks finished")

    def load_debug_cog(self) -> None:
        """
        Load the debug cog
        :return: None
        """
        self.load_extension("debug_cog.py")

    def load_exception_handler(self) -> None:
        """
        Load the exception handler
        :return: None
        """
        self.load_extension("exception_handler")

    async def register_aiohttp_session(self) -> None:
        """
        Register the bots ClientSession
        :return: None
        """
        self.aiohttp_session = aiohttp.ClientSession()

    def run_bot(self) -> None:
        """
        Run the bot
        :return: None
        """
        logging.info("starting up...")
        self.load_db()
        self.load_exception_handler()
        self.load_cogs()
        self.load_tasks()
        self.loop.create_task(self.register_aiohttp_session())
        super().run(self.token)

    # Events
    async def on_ready(self) -> None:
        """
        on_ready event
        :return: None
        """
        logging.info("ready")
        logging.info("logged in as %s / %s", self.user, self.user.id)
        self.log_event("on_ready", "event")

    async def on_connect(self) -> None:
        """
        on_connect event
        :return: None
        """
        self.log_event("on_connect", "event")

    async def on_disconnect(self) -> None:
        """
        on_disconnect event
        :return: None
        """
        self.log_event("on_disconnect", "event")


class CustomHelpCommand(commands.HelpCommand):
    """
    Custom help command
    """

    # !help
    async def send_bot_help(self, mapping: collections.abc.Mapping) -> nextcord.Message:
        """
        Bot help
        :param mapping: Stuff
        :return: The message that got sent
        """

        emb = nextcord.Embed(
            title=f"**Full command list.** For a detailed guide, check "
            f"{self.context.clean_prefix}help <name of command>",
            color=bot.main_color,
        )

        for cog in bot.cogs:
            cog = bot.get_cog(cog)
            cog_cmds = cog.get_commands()
            cog_cmd_list = " ".join(
                [f"`{cmd.name}`" for cmd in cog_cmds if not cmd.hidden]
            )
            if cog_cmd_list:
                emb.add_field(
                    name=f"**{cog.qualified_name} Commands [{len(cog_cmds)}]:**",
                    value=cog_cmd_list,
                    inline=False,
                )

        return await self.context.send(embed=emb)

    # !help <command>
    async def send_command_help(self, command: commands.Command) -> nextcord.Message:
        """
        Command help
        :param command: The command given
        :return: The message that got sent
        """
        sql = "SELECT COUNT(command_name) FROM bot_db.command_stats WHERE command_name=%s AND command_state=%s"

        val = (command.name, "SUCCESS")
        bot.cursor.execute(sql, val)
        times_worked = bot.cursor.fetchone()[0]

        val = (command.name, "ERROR")
        bot.cursor.execute(sql, val)
        times_failed = bot.cursor.fetchone()[0]

        times_used = times_failed + times_worked

        syntax = (
            f"{self.context.clean_prefix}{command.qualified_name} {command.signature}"
        )
        emb = nextcord.Embed(
            title="Command help",
            description="If a parameter is surrounded by <>, it is a `required` parameter\n"
            "If a parameter is surrounded by [], it is an `optional` parameter.",
            color=bot.main_color,
        )
        emb.add_field(name=str(syntax), value=f"`{command.description}`", inline=False)
        emb.add_field(
            name="Command stats",
            value=f"Successful = {times_worked}\n"
            f"Failed = {times_failed}\n"
            f"Total  usages = {times_used}",
            inline=False,
        )

        return await self.context.send(embed=emb)

    # !help <group>
    async def send_group_help(self, group: commands.Group) -> nextcord.Message:
        """
        Group help
        :param group: The group given
        :return: The message that got sent
        """
        emb = nextcord.Embed(title="Command group help", color=bot.main_color)

        for sub_command in group.walk_commands():
            syntax = f"{self.context.prefix}{group.qualified_name} {sub_command.name} {sub_command.signature}"
            emb.add_field(
                name=f"{syntax}",
                value=f"`{sub_command.description or 'No description defined.'}`",
                inline=False,
            )

        return await self.context.send(embed=emb)

    # !help <cog>
    async def send_cog_help(self, cog: commands.Cog) -> nextcord.Message:
        """
        Cog help
        :param cog: The cog given
        :return: The message that got sent
        """
        emb = nextcord.Embed(
            title="**Full command list.** For a detailed guide, check !!help <name of command>",
            color=bot.main_color,
        )

        cog_cmds = cog.get_commands()
        cog_cmd_list = " ".join([f"`{cmd.name}`" for cmd in cog_cmds if not cmd.hidden])

        if cog_cmd_list:
            emb.add_field(
                name=f"**{cog.qualified_name} Commands [{len(cog_cmds)}]:**",
                value=cog_cmd_list,
                inline=False,
            )

        return await self.context.send(embed=emb)


if __name__ == "__main__":
    bot = CustomBot()

    bot.help_command = CustomHelpCommand()
    bot.run_bot()
