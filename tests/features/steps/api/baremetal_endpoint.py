import requests

from steps.api.base_endpoint import BaseEndpoint
from steps.api.baremetal_handler_endpoint import BaremetalHandlerEndpoint
from steps.api.baremetal_host_endpoint import BaremetalHostEndpoint
from steps.api.baremetal_image_endpoint import BaremetalImageEndpoint
from steps.api.baremetal_provision_endpoint import BaremetalProvisionEndpoint


class BaremetalEndpoint(BaseEndpoint):
    """
    Represents the /bare_metal API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.handler = BaremetalHandlerEndpoint(self.session)
        self.host = BaremetalHostEndpoint(self.session)
        self.image = BaremetalImageEndpoint(self.session)
        self.provision = BaremetalProvisionEndpoint(self.session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/bare_metal{suffix}"
