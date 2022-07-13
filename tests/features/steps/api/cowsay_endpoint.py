import requests

from api.base_endpoint import BaseEndpoint, log_call


class CowsayEndpoint(BaseEndpoint):
    """
    Represents the cowsay API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        "cowsay": {}
    }

    def cowsay_url(self, suffix: str = '') -> str:
        return f"{self.base_url}/cowsay{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS["cowsay"])
    def cowsay(self) -> requests.Response:
        url = self.cowsay_url()
        response = self.get(url)

        return response
