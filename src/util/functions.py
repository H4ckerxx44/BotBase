from datetime import datetime
from nextcord.ext import commands


def format_time(_time: datetime.time) -> str:
    return _time.strftime("%H:%M:%S")


def format_date(_date: datetime.date) -> str:
    return _date.strftime("%d.%m.%Y")


def format_to_db_date(_date: datetime) -> str:
    return _date.strftime("%Y-%m-%d %H:%M:%S")


def format_date_time(_datetime: datetime) -> str:
    return _datetime.strftime("%H:%M:%S, %d.%m.%Y")


def list_options(group: commands.Group) -> str:
    options = [f"`!!{cmd.qualified_name}`" for cmd in group.walk_commands()]
    params = ", ".join(options)
    return params
