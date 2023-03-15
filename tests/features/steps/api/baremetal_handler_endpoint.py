# TODO: log cleanups, find unverifiable items
import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class BaremetalHandlerEndpoint(BaseEndpoint):
    """
    Represents the /baremetal/handler API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {},
        'get': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/bare_metal/handler{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        arch: str,
        base_url: str,
        hostname: str,
        location_id: int,
        name: str,
        password: str,
        user_name: str,
        last_check: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response
