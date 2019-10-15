from utils import DeepSearch

data = {'a': 123, 'b': {'address': {'city': 'mumbai'}}}
keys = ['b', 'address', 'city' ]

res = DeepSearch(keys).get('b', 'address', 'city')
print(res)

res = DeepSearch(data).contains(123)
print(res)
