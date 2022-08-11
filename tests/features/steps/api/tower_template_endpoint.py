import requests

from api.base_endpoint import BaseEndpoint, log_call


class TowerTemplateEndpoint(BaseEndpoint):
    """
    Represents the tower/template API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {'id': True},
        'delete': {},
        'get': {},
        'update': {},
        'get_jobs': {},
        'launch': {'created_at': True, 'started_at': True, 'finished_at': True}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/tower/template{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(
        self,
        filter: dict = None,
        sort: str = None,
        page: int = None,
        limit: int = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', '__class__'])
        params = self.create_params(args)
        response = super().get(self.url(), params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        server_id: int,
        tower_template_id: int,
        tower_template_is_workflow: bool,
        description: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().delete(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: int,
        name: str = None,
        server_id: int = None,
        tower_template_id: int = None,
        tower_template_is_workflow: bool = None,
        description: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        response = self.patch(self.url(suffix=f"/{id}"), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_jobs'])
    def get_jobs(self, id: int, filter: dict = None, page: str = None, limit: str = None) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', '__class__', 'id'])
        params = self.create_params(args)
        url = self.url(suffix=f"/{id}/jobs")
        response = super().get(url, params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['launch'])
    def launch(self, id: int, extra_vars: dict = None) -> requests.Response:
        url = self.url(suffix=f"/{id}/launch")
        body = {'extra_vars': extra_vars}
        response = self.post(url, json=body)

        return response
