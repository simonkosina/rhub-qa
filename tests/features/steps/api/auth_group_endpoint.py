import requests

from api.base_endpoint import BaseEndpoint, log_call


class AuthGroupEndpoint(BaseEndpoint):
    """
    Represents the auth/group API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': True},
        'delete': {},
        'get': {},
        'update': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/group{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(url=self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        access: dict = None,
        attributes: dict = None,
        clientRoles: dict = None,
        path: str = None,
        realmRoles: list[str] = None,
        subGroups: list[dict] = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)

        response = self.post(url=self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: str) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().delete(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: str) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: str,
        name: str = None,
        access: dict = None,
        attributes: dict = None,
        clientRoles: dict = None,
        path: str = None,
        realmRoles: list[str] = None,
        subGroups: list[dict] = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)

        url = self.url(suffix=f"/{id}")
        response = self.patch(url, json=body)

        return response

    # TODO:
    # implement the role methods when the API is finished
    # https://github.com/resource-hub-dev/rhub-api/blob/master/src/rhub/api/auth/group.py

    def remove_from_role(self):
        raise NotImplementedError

    def get_roles(self):
        raise NotImplementedError

    def add_to_role(self):
        raise NotImplementedError
