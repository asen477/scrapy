#-*- coding: UTF-8 -*-
import json

data = []
with open('./auto3.json') as f:
    for line in f:
        data.append(json.loads(line))


print(json.dumps(data , ensure_ascii=False))
