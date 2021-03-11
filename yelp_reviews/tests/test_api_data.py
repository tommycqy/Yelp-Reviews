import unittest
import os
import glob
import pandas
from bs4 import BeautifulSoup
from yelp_reviews.data_collection.api_data import *
from yelp_reviews.data_collection.reviews_scraper import *
api_path = glob.glob('./data/api_key.txt')
api_full_path = os.path.abspath(api_path[0])
params_path=glob.glob('./data/params.txt')
params_full_path = os.path.abspath(params_path[0])

'''
placed globally as these are used by both functions
using data from the file to test.
scope: If needed to test for other cases , should change the file.
'''
with open(api_full_path,'r') as file:
    for line in file:
        api_key=line

params_list=[]
with open(params_full_path,'r') as file:
    for line in file:
        params_list.append(line.strip())
params={"term":params_list[0],"location":params_list[1],"categories":params_list[2]}

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
        # to get data from the url file
        url_path = glob.glob('./data/url.txt')
        url_full_path = os.path.abspath(url_path[0])
        with open(url_full_path, 'r') as file:
            for line in file:
                url_name = line
        # To get the data from dataframe file
        df_path = glob.glob('./data/dataframe.txt')
        df_full_path = os.path.abspath(df_path[0])
        df_list=[]
        with open(df_full_path, 'r') as file:
            for line in file:
                df_list.append(line.strip())

        #url_name ='https://www.yelp.com/biz/tnt-taqueria-seattle?adjust_creative=Yd84IPqpgzteXDQ2QE83uA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=Yd84IPqpgzteXDQ2QE83uA'
        TNT_Taqueria=taco_restaurants_df.loc[taco_restaurants_df['url'] == url_name]
        rating_value=df_list[2]


        self.assertEqual(TNT_Taqueria.iloc[0]['name'],df_list[0])
        self.assertEqual(TNT_Taqueria.iloc[0]['price'], df_list[1])
        self.assertEqual(TNT_Taqueria.iloc[0]['rating'], int(rating_value))
        self.assertEqual(TNT_Taqueria.iloc[0]['category'], df_list[3])



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
