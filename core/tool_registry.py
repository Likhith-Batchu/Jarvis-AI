from core.tool import Tool

from tools.app_launcher import open_application
from tools.clipboard import copy

from tools.browser import (
    open_website,
    google_search,
    open_leetcode_topic
)

from workspaces.dsa import start as start_dsa




TOOLS = {

    "open_application": Tool(
        function=open_application,
        arguments=["app"]
    ),

    "open_website": Tool(
        function=open_website,
        arguments=["website"]
    ),

    "google_search": Tool(
        function=google_search,
        arguments=["query"]
    ),

    "leetcode": Tool(
        function=open_leetcode_topic,
        arguments=["topic"]
    ),
    "copy": Tool(
    function=copy,
    arguments=["text"]
    ),


}