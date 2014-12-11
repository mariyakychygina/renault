import unittest

from api.controller import RenaultAPI

from data import (
    weather, longdrive)


class EventTypeTest(unittest.TestCase):

    api = RenaultAPI()

    def test_get_list(self):
        status, response = self.api.event_type.get_list()
        self.assertTrue(status, 200)

        for type_object in response:
            if type_object.get('type') == 'Weather':
                self.assertTrue(type_object.get('values'),
                                weather.get('values'))

            if type_object.get('type') == 'Leather':
                self.assertTrue(type_object.get('values'),
                                longdrive.get('values'))
