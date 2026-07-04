import webbrowser
from urllib.parse import quote_plus

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
}


LEETCODE_TOPICS = {
    "arrays": "https://leetcode.com/problem-list/array/",
    "strings": "https://leetcode.com/problem-list/string/",
    "linked list": "https://leetcode.com/problem-list/linked-list/",
    "trees": "https://leetcode.com/problem-list/tree/",
    "graph": "https://leetcode.com/problem-list/graph/",
    "dynamic programming": "https://leetcode.com/problem-list/dynamic-programming/",
}


def open_website(name):

    name = name.lower()

    if name in WEBSITES:
        webbrowser.open(WEBSITES[name])
        return True, f"Opening {name}."

    return False, "Unknown website."


def google_search(query):

    url = "https://www.google.com/search?q=" + quote_plus(query)

    webbrowser.open(url)

    return True, f"Searching Google for {query}."


def open_leetcode_topic(topic):

    topic = topic.lower()

    if topic in LEETCODE_TOPICS:

        webbrowser.open(LEETCODE_TOPICS[topic])

        return True, f"Opening LeetCode {topic}."

    return False, "Unknown topic."