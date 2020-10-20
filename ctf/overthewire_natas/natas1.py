import requests
import re

username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.get(url, auth=(username, password))

content = response.text

flag = re.findall(r"<!--The password for natas2 is (.*) -->", content)[0]

print(flag)