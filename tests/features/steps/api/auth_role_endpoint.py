from lib2to3.pytree import Base
import requests

from api.base_endpoint import BaseEndpoint, log_call


class AuthRoleEndpoint(BaseEndpoint):
    """
    Represents the auth/role API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': True},
        'delete': {},
        'get': {},
        'update': {},
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/role{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        attributes: dict = None,
        client_role: bool = None,
        composite: bool = None,
        composites: dict = None,
        container_id: str = None,
        description: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)

        response = self.post(url=self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: str) -> requests.Response:
        response = super().delete(self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: str) -> requests.Response:
        response = super().get(self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: str,
        name: str = None,
        attributes: dict = None,
        client_role: bool = None,
        composite: bool = None,
        composites: dict = None,
        container_id: str = None,
        description: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)

        response = self.patch(url=self.url(suffix=f"/{id}"), json=body)

        return response
