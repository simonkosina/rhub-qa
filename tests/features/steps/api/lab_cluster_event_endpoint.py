import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class LabClusterEventEndpoint(BaseEndpoint):
    """
    Represent the lab/cluster_event API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get': {},
        'get_stdout': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab/cluster_event{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        response = super().get(url=self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_stdout'])
    def get_stdout(self, id: int) -> requests.Response:
        response = super().get(url=self.url(suffix=f"/{id}/stdout"))

        return response
