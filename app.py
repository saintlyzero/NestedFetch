from utils import NestedFetch

'''
    NestedFetch.get()
'''

# Dictionaries
# data1 = {'a': 123, 'b': {'address': {'city': 'mumbai'}}}
# res = NestedFetch(data1).get('b','address','city')

# Dictionaries -> lists
# data2 = {'a':123, 'b': [{'city':'Pune'},{'city':'Paris'},{'city':'Goa'}]}
# res = NestedFetch(data2).get('b','city')

# Dictionaries -> list -> Dictionaries
# data3 = {'a':123, 'b': [{'address':{'city':'Pune'}},{'address':{'city':'Mumbai'}}]}
# res = NestedFetch(data3).get('b','address','city', default=-1)

data4 = {'a':123, 'b': [{'address':{'city':['Pune']}},{'address':{'city':['Mumbai']}}]}
res = NestedFetch(data4).get(['b','address','city'], default=-1)
print(res)

# data = {
#     'name': 'Alan',
#     'address': [{
#         'cities': [{'city': 'Sataroni'}, {'city': 'Sataroni'}]
#     }, {
#         'cities': [{'city': 'Celta'}]
#     }]
# }


# print(data)
# # print(nested_set(data, ["address","cities",0,"city"], "Naples", create_missing = False))
# print(NestedFetch(data).set_value(
#     ["address", 0, 'cities' ], value="Apli Mumbai", create_missing=True))
# print(data)
