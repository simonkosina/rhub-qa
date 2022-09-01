import requests

from steps.api.base_endpoint import BaseEndpoint
from steps.api.dns_server_endpoint import DNSServerEndpoint


class DNSEndpoint(BaseEndpoint):
    """
    Represents the /dns API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.server = DNSServerEndpoint(self.session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/dns{suffix}"

