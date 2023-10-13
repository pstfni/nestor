"""Send and receive messages from openai"""
from typing import Literal

import openai

from nestor.gpt.typing import GPTQuery


def add_message(
    message_stack: list[GPTQuery], role: Literal["user", "system", "assistant"], content: str
) -> list[GPTQuery]:
    """
    Add a message to the current stack.

    Args:
        message_stack: Current stack of messages
        role: Role of the message (system, user, assistant)
        content: Content of the message

    Returns:
        The updated stack of messages.
    """
    message_stack.append({"role": role, "content": content})
    return message_stack


def send_messages(message_stack: list[GPTQuery]) -> str | None:
    """
    Send messages to OpenAI, and retrieve the response.

    Args:
        message_stack: The message stack

    Returns:
        The gpt response
    """
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message_stack, stream=False)
    except KeyboardInterrupt:
        exit(0)

    if response:
        content = response["choices"][0]["message"]["content"]
        return content
    return None
