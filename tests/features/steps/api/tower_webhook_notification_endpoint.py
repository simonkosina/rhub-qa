import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


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
        body: str | None = None,
        created_by: str | None = None,
        credential: str | None = None,
        extra_vars: str | None = None,
        finished: str | None = None,
        hosts: str | None = None,
        id: str | None = None,
        inventory: str | None = None,
        limit: str | None = None,
        name: str | None = None,
        playbook: str | None = None,
        project: str | None = None,
        started: str | None = None,
        status: str | None = None,
        traceback: str | None = None,
        url: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        response = self.post(self.url(), json=self.create_body(args))

        return response
