import functools
import requests


class APILogger(object):
    """
    Logs the API calls.
    """

    def __init__(self):
        self.responses = []
        self.unverifiable_items = []

    def log_response(self, response: requests.Response):
        self.responses.append(response)

    def log_unverfiable_items(self, item: dict):
        self.unverifiable_items.append(item)

    @property
    def last_response(self) -> requests.Response | None:
        if self.responses:
            return self.responses[-1]

    @property
    def last_unverifiable_items(self) -> dict | None:
        if self.unverifiable_items:
            return self.unverifiable_items[-1]


def log_call(logger: APILogger, unverifiable_items: dict):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            logger.log_response(response)
            logger.log_unverfiable_items(unverifiable_items)

            return response
        return wrapper
    return decorator_log


class BaseEndpoint(object):
    """
    Base object providing some basic functions for all the inheriting API endoints.
    """

    # HOSTNAME = 'https://rhub-api-resource-hub-qe.apps.ocp-c1.prod.psi.redhat.com'
    # PORT = 443
    HOSTNAME = 'http://localhost'
    PORT = '8081'
    PATH = '/v0'

    TIMEOUT = 10
    VERIFY = False
    AUTH = ('testuser1', 'testuser1')

    LOGGER = APILogger()

    def __init__(self, session: requests.Session):
        self.base_url = f"{self.HOSTNAME}:{self.PORT}{self.PATH}"
        self.session = session

    def delete(self, url: str, **kwargs) -> requests.Response:
        """
        Send a DELETE request.
        """

        r = self.session.delete(url, timeout=self.TIMEOUT,
                                verify=self.VERIFY, **kwargs)
        r.raise_for_status()

        return r

    def get(self, url: str, **kwargs) -> requests.Response:
        """
        Send a GET request.
        """

        r = self.session.get(url, timeout=self.TIMEOUT,
                             verify=self.VERIFY, **kwargs)
        r.raise_for_status()

        return r

    def post(self, url: str, **kwargs) -> requests.Response:
        """
        Send a POST request.
        """

        r = self.session.post(url, timeout=self.TIMEOUT,
                              verify=self.VERIFY, **kwargs)
        r.raise_for_status()

        return r

    def patch(self, url: str, **kwargs) -> requests.Response:
        """
        Send a PATCH request.
        """

        r = self.session.patch(url, timeout=self.TIMEOUT,
                               verify=self.VERIFY, **kwargs)
        r.raise_for_status()

        return r
