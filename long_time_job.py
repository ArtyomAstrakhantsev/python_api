import requests
import json
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

start_job = requests.get(url)
json_start_job = json.loads(start_job.text)
print(json_start_job, " - Test start")

token = "token"
time_token = "seconds"

if token in json_start_job:
    value_token = json_start_job[token]
    value_time = json_start_job[time_token]
else:
    print("Token is missing")

params = {token: value_token}

before_finish_job = requests.get(url, params=params)
print(value_time, " - Test before job - Done")

time.sleep(int(value_time))

after_finish_job = requests.get(url, params=params)
json_after_finish_job = json.loads(after_finish_job.text)

result = "result"
status = "status"

if result in json_after_finish_job and status in json_after_finish_job:
    if json_after_finish_job[status] != "Job is ready":
        print("Something go wrong")
else:
    print("Result or status is missing in response")
print(json_after_finish_job[status]," - Test after job - Done")