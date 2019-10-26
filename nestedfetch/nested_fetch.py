import itertools

def flatten_data(data):
    """
        @Arguments:

        data : list

        @Return:

        Returns the flattened list
    """

    if isinstance(data,list):
        while(any(isinstance(o, list) for o in data)):
            data = list(itertools.chain.from_iterable(data)) 
    return data    


def nested_get(data, keys, default=None, flatten=False):
    '''
        @Arguments:

        data : dict / list

        keys => List of sequential keys leading to the desired value to fetch

        default => Specifies the default value to be returned if any specified key is not present. 
        If not specified, it will be None

        flatten => Specifies whether to flatten the returned value

        @Return:

        Returns the fetched value if it exists, or returns specified default value
    '''

    return {
    True : lambda: flatten_data(_nested_get(data,keys,default)),
    False : lambda: _nested_get(data,keys,default)
    }.get(flatten, lambda : None)()


def _nested_get(data, keys, default):
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
                    value = list(map((lambda o: default if o == default else _nested_get(o, [key], default)), value))                        
            else:
                value = dict.get(value, key, default)
            
            if value == default:
                break
        return value
    except Exception as e:
        return default


def nested_set(data, keys, value, create_missing=False, _count = 0):

    """
        @Arguments:

        data => dict / list

        keys => List of sequential keys leading to the desired value to set / update

        value => Specifies the value to set / update

        create_missing => Specifies whether to create new key while building up if the specified key does not exists


        @Return:

        Returns the number of values updated
    """
    d = data
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
        
