from nested_fetch.nested_fetch import NestedFetch

'''
    NestedFetch.get()
'''

# Dictionaries
# data1 = {'a': 123, 'b': {'address': {'city': 'mumbai'}}}
# res = NestedFetch(data1).get(['b','address','city'])
# print(res)

# Dictionaries -> lists

# data2 = {'a':123, 'b': [{'city':'Pune'},{'city':'Paris'},{'city':'Goa'}]}
# res = NestedFetch(data2).get('b','city')
# print(res)

nested_list_get_data = {
        'name': 'Walter White',
        'details': {
            'address':[[{
                'city': 'Albuquerque'
            },{
                'city': 'El Paso'
            }]]
        }
    }

# res = NestedFetch(nested_list_get_data).get(['details','address',0,0])
# print(res)
# Dictionaries -> list -> Dictionaries
# data3 = {'a':123, 'b': [{'address':{'city':'Pune'}},{'address':{'city':'Mumbai'}}]}
# res = NestedFetch(data3).get('b','address','city', default=-1)

# data4 = {'a':123, 'b': [{'address':{'city':['Pune']}},{'address':{'city':['Mumbai']}}]}
# res = NestedFetch(data4).get(['b','address','city'], default=-1)
# print(res)

simple_get_data = {
        'name': 'Jesse Pinkman',
        'details': {
            'address':{
                'city': 'Albuquerque'
            }
        }
    }


print(simple_get_data)
# print(nested_set(data, ["address","cities",0,"city"], "Naples", create_missing = False))
print(NestedFetch(simple_get_data).set_value(
    ['details','address','state'], "New Mexico", create=True))
print(simple_get_data)
