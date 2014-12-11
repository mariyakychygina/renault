from api.clients import RestfulApiClient
from api.resources import EventTypesResource
from config import config


class RenaultAPI(object):
    def __init__(self):
        self.client = RestfulApiClient(
            config.base_url)
        self.event_type = EventTypesResource(self.client)