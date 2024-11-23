# TODO решите задачу
import json

def task() -> float:
    global data
    return sum([item['weight']*item['score'] for item in data]).__round__(3)




with open('input.json') as json_file:
    data = json.load(json_file)

print(task())
