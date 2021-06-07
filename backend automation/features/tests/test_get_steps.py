from pytest_bdd import scenario, given, when, then
import requests


#backend = BackendAutomation()

@scenario(r'get list users.feature', 'Verify get request for single and list users')
def test_get_request_for_single_and_list_users():
    print("********** Scenario to verify get request for single and list users **********")

@given('user hits get request for list users')
def user_hits_get_request_for_list_users():
    get_response_list = requests.get('https://reqres.in/api/users', params={'page': '2'}, verify=False)
    get_response_list.status_code = 200
    print("Given got executed")

@when('user hits get request for single user')
def user_hits_get_request_for_single_user():
    get_response_single = requests.get('https://reqres.in/api/users/2')
    get_response_single.status_code = 200
    print("When got executed")

@then('response should be generated for both get request')
def response_should_be_generated_for_both_get_request():
    print("Then got executed")