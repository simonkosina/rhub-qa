import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class TowerTemplateEndpoint(BaseEndpoint):
    """
    Represents the tower/template API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {'id': IsVerifiable.NO},
        'create': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'delete': {},
        'get': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO, '_href': IsVerifiable.NO},
        'get_jobs': {},
        'launch': {'created_at': IsVerifiable.NO, 'started_at': IsVerifiable.NO, 'finished_at': IsVerifiable.NO}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/tower/template{suffix}"

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
        response = super().get(self.url(), params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        server_id: int,
        tower_template_id: int,
        tower_template_is_workflow: bool,
        description: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        
        response = self.post(self.url(), json=body)

        try:
            response.raise_for_status()
            id = response.json()['id']
            BaseEndpoint.LOGGER.log_cleanup(self.delete, id=id)
        except requests.HTTPError:
            pass

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
        name: str | None = None,
        server_id: int | None = None,
        tower_template_id: int | None = None,
        tower_template_is_workflow: bool | None = None,
        description: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)

        response = self.patch(self.url(suffix=f"/{id}"), json=body)

        try:
            response.raise_for_status()
            BaseEndpoint.LOGGER.log_cleanup(self.update, id=id, **cleanup_args)
        except requests.HTTPError:
            pass

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_jobs'])
    def get_jobs(
        self,
        id: int, filter: dict | None = None,
        page: str | None = None,
        limit: str | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', '__class__', 'id'])
        params = self.create_params(args)
        url = self.url(suffix=f"/{id}/jobs")
        response = super().get(url, params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['launch'])
    def launch(
        self,
        id: int,
        extra_vars: dict | None = None
    ) -> requests.Response:
        url = self.url(suffix=f"/{id}/launch")
        body = {'extra_vars': extra_vars}
        response = self.post(url, json=body)

        return response
