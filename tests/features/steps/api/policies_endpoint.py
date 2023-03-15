import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class PoliciesEndpoint(BaseEndpoint):
    """
    Represents the policies API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': IsVerifiable.NO},
        'delete': {},
        'get': {'id': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/policies{suffix}"

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
        department: str,
        owner_group_id: int | None = None,
        owner_group_name: str | None = None,
        constraint: dict | None = None
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
        id: str,
        name: str | None = None,
        owner_group_id: int | None = None,
        owner_group_name: str | None = None,
        department: str | None = None,
        constraint: dict | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        url = self.url(suffix=f"/{id}")
        response = self.patch(url, json=body)
        self.log_cleanup(response, method=self.update,
                         method_args=cleanup_args)

        return response
