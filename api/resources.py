from urlparse import urljoin

from api import generators


class BaseResource(object):
    """
    Base API resource class. Introduces basic methods for CRUD.
    :parameter client: API client instance
    """
    base_path = None
    generator = None

    def __init__(self, client):
        self.client = client

    def get_details(self, id_, **kwargs):
        """
        Returns the result of GET (details) request.
        :param id_: object id
        :param **kwargs: are the rest parameters to send to requests.get()
            method
        """
        path = self._get_path(id_)
        return self.client.get(path, **kwargs)

    def get_list(self, **kwargs):
        """
        Returns the result of GET (list) request.
        :param id_: object id
        :param **kwargs: are the rest parameters to send to requests.get()
            method
        """
        path = self._get_path()
        return self.client.get(path, **kwargs)

    def post(self, data, **kwargs):
        """
        Returns the result of POST request.
        :param data: data to send via request body
        :param **kwargs: are the rest parameters to send to requests.post()
            method
        """
        path = self._get_path()
        return self.client.post(path, data, **kwargs)

    def put(self, id_, data, **kwargs):
        """
        Returns the result of PUT request.
        :param id_: object id
        :param data: data to send via request body
        :param **kwargs: are the rest parameters to send to requests.put()
            method
        """
        path = self._get_path(id_)
        return self.client.put(path, data, **kwargs)

    def patch(self, id_, data, **kwargs):
        """
        Returns the result of PATCH request.
        :param id_: object id
        :param data: data to send via request body
        :param **kwargs: are the rest parameters to send to requests.patch()
            method
        """
        path = self._get_path(id_)
        return self.client.patch(path, data, **kwargs)

    def delete(self, id_, **kwargs):
        """
        Returns the result of DELETE request.
        :param id_: object id
        :param **kwargs: are the rest parameters to send to requests.delete()
            method
        """
        path = self._get_path(id_)
        return self.client.delete(path, **kwargs)

    def generate_data(self, replace=None):
        """
        Generates the data according to schema.
        :param replace: the dict storing generated data overrides
        """
        return self.generator.generate_data(replace)

    def parse_errors(self, errors):
        pass

    def _get_path(self, id_=None):
        if id_:
            suffix = '{id}/' .format(id=id_)
            return urljoin(self.base_path, suffix)
        return self.base_path


class EventTypesResource(BaseResource):
    generator = generators.EventTypes()
    base_path = '/api/event_types/'
