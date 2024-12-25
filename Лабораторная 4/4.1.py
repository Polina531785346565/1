import json
def task() -> float:
    j = 'input.json'
    with open(j) as f:
        data = json.load(f)
    s = 0.0
    s = s + sum([item["score"] * item["weight"]for item in data])
    return round(s, 3)
print(task())

