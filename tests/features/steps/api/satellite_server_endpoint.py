import requests

from api.base_endpoint import BaseEndpoint, log_call


class SatelliteServerEndpoint(BaseEndpoint):
    """
    Represents the /satellite/server API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {},
        'delete': {},
        'get': {},
        'update': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/satellite/server{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        credentials: str | dict,
        hostname: str,
        name: str,
        description: str = None,
        insecure: bool = None,
        owner_group_id: str = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: int) -> requests.Response:
        response = super().delete(self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        response = super().get(self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: int,
        credentials: str | dict = None,
        hostname: str = None,
        name: str = None,
        description: str = None,
        insecure: bool = None,
        owner_group_id: str = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        response = self.patch(self.url(f"/{id}"), json=body)

        return response
