import sys
import subprocess

from steps.api.api import API
from steps.cli.cli_model import ResourceHubCLI
from tempfile import TemporaryDirectory
from behave import fixture
from pathlib import Path

@fixture
def rhub_api(context):
    context.api = API()

    yield context.api

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
