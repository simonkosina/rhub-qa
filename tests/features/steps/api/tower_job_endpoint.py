import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class TowerJobEndpoint(BaseEndpoint):
    """
    Represents the tower/job API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'get': {},
        'relaunch': {},
        'stdout': {},
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/tower/job{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self, filter: dict | None = None, page: str | None = None, limit: str | None = None) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', '__class__'])
        params = self.create_params(args)
        response = super().get(self.url(), params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['relaunch'])
    def relaunch(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/relaunch")
        response = self.post(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['stdout'])
    def get_stdout(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/stdout")
        response = super().get(url)

        return response
