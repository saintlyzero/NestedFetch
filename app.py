from utils import DeepSearch

'''
    DeepSearch.get()
'''

# Dictionaries
data1 = {'a': 123, 'b': {'address': {'city': 'mumbai'}}}
res = DeepSearch(data1).get('b','address','city')

# Dictionaries -> lists
data2 = {'a':123, 'b': [{'city':'Pune'},{'city':'Paris'},{'city':'Goa'}]}
res = DeepSearch(data2).get('b','city')

# Dictionaries -> list -> Dictionaries
res = DeepSearch(data3).get('b','address','city')
data3 = {'a':123, 'b': [{'address':{'city':'Pune'}},{'address':{'city':'Mumbai'}}]}


