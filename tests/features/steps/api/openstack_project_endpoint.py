# TODO: log cleanups, find unverifiable items
import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class OpenstackProjectEndpoint(BaseEndpoint):
    """
    Represents the openstack/project API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': IsVerifiable.NO},
        'delete': {},
        'get': {},
        'update': {},
        'get_limits': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/openstack/project{suffix}"

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
        cloud_id: int,
        name: str,
        owner_id: str,
        description: str | None = None,
        group_id: str | None = None,
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
        project_id: int,
        cloud_id: int | None = None,
        name: str | None = None,
        owner_id: str | None = None,
        description: str | None = None,
        group_id: str | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', 'project_id'])
        body = self.create_body(args)
        url = self.url(suffix=f"/{project_id}")

        response = self.patch(url, json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_limits'])
    def get_limits(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/limits")
        response = super().get(url)

        return response
