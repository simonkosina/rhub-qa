import requests

from steps.api.base_endpoint import BaseEndpoint
from steps.api.tower_job_endpoint import TowerJobEndpoint
from steps.api.tower_server_endpoint import TowerServerEndpoint
from steps.api.tower_template_endpoint import TowerTemplateEndpoint
from steps.api.tower_webhook_notification_endpoint import TowerWebhookNotification


class TowerEndpoint(BaseEndpoint):
    """
    Represents the tower API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.job = TowerJobEndpoint(self.session)
        self.server = TowerServerEndpoint(self.session)
        self.template = TowerTemplateEndpoint(self.session)
        self.webhook_notification = TowerWebhookNotification(self.session)

    def url(self, suffix: str) -> str:
        return f"{self.base_url}/tower{suffix}"
