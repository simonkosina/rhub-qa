import requests

from api.base_endpoint import BaseEndpoint, log_call


class PingEndpoint(BaseEndpoint):
    """
    Represents the ping API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        "ping": {}
    }

    def ping_url(self, suffix: str = '') -> str:
        return f"{self.base_url}/ping{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS["ping"])
    def ping(self) -> requests.Response:
        url = self.ping_url()
        response = self.get(url)

        return response
