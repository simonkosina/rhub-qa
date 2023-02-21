import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class SatelliteServerEndpoint(BaseEndpoint):
    """
    Represents the /satellite/server API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO, 'owner_group_id': IsVerifiable.NO},
        'create': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO, 'owner_group_id': IsVerifiable.NO},
        'delete': {},
        'get': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO, 'owner_group_id': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO, 'owner_group_id': IsVerifiable.NO}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/satellite/server{suffix}"

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
        hostname: str,
        name: str,
        description: str | None = None,
        insecure: bool | None = None,
        owner_group_id: str | None = None
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
        credentials: str | dict | None = None,
        hostname: str | None = None,
        name: str | None = None,
        description: str | None = None,
        insecure: bool | None = None,
        owner_group_id: str | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        response = self.patch(self.url(f"/{id}"), json=body)
        self.log_cleanup(response, method=self.update,
                         method_args=cleanup_args)

        return response
