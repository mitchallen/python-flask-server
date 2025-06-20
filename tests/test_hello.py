import io
import json
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.app import app as flask_app
from flask import Flask
from flask.testing import FlaskClient
from typing import Any, Generator

# Constants
BASE_URL = "http://localhost:3000"

# Scenarios
scenarios("./features/hello.feature")


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app = flask_app
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@given("the Flask app is running")
def flask_app_is_running(app: Flask) -> None:
    pass  # The app fixture will ensure the app is up


@when(parsers.parse('I go to the "{url}" URL'), target_fixture="request_result")
def go_to_url(client: FlaskClient, url: str) -> Any:
    # Need follow_redirects here
    return client.get(BASE_URL + url, follow_redirects=True)


@then(parsers.parse('I should be greeted with "{text}"'))
def greeted_with(request_result: Any, text: str) -> None:
    response_data = request_result.data
    # assert b"Hello" in response_data
    assert text.encode() in response_data


# Then the JSON response should contain "app", "src.app"
@then(parsers.parse('the JSON response should contain "{name}" set to "{value}"'))
def json_name_value(request_result: Any, name: str, value: str) -> None:
    response_data = request_result.data.replace(b"'", b'"')
    reponse_json = json.load(io.BytesIO(response_data))
    assert reponse_json[name] == value
