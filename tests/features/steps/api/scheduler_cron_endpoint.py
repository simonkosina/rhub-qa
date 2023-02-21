import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class SchedulerCronEndpoint(BaseEndpoint):
    """
    Represents the /scheduler/cron API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {'id': IsVerifiable.NO, 'last_run': IsVerifiable.NO},
        'create': {'id': IsVerifiable.NO},
        'delete': {},
        'get': {'id': IsVerifiable.NO, 'last_run': IsVerifiable.NO},
        'update': {'id': IsVerifiable.NO, 'last_run': IsVerifiable.NO}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/scheduler/cron{suffix}"

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
        job_name: str,
        name: str,
        time_expr: str,
        description: str | None = None,
        enabled: bool | None = None,
        job_params: dict | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)
        self.log_cleanup(response, method=self.delete)

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
        job_name: str | None = None,
        name: str | None = None,
        time_expr: str | None = None,
        description: str | None = None,
        enabled: bool | None = None,
        job_params: dict | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        response = self.patch(self.url(f"/{id}"), json=body)
        self.log_cleanup(response, method=self.update,
                         method_args=cleanup_args)

        return response
