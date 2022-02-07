import requests

responce = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(responce.text)