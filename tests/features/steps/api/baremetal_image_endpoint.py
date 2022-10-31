# TODO: log cleanups, find unverifiable items
import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class BaremetalImageEndpoint(BaseEndpoint):
    """
    Represents the /bare_metal/image API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': IsVerifiable.NO},
        'get': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/bare_metal/image{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(self, image: dict) -> requests.Response:
        response = self.post(self.url(), json=image)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response
