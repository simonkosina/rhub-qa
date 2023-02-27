import requests

from steps.api.base_endpoint import BaseEndpoint, log_call
from steps.api.auth_group_endpoint import AuthGroupEndpoint
from steps.api.auth_user_endpoint import AuthUserEndpoint


class AuthEndpoint(BaseEndpoint):
    """
    Represents the auth API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session, admin_session: requests.Session, base_url: str):
        super().__init__(session, admin_session, base_url)

        self.group = AuthGroupEndpoint(session, admin_session, base_url)
        self.user = AuthUserEndpoint(session, admin_session, base_url)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth{suffix}"
