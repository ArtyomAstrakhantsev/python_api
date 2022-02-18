import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
print(response.history)
print(response.url)

counter = 0
for i in range(len(response.history)):
    counter += 1
print(counter)