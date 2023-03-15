import requests

from steps.api.base_endpoint import BaseEndpoint, log_call, IsVerifiable


class LabRegionEndpoint(BaseEndpoint):
    """
    Represents the lab/region API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {'_href': IsVerifiable.NO},
        'create': {
            '_href': IsVerifiable.NO,
            'id': IsVerifiable.NO,
            'dns_id': IsVerifiable.NO,
            'location_id': IsVerifiable.NO,
            'openstack': IsVerifiable.NO,
            'openstack_id': IsVerifiable.NO,
            'owner_group_id': IsVerifiable.NO,
            'satellite_id': IsVerifiable.NO,
            'tower_id': IsVerifiable.NO
        },
        'get_usage_all': {},
        'delete': {},
        'get': {
            '_href': IsVerifiable.NO,
            'id': IsVerifiable.NO,
            'dns_id': IsVerifiable.NO,
            'location_id': IsVerifiable.NO,
            'openstack': IsVerifiable.NO,
            'openstack_id': IsVerifiable.NO,
            'owner_group_id': IsVerifiable.NO,
            'satellite_id': IsVerifiable.NO,
            'tower_id': IsVerifiable.NO
        },
        'update': {
            '_href': IsVerifiable.NO,
            'id': IsVerifiable.NO,
            'dns_id': IsVerifiable.NO,
            'location_id': IsVerifiable.NO,
            'openstack': IsVerifiable.NO,
            'openstack_id': IsVerifiable.NO,
            'owner_group_id': IsVerifiable.NO,
            'satellite_id': IsVerifiable.NO,
            'tower_id': IsVerifiable.NO
        },
        'remove_product': {},
        'get_products': {},
        'update_products': {},
        'get_usage': {
            "total_quota": IsVerifiable.NO, # can be null
            "total_quota_usage": {
                "num_vcpus": IsVerifiable.NO,
                "num_volumes": IsVerifiable.NO,
                "ram_mb": IsVerifiable.NO,
                "volumes_gb": IsVerifiable.NO
            },
            "user_quota": IsVerifiable.NO, # can be null
            "user_quota_usage": {
                "num_vcpus": IsVerifiable.NO,
                "num_volumes": IsVerifiable.NO,
                "ram_mb": IsVerifiable.NO,
                "volumes_gb": IsVerifiable.NO
            }
        }
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/lab/region{suffix}"

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
        response = super().get(url=self.url(), params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create'])
    def create(
        self,
        name: str,
        openstack_id: int,
        owner_group_id: str,
        tower_id: int,
        banner: str | None = None,
        description: str | None = None,
        enabled: bool | None = None,
        lifespan_length: int | None = None,
        location_id: int | None = None,
        openstack_keyname: str | None = None,
        reservation_expiration_max: int | None = None,
        reservations_enabled: bool | None = None,
        satellite_id: int | None = None,
        dns_id: int | None = None,
        total_quota: dict | None = None,
        user_quota: dict | None = None,
        users_group_id: str | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(url=self.url(), json=body)
        self.log_cleanup(response, method=self.delete)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_usage_all'])
    def get_usage_all(self) -> requests.Response:
        url = self.url(suffix='/all/usage')
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['delete'])
    def delete(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().delete(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update'])
    def update(
        self,
        id: int,
        name: str | None = None,
        openstack_id: int | None = None,
        owner_group_id: str | None = None,
        tower_id: int | None = None,
        banner: str | None = None,
        description: str | None = None,
        enabled: bool | None = None,
        lifespan_length: int | None = None,
        location_id: int | None = None,
        openstack_keyname: str | None = None,
        reservation_expiration_max: int | None = None,
        reservations_enabled: bool | None = None,
        satellite_id: int | None = None,
        total_quota: dict | None = None,
        user_quota: dict | None = None,
        users_group_id: str | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self', 'id'])
        body = self.create_body(args)
        cleanup_args = self.get_values_before_update(self.get, id, args)
        response = self.patch(self.url(f"/{id}"), json=body)
        self.log_cleanup(response, method=self.update, method_args=cleanup_args)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['remove_product'])
    def remove_product(self, region_id: int, product_id: int) -> requests.Response:
        url = self.url(suffix=f"/{region_id}/products")
        body = {'id': product_id}
        response = super().delete(url, json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_products'])
    def get_products(self, id: int, filter: dict | None = None) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', 'id', '__class__'])
        params = self.create_params(args)

        url = self.url(suffix=f"/{id}/products")
        response = super().get(url, params=params)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['update_products'])
    def update_products(
        self,
        region_id: int,
        product_id: int,
        enabled: bool | None = None
    ) -> requests.Response:
        args = self.get_function_arguments(
            locals(), skip_args=['self', 'region_id'])
        body = self.create_body(args)

        # remap 'product_id' to 'id'
        body['id'] = body['product_id']
        del body['product_id']

        url = self.url(suffix=f"/{region_id}/products")
        response = self.post(url, json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_usage'])
    def get_usage(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/usage")
        response = super().get(url)

        return response
