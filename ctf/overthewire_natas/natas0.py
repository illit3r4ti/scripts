import requests
import re

username = "natas0"
password = username
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.get(url, auth=(username, password))

content = response.text

flag = re.findall(r"<!--The password for natas1 is (.*) -->", content)[0]

print(flag)