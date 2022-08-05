import requests

from api.base_endpoint import BaseEndpoint, log_call
from api.auth_token_endpoint import AuthTokenEndpoint
from api.auth_group_endpoint import AuthGroupEndpoint
from api.auth_role_endpoint import AuthRoleEndpoint
from api.auth_user_endpoint import AuthUserEndpoint


class AuthEndpoint(BaseEndpoint):
    """
    Represents the auth API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.token = AuthTokenEndpoint(session)
        self.group = AuthGroupEndpoint(session)
        self.role = AuthRoleEndpoint(session)
        self.user = AuthUserEndpoint(session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth{suffix}"
