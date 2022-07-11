import requests

from api.auth_endpoint import AuthEndpoint
from api.tower_endpoint import TowerEndpoint


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

    def update_token(self, token):
        """
        Updates headers with the provided token.
        """

        self.session.headers.update({'Authorization': f'Bearer {token}'})
