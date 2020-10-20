import requests
import re

username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, auth=(username, password), data={"secret": "oubWYf2kBq", "submit": "submit"})

content = response.text

flag = re.findall(r"The password for natas9 is (.*)\n", content)[0]

print(flag)