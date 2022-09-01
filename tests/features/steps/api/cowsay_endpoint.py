import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class CowsayEndpoint(BaseEndpoint):
    """
    Represents the cowsay API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/cowsay{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self) -> requests.Response:
        url = self.url()
        response = super().get(url)

        return response
