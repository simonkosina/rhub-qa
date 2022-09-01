import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class LabProductEndpoint(BaseEndpoint):
    """
    Represents the lab/product API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {},
        'delete': {},
        'get': {},
        'update': {},
        'get_regions': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab/product{suffix}"

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
        name: str,
        parameters: list[dict],
        tower_template_name_create: str,
        tower_template_name_delete: str,
        description: str = None,
        enabled: bool = None,
        flavors: dict = None,
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
        name: str = None,
        parameters: list[dict] = None,
        tower_template_name_create: str = None,
        tower_template_name_delete: str = None,
        description: str = None,
        enabled: bool = None,
        flavors: dict = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        url = self.url(suffix=f"/{id}")

        response = self.patch(url, json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_regions'])
    def get_regions(
        self,
        id: int,
        filter: dict = None,
        page: int = None,
        limit: int = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', 'id', '__class__'])
        params = self.create_params(args)

        url = self.url(suffix=f"/{id}/regions")
        response = super().get(url, params=params)

        return response
