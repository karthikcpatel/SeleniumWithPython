import requests

class BackendAutomation:

    def get_list_users(self):
        get_response_list = requests.get('https://reqres.in/api/users', params={'page': '2'}, verify=False)
        get_response_list.status_code = 200
