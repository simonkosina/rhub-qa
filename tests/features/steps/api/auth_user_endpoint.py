import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class AuthUserEndpoint(BaseEndpoint):
    """
    Represents the auth/user API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'get': {'created_at': IsVerifiable.NO, 'updated_at': IsVerifiable.NO},
        'get_ssh_keys': {},
        'get_tokens': {},
        'create_token': {'created_at': IsVerifiable.NO, 'id': IsVerifiable.NO, 'token': IsVerifiable.NO},
        'delete_token': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/user{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(url=self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_ssh_keys'])
    def get_ssh_keys(self, id: int) -> requests.Response:
        url = self.url(f"/{id}/ssh_keys")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_tokens'])
    def get_tokens(self, id: int) -> requests.Response:
        url = self.url(f"/{id}/token")
        response = super().get(url)

        return response
    
    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create_token'])
    def create_token(
        self,
        id: int,
        name: str | None = None,
        expires_at: str | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id', '__class__'])
        body = self.create_body(args)

        url = self.url(f"/{id}/token")
        response = super().post(url, json=body)
        
        # need to properly log the user_id and token_id for delete_token
        try:
            response.raise_for_status()
            
            self.log_cleanup(
                response,
                method=self.delete_token,
                method_args={
                    'user_id': id,
                    'token_id': response.json()['id']
                },
                find_id=False
            )
        except requests.HTTPError:
            pass

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete_token'])
    def delete_token(self, user_id: int, token_id: int) -> requests.Response:
        url = self.url(f"/{user_id}/token/{token_id}")
        response = super().delete(url)

        return response
