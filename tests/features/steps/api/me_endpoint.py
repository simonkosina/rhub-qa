import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class MeEndpoint(BaseEndpoint):
    """
    Represents the me API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get': {'created_at': True, 'updated_at': True}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/me{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self) -> requests.Response:
        response = super().get(self.url())

        return response
