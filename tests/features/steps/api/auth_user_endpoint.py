from lib2to3.pytree import Base
from types import NotImplementedType
import requests

from api.base_endpoint import BaseEndpoint, log_call


class AuthUserEndpoint(BaseEndpoint):
    """
    Represents the auth/user API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': True, 'createdTimestamp': True},
        'delete': {},
        'get': {},
        'update': {},
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
        access: dict = None,
        attributes: dict = None,
        client_consents: list[dict] = None,
        client_roles: dict = None,
        created_timestamp: int = None,
        disableable_credential_types: list[str] = None,
        email_verified: bool = None,
        enabled: bool = None,
        federated_identities: list[dict] = None,
        federation_link: str = None,
        first_name: str = None,
        groups: list[str] = None,
        last_name: str = None,
        not_before: int = None,
        origin: str = None,
        realm_roles: list[str] = None,
        required_actions: list[str] = None,
        service_account_client_id: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)

        response = self.post(url=self.url(), json=body)

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
        access: dict = None,
        attributes: dict = None,
        client_consents: list[dict] = None,
        client_roles: dict = None,
        created_timestamp: int = None,
        disableable_credential_types: list[str] = None,
        email_verified: bool = None,
        enabled: bool = None,
        federated_identities: list[dict] = None,
        federation_link: str = None,
        first_name: str = None,
        groups: list[str] = None,
        last_name: str = None,
        not_before: int = None,
        origin: str = None,
        realm_roles: list[str] = None,
        required_actions: list[str] = None,
        service_account_client_id: str = None,

    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)

        url = self.url(suffix=f"/{id}")
        response = self.patch(url, json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['remove_from_group'])
    def remove_from_group(self, user_id: str, group_id: str) -> requests.Response:
        url = self.url(suffix=f"/{user_id}/groups")
        body = {'id': group_id}

        print(url)
        response = super().delete(url, json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_groups'])
    def get_groups(self, id) -> requests.Response:
        url = self.url(suffix=f"/{id}/groups")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['add_to_group'])
    def add_to_group(self, user_id: str, group_id: str) -> requests.Response:
        url = self.url(suffix=f"/{user_id}/groups")
        body = {'id': group_id}

        response = self.post(url, json=body)

        return response

    # TODO:
    # following function are not yet implemented in the API itself
    # https://github.com/resource-hub-dev/rhub-api/blob/master/src/rhub/api/auth/user.py

    def remove_from_role(self):
        raise NotImplementedError

    def get_roles(self):
        raise NotImplementedError

    def add_to_role(self):
        raise NotImplementedError
