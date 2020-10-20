import requests
import re

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, auth=(username, password), data={'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': 'submit'})

content = response.text

flag = re.findall(r"The password for natas7 is (.*)", content)[0]

print(flag)