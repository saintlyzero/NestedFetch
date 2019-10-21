

def nested_get(data, keys, default=None):
    '''@Arguments: keys -> sequential keys to iterate'''
    value = None
    try: 
        for key in keys:
            if value:
                if isinstance(value, list):
                    if isinstance(key, int):
                        value = value[key]
                    else:
                        value = list(map((lambda o: default if o == default else o.get(key, default)), value))                        
                else:
                    value = value.get(key, default)
            else:
                value = dict.get(data, key, default)
            if not value:
                break
        return value
    except Exception as e:
        return default


def nested_set(data, keys, value, create_missing=False, _count = 0):
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
        
