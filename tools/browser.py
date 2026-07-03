import webbrowser

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "leetcode": "https://leetcode.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
}


def open_website(site):

    site = site.lower()

    if site not in WEBSITES:
        return False, f"I don't know the website '{site}'."

    webbrowser.open(WEBSITES[site])

    return True, f"Opening {site}."