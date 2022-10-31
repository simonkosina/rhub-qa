import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable

class AuthRoleEndpoint(BaseEndpoint):
    """
    Represents the auth/role API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {'description': IsVerifiable.NOT_REQUIRED, 'attributes': IsVerifiable.NOT_REQUIRED},
        'create': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'delete': {},
        'get': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/auth/role{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        attributes: dict = None,
        clientRole: bool = None,
        composite: bool = None,
        composites: dict = None,
        containerId: str = None,
        description: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)

        response = self.post(url=self.url(), json=body)

        try:
            response.raise_for_status()
            name = response.json()['name']
            BaseEndpoint.LOGGER.log_cleanup(self.delete, id=name)
        except requests.HTTPError:
            pass

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: str) -> requests.Response:
        response = super().delete(self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: str) -> requests.Response:
        response = super().get(self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: str,
        name: str = None,
        attributes: dict = None,
        clientRole: bool = None,
        composite: bool = None,
        composites: dict = None,
        containerId: str = None,
        description: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)

        response = self.patch(url=self.url(suffix=f"/{id}"), json=body)

        if name:
            new_id = name
        else:
            new_id = cleanup_args['id'] 

        try:
            response.raise_for_status()
            BaseEndpoint.LOGGER.log_cleanup(self.update, id=new_id, **cleanup_args)
        except requests.HTTPError:
            pass

        return response
