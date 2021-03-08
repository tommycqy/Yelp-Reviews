import unittest
import pandas
from bs4 import BeautifulSoup
from yelp_reviews.code.data_collection.api_data import *
from yelp_reviews.code.data_collection.reviews_scraper import *

api_key = 'Y0vpAcCzpLY3l5VSChBzAcRpy-JrWmmaOenf'\
                    'Uf-AGrC4lKtc79YDH503ZZSURFVGsAx_I1-Xo'\
                    '0T6YykBPmaOalvnGubVhpIH_K0kfIcWEh0FLftyNyUQ75MXaW0wYHYx'
params={"term":"taco",
                    "location":"University District,Seattle",
                    "categories": "restaurants"}
class MyTestCase(unittest.TestCase):
    def test_api_response(self):

        tacos = all_restaurants(api_key,params)
        taco_restaurants_df = parse_api_response(tacos)
        #Test the dataframe specs
        self.assertEqual(len(tacos), len(taco_restaurants_df))
        self.assertEqual(taco_restaurants_df.shape, (156,12))

        #Test for a single row

        restaurant_url_list = taco_restaurants_df['url'].tolist()

        for i in range(len(restaurant_url_list)):
            url = restaurant_url_list[i]
            url_name='https://www.yelp.com/biz/off-the-rez-seattle?adjust_creative=Yd84IPqpgzteXDQ2QE83uA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Yd84IPqpgzteXDQ2QE83uA'
            if (url==url_name):
                Off_the_Rez = taco_restaurants_df.iloc[i]
                self.assertEqual(Off_the_Rez['name'], 'Off the Rez')
                self.assertEqual(Off_the_Rez['price'], '$')
                self.assertEqual(Off_the_Rez['rating'], 4.0)
                self.assertEqual(Off_the_Rez['category'], 'foodtrucks,burgers,tacos')



    def test_parse_page(self):

        tacos = all_restaurants(api_key, params)
        taco_restaurants_df = parse_api_response(tacos)

        #to check page_parsing
        test_url = taco_restaurants_df.loc[1]['url']
        test_reviews=extract_reviews(test_url)
        self.assertEqual(len(test_reviews),20)
        #parse Instance
        self.assertIsInstance(parse_page('tests/test.html'), list, "is list")



if __name__ == '__main__':
    unittest.main()
