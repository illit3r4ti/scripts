import requests
import re
import base64
from urllib.parse import unquote

username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, auth=(username, password), cookies={'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'})

content = response.text

# cookie = unquote(response.cookies['data'])

flag = re.findall(r"The password for natas12 is (.*)<br>", content)[0]

print(flag)