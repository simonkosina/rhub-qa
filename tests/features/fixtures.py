import sys
import subprocess
import json
import glob

from steps.api.api import API
from steps.api.base_endpoint import BaseEndpoint
from steps.cli.cli_model import ResourceHubCLI
from tempfile import TemporaryDirectory
from behave import fixture
from pathlib import Path

API_REQUESTS_PATTERN = '../tools/api_*_requests.json'
API_RESPONSE_PATTERN = '../tools/api_*_responses.json'
API_AUTH = ('testuser1', 'testuser1')


@fixture
def rhub_api(context):
    try:
        context.api = API(admin_auth=API_AUTH)
        context.auth = API_AUTH
        context.api.logger = BaseEndpoint.LOGGER
        context.api.request_data = {}
        context.api.response_data = {}
        context.saved_ids = {}

        request_data_paths = glob.glob(API_REQUESTS_PATTERN)
        response_data_paths = glob.glob(API_RESPONSE_PATTERN)

        for path in request_data_paths:
            with open(path) as f:
                context.api.request_data.update(json.load(f))

        for path in response_data_paths:
            with open(path) as f:
                context.api.response_data.update(json.load(f))

        yield context.api
    finally:
        context.api.cleanup()


@fixture
def rhub_cli(context):
    try:
        temp_directory = TemporaryDirectory()
        temp_directory_path = Path(temp_directory.name)

        # create temporary python virtual environment
        subprocess.run(
            [sys.executable, '-m', 'venv', temp_directory.name],
            check=True,
        )

        # install RHub CLI on the created virtual environment
        subprocess.run(
            f"source {temp_directory_path / 'bin/activate'} ; pip install -q {ResourceHubCLI.PIP_CLONE_URL}",
            check=True,
            shell=True,
        )

        context.cli = ResourceHubCLI(temp_directory_path)
        yield context.cli

    finally:
        temp_directory.cleanup()
