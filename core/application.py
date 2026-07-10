from services.service_manager import ServiceManager
from core.event_bus import EventBus


class Application:

    def __init__(self):

        self.services = ServiceManager()

        self.bus = EventBus()