import requests
import json


parameters = '[{"method": "GET"}, {"method": "POST"}, {"method": "DELETE"}, {"method": "PUT"}, {"method": "HEAD"}]'
parameter = json.loads(parameters)

method = [requests.get, requests.post, requests.delete, requests.put, requests.head]
url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

x = 0
for i in range(len(parameter)):
    for x in range(len(method)):
        print(i)
        if i == 0:
            response = method[x](url, params=parameter[i])
            print(response.text)
            x += 1
        else:
            response = method[x](url, data=parameter[i])
            print(response.text)
            x += 1
    i += 1