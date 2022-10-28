import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class AuthTokenEndpoint(BaseEndpoint):
    """
    Represents the auth/token API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get': {'exp': IsVerifiable.NOT_REQUIRED, 'iat': IsVerifiable.NOT_REQUIRED, 'jti': IsVerifiable.NOT_REQUIRED, 'session_state': IsVerifiable.NOT_REQUIRED, 'sid': IsVerifiable.NO},
        'create': {'access_token': IsVerifiable.NO, 'session_state': IsVerifiable.NO, 'refresh_token': IsVerifiable.NO},
        'refresh': {'access_token': IsVerifiable.NO, 'session_state': IsVerifiable.NO, 'refresh_token': IsVerifiable.NO}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/token{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(self, username: str, password: str) -> requests.Response:
        auth = (username, password)
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
