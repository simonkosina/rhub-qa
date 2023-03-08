# TODO: log cleanups, find unverifiable items
import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class LabProductEndpoint(BaseEndpoint):
    """
    Represents the lab/product API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'delete': {},
        'get': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'get_regions': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab/product{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(
        self,
        filter: dict | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None
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
        description: str | None = None,
        enabled: bool | None = None,
        flavors: dict | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)
        self.log_cleanup(response, method=self.delete)

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
        name: str | None = None,
        parameters: list[dict] | None = None,
        tower_template_name_create: str | None = None,
        tower_template_name_delete: str | None = None,
        description: str | None = None,
        enabled: bool | None = None,
        flavors: dict | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        response = self.patch(self.url(f"/{id}"), json=body)
        self.log_cleanup(response, method=self.update, method_args=cleanup_args)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_regions'])
    def get_regions(
        self,
        id: int,
        filter: dict | None = None,
        page: int | None = None,
        limit: int | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', 'id', '__class__'])
        params = self.create_params(args)

        url = self.url(suffix=f"/{id}/regions")
        response = super().get(url, params=params)

        return response
