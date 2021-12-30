"""
This is a template module for easy copy pasting
"""

import nextcord
from nextcord.ext import commands

from main import CustomBot


class TemplateCog(commands.Cog):
    """
    This is a template cog
    """

    def __init__(self, client: CustomBot):
        self.client: CustomBot = client

    @commands.command()
    async def template_command(self, ctx: commands.Context) -> nextcord.Message:
        """
        Template command with text response
        :param ctx: The context
        :return: The message that got sent
        """
        return await ctx.send("Template Message")

    @commands.command()
    async def template_embed(self, ctx: commands.Context) -> nextcord.Message:
        """
        Template command with embed response
        :param ctx: The context
        :return: The message that got sent
        """
        emb = nextcord.Embed(
            title="Template title",
            description="Template description",
            timestamp=ctx.message.created_at,
            color=0x696969,
        )
        emb.set_author(
            name="Template author name",
            url="https://example.com/",
            icon_url=ctx.author.avatar.with_size(4096).url,
        )
        emb.set_thumbnail(url="https://i.imgur.com/p2qNFag.png")  # small image
        emb.set_image(url="https://i.imgur.com/yVpymuV.png")  # large image
        emb.add_field(name="Template field 1", value="Template value 1", inline=False)
        emb.add_field(name="Template field 2", value="Template value 2", inline=False)
        emb.add_field(name="Template field 3", value="Template value 3", inline=False)
        emb.add_field(name="Template field 4", value="Template value 4", inline=True)
        emb.add_field(name="Template field 5", value="Template value 5", inline=True)
        emb.add_field(name="Template field 6", value="Template value 6", inline=True)
        emb.set_footer(
            text="Template footer", icon_url=ctx.guild.icon.with_size(4096).url
        )
        return await ctx.send(embed=emb)


def setup(client):
    """
    Setup function to add the cog to the client
    :param client: the client
    :return: None
    """
    client.add_cog(TemplateCog(client))
