import json
import requests

from api.base_endpoint import BaseEndpoint, log_call
from api.tower_job_endpoint import TowerJobEndpoint


class TowerEndpoint(BaseEndpoint):
    """
    Represents the tower API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.job = TowerJobEndpoint(session)

    def url(self, suffix: str) -> str:
        return f"{self.base_url}/tower{suffix}"
