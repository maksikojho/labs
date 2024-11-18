# TODO решите задачу
import json

def task() -> float:
    global data
    result = 0
    for i in data:
        result += i['weight'] * i['score']
    result = round(result, 3)
    return result




with open('input.json') as json_file:
    data = json.load(json_file)

print(task())
