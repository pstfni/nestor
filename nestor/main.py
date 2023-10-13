import os
import typer


import openai
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from rich.console import Console
from rich.markdown import Markdown
from typing import Annotated

from nestor.gpt.session import create_session
from nestor.gpt.chats import add_message, send_messages
from nestor.prompts.prompts import Prompt


try:
    openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError as key_error:
    raise ValueError(f"You must set the OPENAI_API_KEY environment variable") from key_error


def cli(target: Annotated[Prompt, typer.Argument(help="Role you expect from GPT.")] = Prompt.DEFAULT) -> int:
    console = Console(width=120)
    console.print("Welcome", justify="center")
    session = create_session()
    messages = []

    messages = add_message(messages, role="system", content=target.value)

    while True:

        try:
            text = session.prompt("🦊 ░▒▓▏", auto_suggest=AutoSuggestFromHistory())
        except (KeyboardInterrupt, EOFError):
            return 0

        with console.status("Working on it", spinner="point"):
            messages = add_message(messages, role="user", content=text)
            response = send_messages(messages)

            if response:
                messages = add_message(messages, role="assistant", content=response)
                markdown_response = Markdown(response)
                console.print(markdown_response)

        console.rule()


if __name__ == '__main__':
    typer.run(cli)
