import io
import json
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.app import app as flask_app

# Constants
BASE_URL = "http://localhost:3000"

# Scenarios
scenarios('./features/hello.feature')

@pytest.fixture
def app():
    app = flask_app
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@given('the Flask app is running')
def flask_app_is_running(app):
    pass  # The app fixture will ensure the app is up

@when(parsers.parse('I go to the "{url}" URL'), target_fixture="request_result")
def go_to_url(client, url):
    # Need follow_redirects here
    return client.get(BASE_URL + url, follow_redirects=True)

@then(parsers.parse('I should be greeted with "{text}"'))
def greeted_with( request_result, text):
    response_data = request_result.data
    # assert b"Hello" in response_data
    assert text.encode() in response_data

# Then the JSON response should contain "app", "src.app"
@then(parsers.parse('the JSON response should contain "{name}" set to "{value}"'))
def json_name_value( request_result, name, value):
    response_data = request_result.data.replace(b"'", b'"')
    reponse_json = json.load(io.BytesIO(response_data))
    assert reponse_json[name] == value
