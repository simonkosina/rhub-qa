import requests

from steps.api.base_endpoint import BaseEndpoint, log_call


class BaremetalHostEndpoint(BaseEndpoint):
    """
    Represents the /bare_metal/host API endpoint.
    """

    UNVERIFIABLE_ITEMS = {
        'get_list': {},
        'create_drac': {},
        'create_impl': {},
        'create_redfish': {},
        'get': {},
        'get_power_state': {}
    }

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/bare_metal/host{suffix}"

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_list'])
    def get_list(self) -> requests.Response:
        response = super().get(self.url())

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create_drac'])
    def create_drac(
        self,
        arch: str,
        handler_id: int,
        ipmi_address: str,
        ipmi_password: str,
        ipmi_port: str,
        ipmi_username: str,
        mac: str,
        name: str,
        redfish_address: str,
        redfish_password: str,
        redfish_system_id: str,
        redfish_username: str,
        redfish_verify_ca: bool,
        drac_address: str,
        drac_password: str,
        drac_username: str,
        ipxe_support: bool = None,
        legacy_bios: bool = None,
        uefi: bool = None,
        uefi_secure_boot: bool = None,
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(suffix='/drac'), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create_impl'])
    def create_ipmi(
        self,
        arch: str,
        handler_id: int,
        ipmi_address: str,
        ipmi_password: str,
        ipmi_port: str,
        ipmi_username: str,
        mac: str,
        name: str,
        ipxe_support: bool = None,
        legacy_bios: bool = None,
        uefi: bool = None,
        uefi_secure_boot: bool = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(suffix='/ipmi'), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['create_redfish'])
    def create_redfish(
        self,
        arch: str,
        handler_id: int,
        ipmi_address: str,
        ipmi_password: str,
        ipmi_port: str,
        ipmi_username: str,
        mac: str,
        name: str,
        redfish_address: str,
        redfish_password: str,
        redfish_system_id: str,
        redfish_username: str,
        redfish_verify_ca: bool,
        ipxe_support: bool = None,
        legacy_bios: bool = None,
        uefi: bool = None,
        uefi_secure_boot: bool = None
    ) -> requests.Response:
        args = self.get_function_arguments(locals(), skip_args=['self'])
        body = self.create_body(args)
        response = self.post(self.url(suffix='/redfish'), json=body)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get'])
    def get(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}")
        response = super().get(url)

        return response

    @log_call(BaseEndpoint.LOGGER, UNVERIFIABLE_ITEMS['get_power_state'])
    def get_power_state(self, id: int) -> requests.Response:
        url = self.url(suffix=f"/{id}/power_state")
        response = super().get(url)

        return response
