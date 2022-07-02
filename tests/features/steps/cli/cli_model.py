import sys
import subprocess
import requests
import json

from pathlib import Path


class ResourceHubCLI:
    API_BASE_URL = 'http://localhost:8081/v0'
    API_USER = 'testuser1'
    API_PASS = 'testuser1'

    # TODO: API needs to be on the same version as the CLI code being tested
    # TODO: switch back to official repo
    # PIP_CLONE_URL = 'git+ssh://git@github.com/resource-hub-dev/rhub-cli.git'
    PIP_CLONE_URL = 'git+ssh://git@github.com/guioliveirabh/rhub-cli@test_generation'
    # PIP_CLONE_URL = 'git+ssh://git@github.com/simonkosina/rhub-cli@format-fix'

    def __init__(self, virtual_environment_path: Path):
        self.entrypoint = str(virtual_environment_path / 'bin/rhub-cli')
        self.base_command = [
            self.entrypoint,
            '--data-format', 'json',
            '--base-url', self.API_BASE_URL,
            '--user', self.API_USER,
            '--password', self.API_PASS,
        ]
        self.last_output = ''

    def run(self, cli_args: list[str]):
        """
        Execute a CLI command.
        """
        self.last_output = None
        self.last_cli_args = cli_args
        command = self.base_command + cli_args

        try:
            process_status = subprocess.run(
                command,
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as error:
            error_msg = error.stderr.decode('utf-8')
            print(error_msg, file=sys.stderr)

            raise(error)

        self.last_output = self._format_cli_output(process_status.stdout)

    def _format_cli_output(self, output: str):
        """
        Format the CLI output for comparison.
        """

        try:
            return json.loads(output)
        except json.JSONDecodeError:
            return output.rstrip()

    def _format_api_output(self, response: requests.Response):
        """
        Format the API response for comparison.
        """

        try:
            return response.json()
        except json.JSONDecodeError:
            return response.content.rstrip()

    def _prepare_dict(self, dictionary: dict, keys_to_remove: dict) -> dict:
        """
        Removes keys from the original dictionary which are not compared during verification.
        """

        for k, v in keys_to_remove.items():
            if type(v) is dict:
                # recursively remove nested fields
                self._prepare_dict(dictionary[k], v)
            elif v is True:
                del dictionary[k]

    def verify(self, api_response: requests.Response, unverifiable_items: dict) -> bool:
        """
        Compare the last CLI output with the API response.
        """
        api_output = self._format_api_output(api_response)
        cli_output = self.last_output

        print(f"> CLI output:\n{cli_output}\n\n> API response:\n{api_output}")

        if type(api_output) is not type(cli_output):
            return False

        if type(api_output) is dict:
            self._prepare_dict(api_output, unverifiable_items)
            self._prepare_dict(cli_output, unverifiable_items)

        return api_output == cli_output
