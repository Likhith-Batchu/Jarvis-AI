from core.event_bus import EventBus

bus = EventBus()

def wake(data):

    print("Wake Event")

def sleep(data):

    print("Sleep Event")

bus.subscribe("wake", wake)

bus.subscribe("sleep", sleep)

bus.emit("wake")

bus.emit("sleep")