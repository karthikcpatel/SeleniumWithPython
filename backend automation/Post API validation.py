import requests

post_response = requests.post('https://reqres.in/api/users',json={
        "name": "morpheus",
        "job": "leader"
},)
print(post_response.json())
print(post_response.text)

json_response = post_response.json()
print(json_response['name'])

assert post_response.status_code == 201