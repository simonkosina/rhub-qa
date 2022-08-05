import json
from lib2to3.pytree import Base
import requests

from api.base_endpoint import BaseEndpoint, log_call


class TowerJobEndpoint(BaseEndpoint):
    """
    Represents the tower/job API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/tower/job{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self, filter: dict = None, page: str = None, limit: str = None) -> requests.Response:
        params = {}

        if filter:
            params['filter'] = json.dumps(filter)

        if page:
            params['page'] = page

        if limit:
            params['limit'] = limit

        url = self.url()
        response = self.get(url, params=params)

        return response
