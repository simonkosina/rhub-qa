import requests

from steps.api.base_endpoint import BaseEndpoint, log_call
from steps.api.lab_cluster_endpoint import LabClusterEndpoint
from steps.api.lab_cluster_event_endpoint import LabClusterEventEndpoint
from steps.api.lab_location_endpoint import LabLocationEndpoint
from steps.api.lab_region_endpoint import LabRegionEndpoint
from steps.api.lab_product_endpoint import LabProductEndpoint


class LabEndpoint(BaseEndpoint):
    """
    Represents the lab API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session, admin_session: requests.Session):
        super().__init__(session, admin_session)

        self.cluster = LabClusterEndpoint(session, admin_session)
        self.cluster_event = LabClusterEventEndpoint(session, admin_session)
        self.location = LabLocationEndpoint(self.session, admin_session)
        self.region = LabRegionEndpoint(session, admin_session)
        self.product = LabProductEndpoint(session, admin_session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab{suffix}"
