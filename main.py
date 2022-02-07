from simplejson.errors import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_json = response.json()
    print(parsed_json)
except JSONDecodeError:
    print("Response is a not JSON")