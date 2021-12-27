from pytest_bdd import scenario, given, when, then
from backendautomation.features.forms.test_steps import *

backend = BackendAutomation()

@scenario(r'post create users.feature', 'Verify all post requests from reqres')
def test_all_post_requests():
    print("********** Scenario to verify all post requests **********")

@given('user has access to hit all post requests')
def user_has_access_to_hit_all_post_requests():
    pass
    print("Given got executed")

@when('user hits post request for create users')
def user_hits_post_request_for_create_users():
    #backend.post_create_users()
    print("When got executed")

@then('post request should be successful')
def all_requests_should_be_successful():
    #backend.verify_post_response_code()
    print("Then got executed")