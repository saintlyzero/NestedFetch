import unittest  
from nestedfetch import nested_get, nested_set, flatten_data

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
    
    flatten_data = {
        "league": "Champions League",
        "matches": [
            {
            "match_id": "match_1",
            "goals": [
                {
                "time": 13,
                "scorrer": "Lionel Messi",
                "assist": "Luis Suarez",
                "details": [
                    {
                    "position": "outside-box"
                    },
                    {
                    "position": "right-side"
                    }
                ]
                },
                {
                "time": 78,
                "scorrer": "Luis Suarez",
                "assist": "Ivan Rakitic",
                "details": [
                    {
                    "position": "inside-box"
                    },
                    {
                    "position": "left-side"
                    }
                ]
                }
            ]
            },
            {
            "match_id": "match_2",
            "goals": [
                {
                "time": 36,
                "scorrer": "C. Ronaldo",
                "assist": "Luka Modric",
                "details": [
                    {
                    "position": "penalty"
                    },
                    {
                    "position": "d-box"
                    }
                ]
                }
            ]
            }
        ]
        }

    flatten_test_data = [
        ['This','is'],
        ['flattened', 'data']
    ]

    flatten_nested_data = [[
        ['This','is'],
        ['flattened', 'data']
    ]]

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


    def test_nested_get_flatten(self):
            res = nested_get(self.flatten_data,['matches','goals','scorrer'], default=None, flatten=True)
            self.assertEqual(res, ['Lionel Messi', 'Luis Suarez', 'C. Ronaldo'])


    def test_nested_get_ll_flatten(self):
            res = nested_get(self.flatten_data,['matches','goals','details'], default=None, flatten=True)
            self.assertEqual(res, [{'position': 'outside-box'}, {'position': 'right-side'}, {'position': 'inside-box'}, {'position': 'left-side'}, {'position': 'penalty'}, {'position': 'd-box'}])


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

    def test_simple_flatten(self):
            res = flatten_data(self.flatten_test_data)
            self.assertEqual(res, ['This','is','flattened','data'])


    def test_nested_flatten(self):
            res = flatten_data(self.flatten_nested_data)
            self.assertEqual(res, ['This','is','flattened','data'])



if __name__ == "__main__":
    unittest.main()