import requests

from api.base_endpoint import BaseEndpoint, log_call


class LabClusterEndpoint(BaseEndpoint):
    """
    Represents the lab/cluster API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'created': True, 'id': True},
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
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        product_id: int,
        product_params: dict,
        region_id: int,
        description: str = None,
        lifespan_expiration: str = None,
        project_id: int = None,
        quota: dict = None,
        quota_usage: dict = None,
        reservation_expiration: str = None,
        shared: bool = None,
        status: str = None,
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
        name: str = None,
        product_id: int = None,
        product_params: dict = None,
        region_id: int = None,
        description: str = None,
        lifespan_expiration: str = None,
        project_id: int = None,
        quota: dict = None,
        quota_usage: dict = None,
        reservation_expiration: str = None,
        shared: bool = None,
        status: str = None,
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
    def reboot_hosts(self, id: int, hosts: str | list[dict] = None, reboot_type: str = None) -> requests.Response:
        body = {}

        if hosts is not None:
            body['hosts'] = hosts
        if reboot_type is not None:
            body['type'] = reboot_type

        url = self.url(suffix=f"/{id}/reboot")
        response = super().post(url, json=body)

        return response
