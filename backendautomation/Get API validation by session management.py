import requests

def getPassword():
    file = open(r"C:\Users\kartik.patel\PycharmProjects\SeleniumWithPython\backendautomation\utilities\info.txt", "r")
    content = file.read()
    return content

get_session = requests.session()
get_session.auth=('karthikcpatel@gmail.com',getPassword())

get_response = get_session.get("https://api.github.com/user",auth=('karthikcpatel@gmail.com',getPassword()))
print(get_response.status_code)