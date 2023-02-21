# TODO: log cleanups, find unverifiable items
import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class LabClusterEndpoint(BaseEndpoint):
    """
    Represents the lab/cluster API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'created': IsVerifiable.NO, 'id': IsVerifiable.NO},
        'delete': {},
        'get': {},
        'update': {},
        'get_events': {},
        'delete_hosts': {},
        'get_hosts': {},
        'update_hosts': {},
        'reboot_hosts': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab/cluster{suffix}"

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
        product_id: int,
        product_params: dict,
        region_id: int,
        description: str | None = None,
        lifespan_expiration: str | None = None,
        project_id: int | None = None,
        quota: dict | None = None,
        quota_usage: dict | None = None,
        reservation_expiration: str | None = None,
        shared: bool | None = None,
        status: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)

        response = self.post(url=self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: int) -> requests.Response:
        response = super().delete(url=self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        response = super().get(url=self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: int,
        name: str | None = None,
        product_id: int | None = None,
        product_params: dict | None = None,
        region_id: int | None = None,
        description: str | None = None,
        lifespan_expiration: str | None = None,
        project_id: int | None = None,
        quota: dict | None = None,
        quota_usage: dict | None = None,
        reservation_expiration: str | None = None,
        shared: bool | None = None,
        status: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)

        response = self.patch(url=self.url(suffix=f"/{id}"), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_events'])
    def get_events(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/events")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete_hosts'])
    def delete_hosts(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/hosts")
        response = super().delete(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_hosts'])
    def get_hosts(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/hosts")
        response = super().delete(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update_hosts'])
    def update_hosts(self, id: int, hosts: list[dict]) -> requests.Response:
        url = self.url(suffix=f"/{id}/hosts")
        response = super().post(url, json=hosts)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['reboot_hosts'])
    def reboot_hosts(self, id: int, hosts: str | list[dict] | None = None, reboot_type: str | None = None) -> requests.Response:
        body = {}

        if hosts is not None:
            body['hosts'] = hosts
        if reboot_type is not None:
            body['type'] = reboot_type

        url = self.url(suffix=f"/{id}/reboot")
        response = super().post(url, json=body)

        return response
