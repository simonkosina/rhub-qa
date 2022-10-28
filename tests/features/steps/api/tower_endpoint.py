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

    def __init__(self, session: requests.Session, admin_session: requests.Session):
        super().__init__(session, admin_session)

        self.job = TowerJobEndpoint(session, admin_session)
        self.server = TowerServerEndpoint(session, admin_session)
        self.template = TowerTemplateEndpoint(session, admin_session)
        self.webhook_notification = TowerWebhookNotification(session, admin_session)

    def url(self, suffix: str) -> str:
        return f"{self.base_url}/tower{suffix}"
