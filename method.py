import requests
import json


params = '[{"method": "GET"}, {"method": "POST"}, {"method": "DELETE"}, {"method": "PUT"}, {"method": "HEAD"}]'
param = json.loads(params)

method = [requests.get, requests.post, requests.delete, requests.put, requests.head]
url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

x = 0
for i in range(len(param)):
    for x in range(len(method)):
        print(i)
        if i == 0:
            response = method[x](url, params=param[i])
            print(response.text)
            x += 1
        else:
            response = method[x](url, data=param[i])
            print(response.text)
            x += 1
    i += 1