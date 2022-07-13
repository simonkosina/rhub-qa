import json
import requests

from api.base_endpoint import BaseEndpoint, log_call


class TowerEndpoint(BaseEndpoint):
    """
    Represents the tower API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        "list_jobs": {}
    }

    def tower_url(self, suffix: str) -> str:
        """
        Create an URL for the tower endpoint.
        """

        return f"{self.base_url}/tower{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS["list_jobs"])
    def list_jobs(self, filter: dict = None, page: str = None, limit: str = None) -> requests.Response:
        """
        List tower jobs.
        """

        params = {}

        if filter:
            params["filter"] = json.dumps(filter)

        if page:
            params["page"] = page

        if limit:
            params["limit"] = limit

        url = self.tower_url(suffix='/job')
        response = self.get(url, params=params)

        return response
