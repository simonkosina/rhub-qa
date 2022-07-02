from api.base_endpoint import BaseEndpoint, log_call


class AuthEndpoint(BaseEndpoint):
    """
    Represents the auth API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        "create_token": {}
    }

    def auth_url(self, suffix: str):
        """
        Create an URL for the auth endpoint.

        Arguments
        ---------
        suffix: str
            String appended at the end of the url.

        Returns
        -------
        str
            Created url.
        """

        return f"{self.base_url}/auth/{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS["create_token"])
    def create_token(self, auth: tuple):
        """
        Login and get access token.

        Arguments
        ---------
        auth: tuple
            Auth tuple for basic HTTP authentication.

        Returns 
        -------
        Response
            API response.
        """

        url = self.auth_url(suffix='token/create')
        response = self.post(url, auth=auth)

        return response
