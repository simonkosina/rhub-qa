import requests

from helpers.auth_endpoint_api import AuthEndpointAPI
from helpers.tower_endpoint_api import TowerEndpointAPI


class API(object):
    """
    Object containing all the api endpoints.
    """

    def __init__(self):
        """
        Create a request.Session and all the endpoint objects.
        """

        self.session = requests.Session()
        self.auth = AuthEndpointAPI(self.session)
        self.tower = TowerEndpointAPI(self.session)

    def update_token(self, token):
        """
        Updates headers with the provided token.
        """

        self.session.headers.update({'Authorization': f'Bearer {token}'})
