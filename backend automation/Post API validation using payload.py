import requests
from AllPayloads import *
from utilities.configurations import *

post_response = requests.post(get_config['API']['endpoint']+'/api/users',json=add_user("kartik"),)
print(post_response.json())
print(post_response.text)

json_response = post_response.json()
print(json_response['name'])

assert post_response.status_code == 201