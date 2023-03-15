import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class AuthGroupEndpoint(BaseEndpoint):
    """
    Represents the auth/group API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'get': {'id': IsVerifiable.NO},
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/group{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(
        self,
        filter: dict | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', '__class__'])
        params = self.create_params(args)
        response = super().get(url=self.url(), params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: str) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response
