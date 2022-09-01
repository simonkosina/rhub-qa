import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class TowerWebhookNotification(BaseEndpoint):
    """
    Represents the tower/webhook_notification API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'create': {},
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/tower/webhook_notification{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        body: str = None,
        created_by: str = None,
        credential: str = None,
        extra_vars: str = None,
        finished: str = None,
        hosts: str = None,
        id: str = None,
        inventory: str = None,
        limit: str = None,
        name: str = None,
        playbook: str = None,
        project: str = None,
        started: str = None,
        status: str = None,
        traceback: str = None,
        url: str = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        response = self.post(self.url(), json=self.create_body(args))

        return response
