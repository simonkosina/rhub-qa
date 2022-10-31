import copy
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
from steps.api.base_endpoint import IsVerifiable


def filter_dict(dictionary: dict, keys_to_remove: dict) -> dict:
    """
    Removes keys from the original dictionary which are not compared during verification.
    """

    dict_copy = copy.deepcopy(dictionary)

    for k, v in keys_to_remove.items():
        if type(v) is dict:
            # recursively remove nested fields
            filter_dict(dict_copy[k], v)
        elif v is IsVerifiable.NO:
            del dict_copy[k]
        elif v is IsVerifiable.NOT_REQUIRED:
            if k in dict_copy.keys():
                del dict_copy[k]

    return dict_copy


class API(object):
    """
    Object containing all the api endpoints.
    """

    def __init__(self, admin_auth: tuple):
        """
        Create a request.Session and all the endpoint objects.
        """

        self.session = requests.Session()
        self.admin_session = requests.Session()

        self.auth = AuthEndpoint(self.session, self.admin_session)
        self.bare_metal = BaremetalEndpoint(self.session, self.admin_session)
        self.lab = LabEndpoint(self.session, self.admin_session)
        self.openstack = OpenstackEndpoint(self.session, self.admin_session)
        self.monitor = MonitorEndpoint(self.session, self.admin_session)
        self.tower = TowerEndpoint(self.session, self.admin_session)
        self.policies = PoliciesEndpoint(self.session, self.admin_session)
        self.ping = PingEndpoint(self.session, self.admin_session)
        self.cowsay = CowsayEndpoint(self.session, self.admin_session)
        self.me = MeEndpoint(self.session, self.admin_session)
        self.dns = DNSEndpoint(self.session, self.admin_session)
        self.satellite = SatelliteEndpoint(self.session, self.admin_session)
        self.scheduler = SchedulerEndpoint(self.session, self.admin_session)

        # Setup authorization for the admin session
        response = self.auth.token.create(admin_auth[0], admin_auth[1])
        response.raise_for_status()

        admin_token = response.json()['access_token']
        self.update_token(access_token=admin_token, session=self.admin_session)

    def update_token(self, access_token: str, session: requests.Session = None):
        """
        Updates headers with the provided token.
        """

        if not session:
            self.session.headers.update(
                {'Authorization': f'Bearer {access_token}'})
        else:
            session.headers.update(
                {'Authorization': f'Bearer {access_token}'})

    def cleanup(self):
        self.session.close()
        self.admin_session.close()
