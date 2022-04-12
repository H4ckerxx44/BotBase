"""
This is a cog with slash commands
"""

import nextcord
from nextcord.ext import commands

from main import CustomBot


TESTING_GUILD_IDS = []


class SlashCommands(commands.Cog):
    """
    This is a template cog
    """

    def __init__(self, bot: CustomBot):
        self.bot: CustomBot = bot

    @nextcord.slash_command(
        guild_ids=TESTING_GUILD_IDS, description="Simple slash command."
    )
    async def basic_slash(self, interaction: nextcord.Interaction) -> nextcord.Message:
        """
        Template command with text response
        :param interaction: The interaction
        :return: The message that got sent
        """
        return await interaction.response.send_message("This is a test.")

    @nextcord.slash_command(guild_ids=TESTING_GUILD_IDS, description="Test command")
    async def my_slash_command(self, interaction: nextcord.Interaction):
        return await interaction.response.send_message(
            "This is a slash command in a cog!"
        )

    @nextcord.slash_command(guild_ids=TESTING_GUILD_IDS)
    async def my_user_command(
        self, interaction: nextcord.Interaction, member: nextcord.Member
    ):
        return await interaction.response.send_message(f"Hello, {member}!")

    @nextcord.slash_command(guild_ids=TESTING_GUILD_IDS, description="Idk.")
    async def my_message_command(
        self, interaction: nextcord.Interaction, message: nextcord.Message
    ):
        return await interaction.response.send_message(f"{message}")

    @nextcord.slash_command(guild_ids=TESTING_GUILD_IDS, description="Bot info.")
    async def bot_info(self, interaction: nextcord.Interaction):
        e = nextcord.Embed(
            title=self.bot.user.display_name,
            description=f"Version {'.'.join(self.bot.version)}",
        )
        return await interaction.response.send_message(embed=e)

    @nextcord.slash_command(guild_ids=TESTING_GUILD_IDS, description="This is a test.")
    async def alexlol(
        self,
        interaction: nextcord.Interaction,
        arg: str = nextcord.SlashOption(description="Hallo."),
    ):
        return await interaction.response.send_message(f"The arg is {arg}.")


def setup(bot):
    """
    Setup function to add the cog to the bot
    :param bot: the bot
    :return: None
    """
    bot.add_cog(SlashCommands(bot))
