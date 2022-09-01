import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class MonitorBMEndpoint(BaseEndpoint):
    """
    Represents the /monitor/bm API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_hosts': {},
        'get_metrics': {},
        'get_power_states_metrics': {},
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/monitor/bm{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_hosts'])
    def get_hosts(self, host_type: str) -> requests.Response:
        url = self.url(suffix=f"/hosts/{host_type}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_metrics'])
    def get_metrics(self) -> requests.Response:
        url = self.url(suffix=f"/metrics")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_power_states_metrics'])
    def get_power_states_metrics(self) -> requests.Response:
        url = self.url(suffix=f"/power_states_metrics")
        response = super().get(url)

        return response
