import requests

cookie = {'visit-month':'February'}

response = requests.get("https://httpbin.org/cookies",cookies={'visit-year':'2021'})
response_dict = response.json()
print(response_dict)