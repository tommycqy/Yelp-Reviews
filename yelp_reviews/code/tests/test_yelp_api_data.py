import unittest
import pandas
from yelp_reviews.code.data_collection.api_data import *

TEST_HTML_FILE_NAME = 'test.html'

class MyTestCase(unittest.TestCase):

    def test_api_response(self):
        api_key = 'Y0vpAcCzpLY3l5VSChBzAcRpy-JrWmmaOenf'\
                    'Uf-AGrC4lKtc79YDH503ZZSURFVGsAx_I1-Xo'\
                    '0T6YykBPmaOalvnGubVhpIH_K0kfIcWEh0FLftyNyUQ75MXaW0wYHYx'
        tacos = all_restaurants(api_key, params={"term":"taco",
                    "location":"University District,Seattle", 
                    "categories": "restaurants"})
        taco_restaurants_df = parse_api_response(tacos)
        #Test the dataframe specs
        self.assertEqual(len(tacos), len(taco_restaurants_df))
        self.assertEqual(len(tacos), 156)
        self.assertEqual(taco_restaurants_df.shape, (156,12))

        #Test for a single row
        Off_the_Rez = taco_restaurants_df.iloc[1]
        self.assertEqual(Off_the_Rez['name'], 'Off the Rez')
        self.assertEqual(Off_the_Rez['price'], '$')
        self.assertEqual(Off_the_Rez['rating'], 4.0)
        self.assertEqual(Off_the_Rez['category'], 'foodtrucks,burgers,tacos')

if __name__ == '__main__':
    unittest.main()
