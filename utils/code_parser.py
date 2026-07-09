import re


def extract_code(text):

    """
    Extracts the first code block from an LLM response.
    """

    match = re.search(
        r"```(?:\w+)?\n(.*?)```",
        text,
        re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return None