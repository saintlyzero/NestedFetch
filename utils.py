class NestedFetch(dict):
    '''Class to fetch value from Nested Dictionary'''

    def get(self, *keys, default=None):
        '''@Arguments: *keys -> sequential keys to iterate'''
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
                    value = dict.get(self, key, default)
                if not value:
                    break
            return value
        except Exception as e:
            return default


    # def set(self, *keys, value, build=False):
    #     '''@Arguments: *keys -> sequential keys to iterate'''
    #     updated = False
    #     try:
    #         for key in keys:
    #             if value:

    # def contains(self, value, default=None):
    #     '''@Arguments: value -> value to check if it exists'''
        
    #     for key, value in self.items():
    #         if isinstance(self, dict):


