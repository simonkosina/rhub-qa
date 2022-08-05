import requests

from api.base_endpoint import BaseEndpoint, log_call
from api.lab_cluster_endpoint import LabClusterEndpoint
from api.lab_cluster_event_endpoint import LabClusterEventEndpoint
from api.lab_location_endpoint import LabLocationEndpoint
from api.lab_region_endpoint import LabRegionEndpoint
from api.lab_product_endpoint import LabProductEndpoint


class LabEndpoint(BaseEndpoint):
    """
    Represents the lab API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.cluster = LabClusterEndpoint(self.session)
        self.cluster_event = LabClusterEventEndpoint(self.session)
        self.location = LabLocationEndpoint(self.session)
        self.region = LabRegionEndpoint(self.session)
        self.product = LabProductEndpoint(self.session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab{suffix}"
