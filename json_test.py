import json

data = {"test1": "a", "test2": "b", "test3": "C"}
data_str = json.dumps(data)
data2 = {"body": data_str}
print(json.dumps(data2))
