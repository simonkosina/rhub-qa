import requests

from api.auth_endpoint import AuthEndpoint
from api.me_endpoint import MeEndpoint
from api.tower_endpoint import TowerEndpoint
from api.policies_endpoint import PoliciesEndpoint
from api.ping_endpoint import PingEndpoint
from api.cowsay_endpoint import CowsayEndpoint


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
        self.tower = TowerEndpoint(self.session)
        self.policies = PoliciesEndpoint(self.session)
        self.ping = PingEndpoint(self.session)
        self.cowsay = CowsayEndpoint(self.session)
        self.me = MeEndpoint(self.session)

    def update_token(self, access_token: str):
        """
        Updates headers with the provided token.
        """

        self.session.headers.update(
            {'Authorization': f'Bearer {access_token}'})
