import requests

from steps.api.base_endpoint import BaseEndpoint
from steps.api.satellite_server_endpoint import SatelliteServerEndpoint


class SatelliteEndpoint(BaseEndpoint):
    """
    Represents the /satellite API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.server = SatelliteServerEndpoint(self.session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/satellite{suffix}"
