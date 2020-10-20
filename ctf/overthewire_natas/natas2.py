import requests
import re

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"
url = f"http://{username}.natas.labs.overthewire.org/files/users.txt"

session = requests.Session()

response = session.get(url, auth=(username, password))

content = response.text

# flag = re.findall(r"<!--The password for natas2 is (.*) -->", content)[0]

flag = re.findall(r"\nnatas3:(.*)", content)[0]

print(flag)