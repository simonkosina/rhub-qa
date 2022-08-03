import json
import requests

from api.base_endpoint import BaseEndpoint, log_call


class PoliciesEndpoint(BaseEndpoint):
    """
    Represents the policies API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        # TODO: constraint['cost'] is just an example of nested fields and can be removed
        'create': {'constraint': {'cost': False}, 'id': True},
        'get_list': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/policies{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(self, name: str, department: str, constraint: dict = None) -> requests.Response:
        url = self.url()

        params = {
            'name': name,
            'department': department,
        }

        if constraint:
            params['constraint'] = json.loads(constraint)

        response = self.post(url, json=params)

        print(response)
        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        url = self.url()
        response = self.get(url)

        return response
