import requests
import re

username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"
url = f"http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt"

session = requests.Session()

response = session.get(url, auth=(username, password))

content = response.text

# flag = re.findall(r"<!--The password for natas2 is (.*) -->", content)[0]

flag = re.findall(r"natas4:(.*)", content)[0]

print(flag)