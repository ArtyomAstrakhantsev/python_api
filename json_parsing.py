import json

string_as_json_format = '{"answer": "Hello, Artyom"}'
obj = json.loads(string_as_json_format)

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} нет в json")