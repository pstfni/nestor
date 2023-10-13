"""Session settings and initialisation for nestor."""
from pathlib import Path
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory


def create_session():
    """
    Create a prompt session, with user history.

    Returns:
        A prompt session, with the loaded ".openai-prompt-history.txt" for prompt history.
    """
    prompt_history_path = Path().home() / ".openai-prompt-history.txt"
    session = PromptSession(history=FileHistory(str(prompt_history_path)))
    return session
