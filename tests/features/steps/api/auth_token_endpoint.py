import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class AuthTokenEndpoint(BaseEndpoint):
    """
    Represents the auth/token API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get': {'exp': True, 'iat': True, 'jti': True, 'session_state': True, 'sid': True},
        'create': {'access_token': True, 'session_state': True, 'refresh_token': True},
        'refresh': {'access_token': True, 'session_state': True, 'refresh_token': True}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/token{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(self, auth: tuple) -> requests.Response:
        url = self.url(suffix='/create')
        response = self.post(url, auth=auth)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['refresh'])
    def refresh(self, refresh_token: str) -> requests.Response:
        # Replace access token with refresh token
        self.session.headers.update(
            {'Authorization': f'Bearer {refresh_token}'})

        url = self.url(suffix='/refresh')
        response = self.post(url)

        return response
