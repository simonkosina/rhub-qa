# TODO: log cleanups, find unverifiable items
import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class OpenstackCloudEndpoint(BaseEndpoint):
    """
    Represents openstack/cloud API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': IsVerifiable.NO},
        'delete': {},
        'get': {},
        'update': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/openstack/cloud{suffix}"

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
        credentials: str | dict,
        domain_id: str,
        domain_name: str,
        name: str,
        networks: list[str],
        owner_group_id: str,
        url: str,
        description: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)
        self.log_cleanup(response, method=self.delete)

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
        credentials: str | dict | None = None,
        domain_id: str | None = None,
        domain_name: str | None = None,
        name: str | None = None,
        networks: list[str] | None = None,
        owner_group_id: str | None = None,
        url: str | None = None,
        description: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['id', 'self'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        response = self.patch(self.url(suffix=f"/{id}"), json=body)
        self.log_cleanup(response, method=self.update, method_args=cleanup_args)

        return response
