import requests

from api.base_endpoint import BaseEndpoint
from api.scheduler_cron_endpoint import SchedulerCronEndpoint


class SchedulerEndpoint(BaseEndpoint):
    """
    Represents the /scheduler API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.cron = SchedulerCronEndpoint(self.session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/scheduler{suffix}"
