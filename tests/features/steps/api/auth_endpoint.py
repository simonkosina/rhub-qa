import requests

from steps.api.base_endpoint import BaseEndpoint, log_call
from steps.api.auth_token_endpoint import AuthTokenEndpoint
from steps.api.auth_group_endpoint import AuthGroupEndpoint
from steps.api.auth_role_endpoint import AuthRoleEndpoint
from steps.api.auth_user_endpoint import AuthUserEndpoint


class AuthEndpoint(BaseEndpoint):
    """
    Represents the auth API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session, admin_session: requests.Session):
        super().__init__(session, admin_session)

        self.token = AuthTokenEndpoint(session, admin_session)
        self.group = AuthGroupEndpoint(session, admin_session)
        self.role = AuthRoleEndpoint(session, admin_session)
        self.user = AuthUserEndpoint(session, admin_session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth{suffix}"
