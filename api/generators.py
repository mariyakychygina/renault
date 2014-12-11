
class BaseGenerator(object):

    def generate_data(self):
        raise NotImplementedError()


class EventTypes(BaseGenerator):

    def generate_data(self, **kwargs):
        pass