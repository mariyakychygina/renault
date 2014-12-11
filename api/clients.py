import json
from urlparse import urljoin

from requests import Session


class RestfulApiClient(Session):
    """
    RESTful client for API tests.
    :param base_url: Base URL (e.g. 'http://localhost/')
    """

    def __init__(self, base_url='http://localhost/'):
        super(RestfulApiClient, self).__init__()
        self.base_url = base_url

    def request(self, method, path, data=None, **kwargs):
        if data is not None:
            data = json.dumps(data)
        res = super(RestfulApiClient, self).request(
            method,
            urljoin(self.base_url, path),
            data=data,
            **kwargs)
        return (
            res.status_code,
            res.json() if res.text else None
        )
