HOSTNAME = 'https://rhub-api-resource-hub-qe.apps.ocp-c1.prod.psi.redhat.com'
PORT = 443
PATH = '/v0'

TIMEOUT = 10
VERIFY = False


class BaseAPI(object):
    """
    Base object providing some basic functions for all the inheriting API endoints.
    """

    def __init__(self, session):
        self.base_url = f"{HOSTNAME}:{PORT}{PATH}"
        self.session = session

    def delete(self, url: str, **kwargs):
        """
        Send a DELETE request.

        Arguments
        ---------
        url: str
            Url to send the request to.
        **kwargs
            Optional arguments that request takes.

        Returns
        -------
        Response
            Response object.
        """
        
        r = self.session.delete(url, timeout=TIMEOUT, verify=VERIFY, **kwargs)
        r.raise_for_status()

        return r

    def get(self, url: str, **kwargs):
        """
        Send a GET request.

        Arguments
        ---------
        url: str
            Url to send the request to.
        **kwargs
            Optional arguments that request takes.

        Returns
        -------
        Response
            Response object.
        """

        r = self.session.get(url, timeout=TIMEOUT, verify=VERIFY, **kwargs)
        r.raise_for_status()

        return r

    def post(self, url: str, **kwargs):
        """
        Send a POST request.

        Arguments
        ---------
        url: str
            Url to send the request to.
        **kwargs
            Optional arguments that request takes.

        Returns
        -------
        Response
            Response object.
        """

        r = self.session.post(url, timeout=TIMEOUT, verify=VERIFY, **kwargs)
        r.raise_for_status()

        return r

    def patch(self, url: str, **kwargs):
        """
        Send a PATCH request.

        Arguments
        ---------
        url: str
            Url to send the request to.
        **kwargs
            Optional arguments that request takes.

        Returns
        -------
        Response
            Response object.
        """

        r = self.session.patch(url, timeout=TIMEOUT, verify=VERIFY, **kwargs)
        r.raise_for_status()

        return r
