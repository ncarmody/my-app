import requests
from function_col import pp
base = "http://127.0.0.1:5000/"

response = requests.get(base + "request")
pp(response.json())
