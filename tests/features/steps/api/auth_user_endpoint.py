import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class AuthUserEndpoint(BaseEndpoint):
    """
    Represents the auth/user API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': IsVerifiable.NO, 'createdTimestamp': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'delete': {},
        'get': {'id': IsVerifiable.NO, 'createdTimestamp': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO, 'createdTimestamp': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'remove_from_group': {},
        'get_groups': {},
        'add_to_group': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/user{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(url=self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        username: str,
        email: str,
        password: str = None,
        access: dict = None,
        attributes: dict = None,
        clientConsents: list[dict] = None,
        clientRoles: dict = None,
        createdTimestamp: int = None,
        disableableCredentialTypes: list[str] = None,
        emailVerified: bool = None,
        enabled: bool = None,
        federatedIdentities: list[dict] = None,
        federationLink: str = None,
        firstName: str = None,
        groups: list[str] = None,
        lastName: str = None,
        notBefore: int = None,
        origin: str = None,
        realmRoles: list[str] = None,
        requiredActions: list[str] = None,
        serviceAccountClientId: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)

        response = self.post(url=self.url(), json=body)

        try:
            response.raise_for_status()
            id = response.json()['id']
            BaseEndpoint.LOGGER.log_cleanup(self.delete, id=id)
        except requests.HTTPError:
            pass

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().delete(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: str,
        username: str = None,
        email: str = None,
        password: str = None,
        access: dict = None,
        attributes: dict = None,
        clientConsents: list[dict] = None,
        clientRoles: dict = None,
        createdTimestamp: int = None,
        disableableCredentialTypes: list[str] = None,
        emailVerified: bool = None,
        enabled: bool = None,
        federatedIdentities: list[dict] = None,
        federationLink: str = None,
        firstName: str = None,
        groups: list[str] = None,
        lastName: str = None,
        notBefore: int = None,
        origin: str = None,
        realmRoles: list[str] = None,
        requiredActions: list[str] = None,
        serviceAccountClientId: str = None,

    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        
        url = self.url(suffix=f"/{id}")
        response = self.patch(url, json=body)

        try:
            response.raise_for_status()
            BaseEndpoint.LOGGER.log_cleanup(self.update, id=id, **cleanup_args)
        except requests.HTTPError:
            pass

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['remove_from_group'])
    def remove_from_group(self, user_id: str, group_id: str) -> requests.Response:
        url = self.url(suffix=f"/{user_id}/groups")
        body = {'id': group_id}

        response = super().delete(url, json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_groups'])
    def get_groups(self, id: str) -> requests.Response:
        url = self.url(suffix=f"/{id}/groups")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['add_to_group'])
    def add_to_group(self, user_id: str, group_id: str) -> requests.Response:
        url = self.url(suffix=f"/{user_id}/groups")
        body = {'id': group_id}

        response = self.post(url, json=body)

        try:
            response.raise_for_status()
            BaseEndpoint.LOGGER.log_cleanup(self.remove_from_group, user_id=user_id, group_id=group_id)
        except requests.HTTPError:
            pass

        return response

    # TODO:
    # following function are not yet implemented in the API itself
    # https://github.com/resource-hub-dev/rhub-api/blob/master/src/rhub/api/auth/user.py

    def remove_from_role(self, user_id: str, role_id: str):
        raise NotImplementedError

    def get_roles(self, id: str):
        raise NotImplementedError

    def add_to_role(self, user_id: str, role_id: str):
        # TODO: add remove_from_group to log_cleanups
        raise NotImplementedError
