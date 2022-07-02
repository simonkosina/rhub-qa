import json

from api.base_endpoint import BaseEndpoint, log_call


class TowerEndpoint(BaseEndpoint):
    """
    Represents the tower API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        "list_jobs": {}
    }

    def tower_url(self, suffix: str):
        """
        Create an URL for the tower endpoint.

        Arguments
        ---------
        suffix: str
            String appended at the end of the url.

        Returns
        -------
        str
            Created url.
        """

        return f"{self.base_url}/tower/{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS["list_jobs"])
    def list_jobs(self, filter: dict = None, page: int = None, limit: int = None):
        """
        List tower jobs.

        Arguments
        ---------
        filter: dict
            Filter jobs by attributes.
        page: int
            Page number.
        limit: int
            Limit.

        Returns
        -------
        dict
            Tower jobs.
        """

        params = {}

        if filter:
            params["filter"] = json.dumps(filter)

        if page:
            params["page"] = page

        if limit:
            params["limit"] = limit

        url = self.tower_url(suffix='job')
        response = self.get(url, params=params)

        return response
