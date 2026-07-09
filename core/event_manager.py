from core.events import Event
from assistant.runtime_commands import RuntimeCommands


class EventManager:

    def __init__(self, runtime):

        self.runtime = runtime

    def parse(self, text):

        text = text.lower().strip()

        if text == "atlas":

            return Event.WAKE

        if RuntimeCommands.should_sleep(text):

            return Event.SLEEP

        return Event.TEXT