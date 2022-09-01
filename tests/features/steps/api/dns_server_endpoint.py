import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class DNSServerEndpoint(BaseEndpoint):
    """
    Represents the /dns/server API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {},
        'delete': {},
        'get': {},
        'update': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/dns/server{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(
        self,
        filter: dict = None,
        sort: str = None,
        page: int = None,
        limit: int = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', '__class__'])
        params = self.create_params(args)
        response = super().get(self.url(), params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        credentials: str | dict,
        hostname: str,
        description: str = None,
        name: str = None,
        owner_group_id: str = None,
        zone: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().delete(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: int,
        credentials: str | dict = None,
        hostname: str = None,
        description: str = None,
        name: str = None,
        owner_group_id: str = None,
        zone: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        response = self.patch(self.url(suffix=f"/{id}"), json=body)

        return response
