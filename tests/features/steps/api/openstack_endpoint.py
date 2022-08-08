import requests

from api.base_endpoint import BaseEndpoint
from api.openstack_cloud_endpoint import OpenstackCloudEndpoint
from api.openstack_project_endpoint import OpenstackProjectEndpoint


class OpenstackEndpoint(BaseEndpoint):
    """
    Represents the OpenStack API endpoint.
    """

    def __init__(self, session: requests.Session):
        super().__init__(session)

        self.cloud = OpenstackCloudEndpoint(self.session)
        self.project = OpenstackProjectEndpoint(self.session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/openstack{suffix}"
