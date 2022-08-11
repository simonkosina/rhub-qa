import requests

from api.base_endpoint import BaseEndpoint, log_call


class PoliciesEndpoint(BaseEndpoint):
    """
    Represents the policies API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': True},
        'delete': {},
        'get': {},
        'update': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/policies{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = self.get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        department: str,
        constraint: dict = None
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
        id: str,
        name: str = None,
        department: str = None,
        constraint: dict = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        url = self.url(suffix=f"/{id}")
        response = self.patch(url, json=body)

        return response
