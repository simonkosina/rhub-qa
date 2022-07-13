import json

from api.base_endpoint import BaseEndpoint


class TowerEndpoint(BaseEndpoint):
    """
    Represents the tower API endpoint.
    """

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

        return response.json()
