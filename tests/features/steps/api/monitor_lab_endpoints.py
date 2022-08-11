import requests

from api.base_endpoint import BaseEndpoint, log_call


class MonitorLabEndpoint(BaseEndpoint):
    """
    Represents the /monitor/bm API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_metrics': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/monitor/lab{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_metrics'])
    def get_metrics(self) -> requests.Response:
        url = self.url(suffix=f"/metrics")
        response = super().get(url)

        return response
