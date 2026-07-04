from tools.app_launcher import open_application
from tools.browser import (
    open_website,
    google_search,
    open_leetcode_topic
)

from workspaces.dsa import start as start_dsa

TOOLS = {

    "open_application": open_application,

    "open_website": open_website,

    "google_search": google_search,

    "leetcode": open_leetcode_topic,

    "workspace_dsa": start_dsa,

}