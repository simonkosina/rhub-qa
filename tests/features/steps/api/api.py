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
from steps.api.base_endpoint import IsVerifiable, APILogger

from base64 import b64encode


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

    def __init__(self, admin_token: str, api_url: str):
        """
        Create a request.Session and all the endpoint objects.
        """

        self.api_url = api_url
        self.session = requests.Session()
        self.admin_session = requests.Session()

        self.auth = AuthEndpoint(self.session, self.admin_session, self.api_url)
        self.bare_metal = BaremetalEndpoint(self.session, self.admin_session, self.api_url)
        self.lab = LabEndpoint(self.session, self.admin_session, self.api_url)
        self.openstack = OpenstackEndpoint(self.session, self.admin_session, self.api_url)
        self.monitor = MonitorEndpoint(self.session, self.admin_session, self.api_url)
        self.tower = TowerEndpoint(self.session, self.admin_session, self.api_url)
        self.policies = PoliciesEndpoint(self.session, self.admin_session, self.api_url)
        self.ping = PingEndpoint(self.session, self.admin_session, self.api_url)
        self.cowsay = CowsayEndpoint(self.session, self.admin_session, self.api_url)
        self.me = MeEndpoint(self.session, self.admin_session, self.api_url)
        self.dns = DNSEndpoint(self.session, self.admin_session, self.api_url)
        self.satellite = SatelliteEndpoint(self.session, self.admin_session, self.api_url)
        self.scheduler = SchedulerEndpoint(self.session, self.admin_session, self.api_url)

        # Setup authorization for the admin session
        self.update_token(token=admin_token, session=self.admin_session)

    def update_token(self, token: str, session: requests.Session | None = None):
        """
        Updates headers with the provided token.
        """

        auth_string = b64encode(f"__token__:{token}".encode()).decode()
        

        if not session:
            self.session.headers.update(
                {'Authorization': f'Basic {auth_string}'})
        else:
            session.headers.update(
                {'Authorization': f'Basic {auth_string}'})

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger: APILogger):
        self._logger = logger

    @property
    def request_data(self):
        return self._request_data
    
    @request_data.setter
    def request_data(self, data: dict):
        self._request_data = data

    @property
    def response_data(self):
        return self._response_data

    @response_data.setter
    def response_data(self, data: dict):
        self._response_data = data
        
    def cleanup(self):
        self.session.close()
        self.admin_session.close()
