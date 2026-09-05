# JSON is commonly used with data APIS. here how we can parse JSON into a python dictionary

import json

# sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)