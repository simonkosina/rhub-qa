import functools
import copy
import requests

from pyclbr import Function
from enum import Enum, auto

class IsVerifiable(Enum):
    NO = auto()
    NOT_REQUIRED = auto()


class APILogger(object):
    """
    Logs the API calls.
    """

    def __init__(self):
        self.responses = []
        self.unverifiable_items = []
        self.__cleanups = []

    def log_response(self, response: requests.Response):
        self.responses.append(response)

    def log_unverfiable_items(self, item: dict):
        self.unverifiable_items.append(item)

    def log_cleanup(self, method: Function, **kwargs):
        self.__cleanups.append({
            'method': method,
            'kwargs': kwargs
        })

    def reset_cleanups(self):
        self.__cleanups = []

    @property
    def cleanups(self) -> list:
        return self.__cleanups[::-1]

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

    LOGGER = APILogger()

    def __init__(self, session: requests.Session, admin_session: requests.Session):
        self.base_url = f"{self.HOSTNAME}:{self.PORT}{self.PATH}"
        self.session = session
        self.__admin_session = admin_session
        self.__test_session = None
        self.__is_admin = False

    def delete(self, url: str, **kwargs) -> requests.Response:
        """
        Send a DELETE request.
        """

        r = self.session.delete(url, timeout=self.TIMEOUT,
                                verify=self.VERIFY, **kwargs)

        return r

    def get(self, url: str, **kwargs) -> requests.Response:
        """
        Send a GET request.
        """

        r = self.session.get(url, timeout=self.TIMEOUT,
                             verify=self.VERIFY, **kwargs)

        return r

    def post(self, url: str, **kwargs) -> requests.Response:
        """
        Send a POST request.
        """

        r = self.session.post(url, timeout=self.TIMEOUT,
                              verify=self.VERIFY, **kwargs)

        return r

    def patch(self, url: str, **kwargs) -> requests.Response:
        """
        Send a PATCH request.
        """

        r = self.session.patch(url, timeout=self.TIMEOUT,
                               verify=self.VERIFY, **kwargs)

        return r

    def get_function_arguments(self, local_vars: dict, skip_args: list[str] = []) -> dict:
        """
        Returns a dictionary containing the arguments that the function was called with.
        `local_vars` is expected to be a result of calling `locals()` at the beginning of a function.
        """

        args = copy.deepcopy(local_vars)

        for key in skip_args:
            del args[key]

        return args

    def create_body(self, args: dict) -> dict:
        """
        Takes arguments that the function's been called with and creates a request
        body.
        """

        body = {}

        for key, value in args.items():
            if value is not None:
                body[key] = value

        return body

    def create_params(self, args: dict) -> dict:
        """
        Takes arguments that the function's been called with and creates request parameters.
        """

        if 'filter' in args and args['filter'] is not None:
            args['filter'] = self.serialize_filter(args['filter'])

        params = {}

        for key, value in args.items():
            if value is not None:
                params[key] = value

        return params

    def get_values_before_update(self, method: Function, id: str, update_args: dict) -> dict:
        """
        Call the provided method with the given id to retrieve current data and filter it 
        to contain only the items that will be updated. Function returns the current 
        keys and value pairs for the to be updated items.
        """

        self.execute_as_admin()

        response = method(id=id)
        response.raise_for_status()

        self.execute_as_test()

        data = response.json()
        res = {}

        for key, value in update_args.items():
            if key not in {'self', 'id'} and value:
                res[key] = data[key]

        return res

    def serialize_filter(self, filter: dict) -> str:
        """
        Serializes the provided filter dictionary into a string that can be used
        as a parameter when creating a request.
        """

        parts = []

        for key, value in filter.items():
            parts.append(key)

            if type(value) is bool:
                value = str(value).lower()

            parts.append(value)

        res = ','.join(parts)

        return res

    def execute_as_admin(self):
        """
        Authorize as an admin.
        """

        if not self.__is_admin:
            self.__is_admin = True
            self.__test_session = self.session
            self.session = self.__admin_session

    def execute_as_test(self):
        """
        Authorize as the user in the tests.
        """

        if self.__is_admin:
            self.__is_admin = False
            self.session = self.__test_session
