import requests

from api.base_endpoint import BaseEndpoint
from api.tower_job_endpoint import TowerJobEndpoint
from api.tower_server_endpoint import TowerServerEndpoint


class TowerEndpoint(BaseEndpoint):
    """
    Represents the tower API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.job = TowerJobEndpoint(self.session)
        self.server = TowerServerEndpoint(self.session)

    def url(self, suffix: str) -> str:
        return f"{self.base_url}/tower{suffix}"
