from core.jarvis import Jarvis
from core.runtime import Runtime
from core.event_manager import EventManager
from core.events import Event
from ui.boot import boot
from ui.status_bar import StatusBar
from voice.listener import listen
from voice.speaker import speak

jarvis = Jarvis()

runtime = Runtime()

events = EventManager(runtime)

boot()

while True:

    StatusBar.draw(runtime)

    # ------------------------
    # STANDBY MODE
    # ------------------------

    if runtime.get_state() == "standby":

        text = input("\nWake Word : ")

        event = events.parse(text)

        if event == Event.WAKE:

            runtime.wake()

            print("\n⚡ Atlas Activated.\n")

        continue

    # ------------------------
    # CONVERSATION MODE
    # ------------------------

    if runtime.get_mode() == "voice":

        user = listen()

    else:

        user = input("\nYou : ")

    event = events.parse(user)

    # Sleep command
    if event == Event.SLEEP:

        runtime.sleep()

        print("\n💤 Going back to standby...\n")

        continue

    reply = jarvis.process(user)

    print(f"\n🤖 Jarvis : {reply}")

    speak(reply)