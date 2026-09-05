# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Simple tuple
fruit_tuple = (('Apple', 'Orange', 'Mango'))
# Using constructor
# fruit_tuple2 = tuple(('Apple', 'Orange', 'Mango'))

# get single value
print(fruit_tuple[1])

# can not change value
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

del fruit_tuple_2

# get length of tuplee
# print(len(fruit_tuple_2))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set
fruit_set = {'Apple', 'Orange', 'Mango'}

# Check if in set
print('Apples' in fruit_set)

# add to set
fruit_set.add('Grape')

# remove from set
fruit_set.remove('Grape')

# clear set
fruit_set.clear()

# delete set
del fruit_set

print(fruit_set)