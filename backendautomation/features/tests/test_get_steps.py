import pytest
from pytest_bdd import scenario, given, when, then
from backendautomation.features.forms.test_steps import BackendAutomation

backend = BackendAutomation()

@scenario(r'get list users.feature', 'Verify all get requests from reqres')
def test_get_request_for_single_and_list_users():
    print("********** Scenario to verify get request for single and list users **********")

@given('user has access to hit all get requests')
def user_has_access_to_hit_all_get_requests():
    pass
    print("Given got executed")

@when('user hits get request for list of users')
def user_hits_get_request_for_list_of_users():
    backend.get_list_of_users()
    print("When got executed")

@when('user hits get request for single user')
def user_hits_get_request_for_single_user():
    backend.get_single_user()
    print("And got executed")

@then('all requests should be successful')
def all_requests_should_be_successful():
    backend.verify_status_code()
    print("Then got executed")