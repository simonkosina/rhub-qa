import requests

from steps.api.auth_endpoint import AuthEndpoint
from steps.api.me_endpoint import MeEndpoint
from steps.api.baremetal_endpoint import BaremetalEndpoint
from steps.api.lab_endpoint import LabEndpoint
from steps.api.tower_endpoint import TowerEndpoint
from steps.api.policies_endpoint import PoliciesEndpoint
from steps.api.ping_endpoint import PingEndpoint
from steps.api.cowsay_endpoint import CowsayEndpoint
from steps.api.openstack_endpoint import OpenstackEndpoint
from steps.api.monitor_endpoint import MonitorEndpoint
from steps.api.dns_endpoint import DNSEndpoint
from steps.api.satellite_endpoint import SatelliteEndpoint
from steps.api.scheduler_endpoint import SchedulerEndpoint


class API(object):
    """
    Object containing all the api endpoints.
    """

    def __init__(self):
        """
        Create a request.Session and all the endpoint objects.
        """

        self.session = requests.Session()
        self.auth = AuthEndpoint(self.session)
        self.bare_metal = BaremetalEndpoint(self.session)
        self.lab = LabEndpoint(self.session)
        self.openstack = OpenstackEndpoint(self.session)
        self.monitor = MonitorEndpoint(self.session)
        self.tower = TowerEndpoint(self.session)
        self.policies = PoliciesEndpoint(self.session)
        self.ping = PingEndpoint(self.session)
        self.cowsay = CowsayEndpoint(self.session)
        self.me = MeEndpoint(self.session)
        self.dns = DNSEndpoint(self.session)
        self.satellite = SatelliteEndpoint(self.session)
        self.scheduler = SchedulerEndpoint(self.session)

    def update_token(self, access_token: str):
        """
        Updates headers with the provided token.
        """

        self.session.headers.update(
            {'Authorization': f'Bearer {access_token}'})
