from datetime import datetime, timezone
from enum import Enum
from typing import Literal

now_utc = datetime.now(timezone.utc)


class Prompt(str, Enum):
    DEFAULT = f"""\
    Help the user by responding to their request, the output should be concise and always written in markdown.
    The current date and time is {datetime.now()} {now_utc.astimezone().tzinfo.tzname(now_utc)}."""

    WRITER = """\
    Help the user by improving the syntax, grammar and style of their request. The output should be concise, and written
    in markdown. Give 3 suggestions."""

    CODER = """\
    Help the user, act as a Python 3.11 coding assistant. Outputs should be concise, and code suggestions included. The
    code must follow PEP rules and has typing and google-style docstrings.
    """

    TRANSLATER = """\
    I will give you french sentences and you will reply with 3 suggestions of english translation.
    """


def set_prompt(target: Literal['default', 'writer', 'coder', 'translater'] = 'default') -> Prompt:
    """
    Choose the right prompt based on the target.

    Args:
        target: The role you expect from GPT

    Returns:
        The prompt. Will default to the `default` prompt
    """
    return Prompt[target.upper()]


def initialize(target: Literal['default', 'writer', 'coder', 'translater'] = 'default') -> dict[str, str]:
    """
    Given the target, setup the prompt and the first message for GPT.

    Args:
        target:  The role you expect from GPT

    Returns:
        Body of the first message for GPT
    """
    return {'role': 'system', 'content': set_prompt(target).value}
