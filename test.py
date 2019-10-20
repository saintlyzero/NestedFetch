#import copy
# import functools 

# data = {
#     'name': 'Alan',
#     'address': [{
#         'city':'Satorini'
#     },{
#         'city':'Budapest'
#     }]
# }


# d = data
# print(data)
# d = d['address']
# print(d)
# print(data)

# def list_set(o,):
    
data = {
    'name': 'Alan',
    'address': [{
        'cities':[{'city':'Sataroni'}, {'city':'Sataroni'}]
    },{
        'cities':[{'city':'Celta'}]
    }]
}

def nested_set(dic, keys, value, create_missing=False, _count = 0):
    d = dic
    count = _count
    try:
        for itr, key in enumerate(keys[:-1]):
            if key in d:
                d = d[key]
                if isinstance(d, list):
                    if (itr != len(keys)-1) and (isinstance(keys[itr+1], int)):
                        if (itr == len(keys)-2):
                            d[keys[-1]] = value
                            count += 1
                        else:
                            d = d[keys[itr+1]]
                            count = nested_set(d, keys[itr+2:], value, create_missing, _count= count)
                    else:
                        count = sum(list(map((lambda o: nested_set(o,keys[itr+1:],value,create_missing,_count = count)),d)))
                    
                    return count

            elif create_missing:
                d = d.setdefault(key, {})
            else:
                return count
        if (keys[-1] in d or create_missing):
            d[keys[-1]] = value
            return count + 1
        elif (isinstance(keys[-1], int)) and isinstance(d, list):
            d[keys[-1]] = value
            return count + 1

        else:
            return count

    except Exception as e:
        return count
 


print(data)
# print(nested_set(data, ["address","cities",0,"city"], "Naples", create_missing = False))
print(nested_set(data, ["address", 'cities', 'city'], "Apli Mumbai", create_missing = False))
print(data)


