import unittest  
from nested_fetch.nested_fetch import nested_get, nested_set

class TestNestedFetch(unittest.TestCase):

    
    simple_get_data = {
            'name': 'Jesse Pinkman',
            'details': {
                'address':{
                    'city': 'Albuquerque'
                }
            }
        }


    nested_get_data = {
            'name': 'Walter White',
            'details': {
                'address':[{
                    'city': 'Albuquerque'
                },{
                    'city': 'El Paso'
                }]
            }
        }
    

    nested_ll_get_data = {
        'name': 'Walter White',
        'details': {
            'address':[{
                'city': 'Albuquerque'
            },{
                'city': 'El Paso'
            },{
                'state': 'New Mexico'
            }]
        }
    }
    
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
    

    def test_simple_get_success(self):
        res = nested_get(self.simple_get_data,['details','address','city'])
        self.assertEqual(res, 'Albuquerque')


    def test_nested_get_all_success(self):
            res = nested_get(self.nested_get_data,['details','address','city'])
            self.assertEqual(res, ['Albuquerque','El Paso'])
    

    def test_nested_ll_get_all_success(self):
        res = nested_get(self.nested_ll_get_data,['details','address','city'], default= None)
        self.assertEqual(res, ['Albuquerque','El Paso', None])


    def test_nested_get_with_index_success(self):
            res = nested_get(self.nested_get_data,['details','address','city', 0])
            self.assertEqual(res, 'Albuquerque')


    def test_nested_list_get_with_index_success(self):
        res = nested_get(self.nested_list_get_data,['details','address',0,0])
        self.assertEqual(res, {'city': 'Albuquerque'})


    def test_nested_get_with_index_error(self):
            res = nested_get(self.nested_get_data,['details','address','city', 5], default=None)
            self.assertEqual(res, None)


    def test_simple_set_success(self):
            res = nested_set(self.simple_get_data,['details','address','city'], "Denver")
            self.assertEqual(res, 1)


    def test_simple_set_build_success(self):
            res = nested_set(self.simple_get_data,['details','address','state'], "New Mexico", create_missing=True)
            self.assertEqual(res, 1)
            self.assertEqual(self.simple_get_data, {
                'name':'Jesse Pinkman', 
                'details': {
                    'address':{
                        'city':'Albuquerque', 
                        'state': 'New Mexico'
                        }}})


    # def test_nested_set_success(self):
    #         res = nested_set(self.nested_get_data,['details','address','city'], "Denver")
    #         self.assertEqual(res, 2)
    #         self.assertEqual(self.nested_get_data,
    #         {
    #             'name': 'Walter White',
    #             'details': {
    #                 'address':[{
    #                     'city': 'Denver'
    #                 },{
    #                     'city': 'Denver'
    #                 }]
    #             }
    #         })
    
    # def test_nested_set_index_success(self):
            # res = NestedFetch(self.nested_get_data).set_value(['details','address', 0, 'city'], "Denver")
            # self.assertEqual(res, 1)
            # self.assertEqual(self.nested_get_data,
            # {
            #     'name': 'Walter White',
            #     'details': {
            #         'address':[{
            #             'city': 'Denver'
            #         },{
            #             'city': 'El Paso'
            #         }]
            #     }
            # })

if __name__ == "__main__":
    unittest.main()