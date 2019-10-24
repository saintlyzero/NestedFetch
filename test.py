# from nested_fetch.nested_fetch import NestedFetch
from nested_fetch.nested_fetch import nested_get, nested_set
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
 

data = {
    'name': 'Alan',
    'address': [{
        'cities': [{'city': 'Sataroni'}, {'city': 'Sataroni'}]
    }, {
        'cities': [{'city': 'Celta'}]
    }]
}

# print(data)
# print(nested_set(data, ["address","cities",0,"city"], "Naples", create_missing = False))
# print(nested_set(data,  ["address", 0, 'cities' ], "Apli Mumbai", create_missing = True))
# print(data)


simple_get_data = {
        'name': 'Jesse Pinkman',
        'details': {
            'address':{
                'city': 'Albuquerque'
            }
        }
    }

# print(simple_get_data)
# print(nested_set(simple_get_data,['details','address','state'], "New Mexico", create_missing=True))
# print(simple_get_data)
# print(simple_get_data)
# print(NestedFetch(simple_get_data).set_value(['details','address','state'], "New Mexico", create=True))
# print(simple_get_data)

data = {
    "league":"Champions League",
    "matches":[
        {
            "match_id": "match_1",
            "goals":[
                {
                    "time": 13,
                    "scorrer": "Lionel Messi",
                    "assist": "Luis Suarez",
                    "details": [
                        {
                            "position":"outside-box",
                        },
                        {
                            "position":"right-side",
                        }
                    ]
                },
                {
                    "time": 78,
                    "scorrer": "Luis Suarez",
                    "assist": "Ivan Rakitic",
                    "details": [
                        {
                            "position":"inside-box",
                        },
                        {
                            "position":"left-side",
                        }
                    ]
                }
            ] 
        },
        {
            "match_id": "match_2",
            "goals":[
                {
                    "time": 36,
                    "scorrer": "C. Ronaldo",
                    "assist": "Luka Modric",
                    "details": [
                        {
                            "position":"penalty",
                        },
                        {
                            "position":"d-box",
                        }
                    ]
                }
            ] 
        }
    ]
}

# print(data)
# print(nested_get(data,['matches','goals']))
# print(data)

def nested_get1(data, keys, default=None):
    value = data
    try:
        for itr, key in enumerate(keys):
            if isinstance(value, list):
                if isinstance(key, int):
                    if any(isinstance(o, list) for o in value):
                        value = list(map((lambda o: default if (key >= len(o)) else o[key]), value))                        
                    else:
                        value = value[key]
                else:
                    value = list(map((lambda o: default if o == default else nested_get1(o, [key], default=default)), value))                        
            else:
                value = dict.get(value, key, default)
            
            if value == default:
                break
        return value
    except Exception as e:
        return default

# data2 = [{'time': 13, 'scorrer': 'Lionel Messi', 'assist': 'Luis Suarez'}, {'time': 78, 'scorrer': 'Luis Suarez', 'assist': 'Ivan Rakitic'}]
res = nested_get1(data,['matches','goals','scorrer'])
print(res)
