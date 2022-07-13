import requests

from api.base_endpoint import BaseEndpoint, log_call


class AuthEndpoint(BaseEndpoint):
    """
    Represents the auth API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        "create_token": {}
    }

    def auth_url(self, suffix: str) -> str:
        """
        Create an URL for the auth endpoint.
        """

        return f"{self.base_url}/auth{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS["create_token"])
    def create_token(self, auth: tuple) -> requests.Response:
        """
        Login and get access token.
        """

        url = self.auth_url(suffix='/token/create')
        response = self.post(url, auth=auth)

        return response
