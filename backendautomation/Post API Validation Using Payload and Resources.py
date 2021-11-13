import requests
from AllPayloads import *
from utilities.configurations import *
from utilities.resources import *

url = get_config()['API']['endpoint']+APIResources.api_users
post_response = requests.post(url,json=add_user("kartik"),headers={"auth_token":"3522kwnfsd43n"},verify=False)
print(post_response.json())
print(post_response.text)

json_response = post_response.json()
print(json_response['name'])

assert post_response.status_code == 201