from core.runtime import Runtime
from core.event_manager import EventManager

runtime = Runtime()

events = EventManager(runtime)

print("State:", runtime.get_state())

while True:

    text = input("> ")

    event = events.parse(text)

    print(event)

    if event == "wake":

        runtime.wake()

        print("Conversation Started")

    elif event == "sleep":

        runtime.sleep()

        print("Going to Standby")

    print(runtime.get_state())