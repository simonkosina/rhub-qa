import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class AuthGroupEndpoint(BaseEndpoint):
    """
    Represents the auth/group API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'delete': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'get': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'get_users': {}
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
        access: dict | None = None,
        attributes: dict | None = None,
        clientRoles: dict | None = None,
        path: str | None = None,
        realmRoles: list[str] | None = None,
        subGroups: list[dict] | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(url=self.url(), json=body)
        self.log_cleanup(response, method=self.delete)

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
        name: str | None = None,
        access: dict | None = None,
        attributes: dict | None = None,
        clientRoles: dict | None = None,
        path: str | None = None,
        realmRoles: list[str] | None = None,
        subGroups: list[dict] | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        url = self.url(suffix=f"/{id}")
        response = self.patch(url, json=body)
        self.log_cleanup(response, method=self.update,
                         method_args=cleanup_args)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_users'])
    def get_users(self, id: str) -> requests.Response:
        url = self.url(suffix=f"/{id}/users")
        response = super().get(url)

        return response

    # TODO:
    # implement the role methods when the API is finished
    # https://github.com/resource-hub-dev/rhub-api/blob/master/src/rhub/api/auth/group.py

    def remove_from_role(self, group_id: str, role_id: str):
        raise NotImplementedError

    def get_roles(self, id: str):
        raise NotImplementedError

    def add_to_role(self, group_id: str, role_id: str):
        raise NotImplementedError
