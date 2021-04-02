import requests

get_response = requests.get('https://reqres.in/api/users',
                        params={'page':'2'},)
print(get_response.text)

json_response = get_response.json()
dict_sub_response = (json_response['data'][0])
print(dict_sub_response['first_name'])

assert get_response.status_code == 200
print(get_response.headers)
assert get_response.headers['Content-Type'] == 'application/json; charset=utf-8'