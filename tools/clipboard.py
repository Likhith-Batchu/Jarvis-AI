import pyperclip


def copy(text):

    pyperclip.copy(text)

    return True, "Copied to clipboard."


def paste():

    return pyperclip.paste()