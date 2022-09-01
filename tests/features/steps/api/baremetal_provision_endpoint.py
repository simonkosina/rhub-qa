import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class BaremetalProvisionEndpoint(BaseEndpoint):
    """
    Represents the /bare_metal/provision API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {},
        'get': {},
        'finish': {},
        'get_kickstart': {},
        'get_kickstart_debug_script': {},
        'upload_log': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/bare_metal/provision{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        boot_type: str,
        description: str,
        host_id: int,
        image_id: int,
        kickstart: str,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['finish'])
    def finish(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/finish")
        response = self.post(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_kickstart'])
    def get_kickstart(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/kickstart")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_kickstart_debug_script'])
    def get_kickstart_debug_script(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/kickstart/debug_script")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['upload_log'])
    def upload_log(self, id: int, file: str) -> requests.Response:
        url = self.url(suffix=f"/{id}/logs")
        body = {"file": file}
        response = self.post(url, json=body)

        return response
