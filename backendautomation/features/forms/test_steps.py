import requests

class BackendAutomation:

    def __init__(self):
        self.get_response_list_response = ""
        self.get_response_single = ""
        self.json_reponse_name = ""

    def get_list_of_users(self):
        get_response_list = requests.get('https://reqres.in/api/users', params={'page': '2'}, verify=False)
        get_response_list_response = get_response_list.status_code

    def get_single_user(self):
        get_response_single = requests.get('https://reqres.in/api/users/2', verify=False)
        get_response_single.status_code == 200

    def verify_status_code(self):
        if self.get_response_list_response == 200:
            return True
        else:
            return False

    def post_create_users(self):
        post_response = requests.post('https://reqres.in/api/users', json=
        {
            "name": "kartik",
            "job": "leader",
        }, verify=False)

        json_response = post_response.json()
        json_response_name = json_response['name']
        print(json_response_name)

    def verify_post_response_code(self):
        if self.json_reponse_name == "kartik":
            return True
        else:
            return False