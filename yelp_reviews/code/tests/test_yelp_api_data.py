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
        """
        TEST FOR API RESPONSE
        To check if the data in json frame is parsed into a panda dataframe correctly.
        """
        tacos = all_restaurants(api_key,params)
        taco_restaurants_df = parse_api_response(tacos)
        self.assertEqual(len(tacos), len(taco_restaurants_df))
        self.assertEqual(taco_restaurants_df.shape, (156,12))

        """
            TEST FOR A SINGLE ROW:
            Using a particular restaurant url to check if all the rows in the dataframe are correct:
            Scope: If we want to check for any other cases , need to change the url as test data needed is hardcoded.
        """

        url_name ='https://www.yelp.com/biz/tnt-taqueria-seattle?adjust_creative=Yd84IPqpgzteXDQ2QE83uA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Yd84IPqpgzteXDQ2QE83uA'
        TNT_Taqueria=taco_restaurants_df.loc[taco_restaurants_df['url'] == url_name]

        self.assertEqual(TNT_Taqueria.iloc[0]['name'],'TNT Taqueria')
        self.assertEqual(TNT_Taqueria.iloc[0]['price'], '$')
        self.assertEqual(TNT_Taqueria.iloc[0]['rating'], 4.0)
        self.assertEqual(TNT_Taqueria.iloc[0]['category'], 'mexican')



    def test_scrape_page(self):
        """
           TEST SCRAPING FUNCTIONS:
           To check if the the numbers of reviews extracted  in a page are 20
        """

        tacos = all_restaurants(api_key, params)
        taco_restaurants_df = parse_api_response(tacos)

        #To check page_parsing
        test_url = taco_restaurants_df.loc[1]['url']
        test_reviews=extract_reviews(test_url)
        self.assertEqual(len(test_reviews),20)

        #Parse Instance
        self.assertIsInstance(parse_page('tests/data/test.html'), list, "is list")



if __name__ == '__main__':
    unittest.main()
