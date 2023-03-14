import requests
import json
import time

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class LabClusterEndpoint(BaseEndpoint):
    """
    Represents the lab/cluster API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create': {
            '_href': IsVerifiable.NO,
            'created': IsVerifiable.NO,
            'hosts': IsVerifiable.NO,
            'id': IsVerifiable.NO,
            'owner_id': IsVerifiable.NO,
            'owner_name': IsVerifiable.NO,
            'product_id': IsVerifiable.NO,
            'project_id': IsVerifiable.NO,
            'project_name': IsVerifiable.NO,
            'quota': IsVerifiable.NO,
            'quota_usage': IsVerifiable.NO,
            'region_id': IsVerifiable.NO,
            'reservation_expiration': IsVerifiable.NO,
            'lifespan_expiration': IsVerifiable.NO,
            'status': IsVerifiable.NO,
            'status_flag': IsVerifiable.NO
        },
        'delete': {},
        'get': {
            '_href': IsVerifiable.NO,
            'created': IsVerifiable.NO,
            'description': IsVerifiable.NO,
            'hosts': IsVerifiable.NO,
            'id': IsVerifiable.NO,
            'owner_id': IsVerifiable.NO,
            'owner_name': IsVerifiable.NO,
            'product_id': IsVerifiable.NO,
            'project_id': IsVerifiable.NO,
            'project_name': IsVerifiable.NO,
            'quota': IsVerifiable.NO,
            'quota_usage': IsVerifiable.NO,
            'region_id': IsVerifiable.NO,
            'reservation_expiration': IsVerifiable.NO,
            'lifespan_expiration': IsVerifiable.NO,
            'status': IsVerifiable.NO,
            'status_flag': IsVerifiable.NO
        },
        'update': {
            '_href': IsVerifiable.NO,
            'created': IsVerifiable.NO,
            'hosts': IsVerifiable.NO,
            'id': IsVerifiable.NO,
            'owner_id': IsVerifiable.NO,
            'owner_name': IsVerifiable.NO,
            'product_id': IsVerifiable.NO,
            'project_id': IsVerifiable.NO,
            'project_name': IsVerifiable.NO,
            'quota': IsVerifiable.NO,
            'quota_usage': IsVerifiable.NO,
            'region_id': IsVerifiable.NO,
            'reservation_expiration': IsVerifiable.NO,
            'lifespan_expiration': IsVerifiable.NO,
            'status': IsVerifiable.NO,
            'status_flag': IsVerifiable.NO
        },
        'get_authorized_keys': {},
        'get_events': {},
        'delete_hosts': {},
        'get_hosts': {},
        'update_hosts': {},
        'reboot_hosts': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab/cluster{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(
        self,
        filter: dict | None = None,
        sort: str | None = None,
        page: int | None = None,
        limit: int | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', '__class__'])
        params = self.create_params(args)
        response = super().get(self.url(), params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        product_id: int,
        product_params: dict,
        region_id: int,
        description: str | None = None,
        lifespan_expiration: str | None = None,
        project_id: int | None = None,
        quota: dict | None = None,
        quota_usage: dict | None = None,
        reservation_expiration: str | None = None,
        shared: bool | None = None,
        status: str | None = None,
    ) -> requests.Response:
        # Cleanup is done in the 'fixtures.py' file as part of rhub_api() fixture
        # This means clusters are deleted only between features and not between scenarios
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)

        response = self.post(url=self.url(), json=body)

        self.log_cluster_creation(response)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: int, as_cleanup: bool = False) -> requests.Response:
        if as_cleanup:
            # the cluster must first be active to delete it as part of a test cleanup
            while True:
                resp = self.get(id)
                resp.raise_for_status()

                cluster = resp.json()

                if cluster["status_flag"] != "creating":
                    break

                time.sleep(15)

        response = super().delete(url=self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        response = super().get(url=self.url(suffix=f"/{id}"))

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: int,
        name: str | None = None,
        product_id: int | None = None,
        product_params: dict | None = None,
        region_id: int | None = None,
        description: str | None = None,
        lifespan_expiration: str | None = None,
        project_id: int | None = None,
        quota: dict | None = None,
        quota_usage: dict | None = None,
        reservation_expiration: str | None = None,
        shared: bool | None = None,
        status: str | None = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        response = self.patch(url=self.url(suffix=f"/{id}"), json=body)
        self.log_cleanup(response, method=self.update,
                         method_args=cleanup_args)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_authorized_keys'])
    def get_authorized_keys(self, id: int) -> requests.Response:
        url = self.url(f"/{id}/authorized_keys")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_events'])
    def get_events(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/events")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete_hosts'])
    def delete_hosts(self, id: int) -> requests.Response:
        original_hosts_resp = self.get_hosts(id)

        url = self.url(suffix=f"/{id}/hosts")
        response = super().delete(url)

        try:
            original_hosts_resp.raise_for_status()

            try:
                original_hosts = original_hosts_resp.json()
            except json.JSONDecodeError:
                # empty string returned
                original_hosts = []

            self.log_cleanup(
                response,
                method=self.update_hosts,
                method_args={"id": id, "hosts": original_hosts},
                find_id=False)

        except requests.HTTPError:
            # update request failed, no cleanup needed
            pass

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_hosts'])
    def get_hosts(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/hosts")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update_hosts'])
    def update_hosts(self, id: int, hosts: list[dict]) -> requests.Response:
        original_hosts_resp = self.get_hosts(id)

        url = self.url(suffix=f"/{id}/hosts")
        response = super().post(url, json=hosts)

        try:
            original_hosts_resp.raise_for_status()

            try:
                original_hosts = original_hosts_resp.json()
            except json.JSONDecodeError:
                # empty string returned
                original_hosts = []

            self.log_cleanup(
                response,
                method=self.update_hosts,
                method_args={"id": id, "hosts": original_hosts},
                find_id=False)

        except requests.HTTPError:
            # update request failed, no cleanup needed
            pass

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['reboot_hosts'])
    def reboot_hosts(self, id: int, hosts: str | list[dict] | None = None, reboot_type: str | None = None) -> requests.Response:
        body = {}

        if hosts is not None:
            body['hosts'] = hosts
        if reboot_type is not None:
            body['type'] = reboot_type

        url = self.url(suffix=f"/{id}/reboot")
        response = super().post(url, json=body)

        return response
