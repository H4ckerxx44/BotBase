"""
Utility functions
"""

from datetime import datetime

from nextcord.ext import commands


def format_time(_time: datetime.time) -> str:
    """
    Format to hours only
    :param _time: The time to be formatted
    :return: Formatted string
    """
    return _time.strftime("%H:%M:%S")


def format_date(_date: datetime.date) -> str:
    """
    Format to german date
    :param _date: The date to be formatted
    :return: Formatted string
    """
    return _date.strftime("%d.%m.%Y")


def format_to_db_date(_date: datetime) -> str:
    """
    Format to Database datetime format
    :param _date: The datetime to  be formatted
    :return: Formatted string
    """
    return _date.strftime("%Y-%m-%d %H:%M:%S")


def format_date_time(_datetime: datetime) -> str:
    """
    Format to time, date format
    :param _datetime: The datetime to  be formatted
    :return: Formatted string
    """
    return _datetime.strftime("%H:%M:%S, %d.%m.%Y")


def list_options(group: commands.Group) -> str:
    """
    Format string to list all subcommands of a command group
    :param group: The group to list sub commands from
    :return: Formatted string of subcommands
    """
    options = [f"`!!{cmd.qualified_name}`" for cmd in group.walk_commands()]
    params = ", ".join(options)
    return params
