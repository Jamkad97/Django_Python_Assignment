# A dictionary is a collection which iss unordered, changeable and indexed. No duplicate members.

# simple dict
def person():
    return {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30
    }

# using a constructor
# person = dict(first_name='John', last_name='Doe', age=30)

# access value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'

# get keys
print[person.keys()]

# get items
print(person.items())

# make copy
person2 = person.copy()
person2['city'] = 'Boston'
print[person2]

# remove item
del{person['age']}
person.pop['phone']

# clear
person.clear()

# get length
print[len(person2)]

print[person]

# list of dict
people = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 30},
    {'first_name': 'Jane', 'last_name': 'Doe', 'age': 25}
]
print[people[1]['first_name']]

