import unittest
import os
import pandas
from bs4 import BeautifulSoup
from pathlib import Path
from yelp_reviews.data_collection.api_data import (
    all_restaurants,
    parse_api_response
)
from yelp_reviews.data_collection.reviews_scraper import (
    retrieve_html,
    parse_page,
    extract_reviews,
    extract_all_restaurants_reviews
)

DIR_PATH = str(Path(os.getcwd()))
API_KEY = Path(os.path.join(DIR_PATH, "yelp_reviews/tests/data", "api_key.txt")).read_text()
PARAM_PATH = Path(os.path.join(DIR_PATH, "yelp_reviews/tests/data", "params.txt"))
HTML_PATH = Path(os.path.join(DIR_PATH, "yelp_reviews/tests/data", "test1.html"))

class WebScraperTestCase(unittest.TestCase):
    def test_scrape_page(self):
        """
           TEST SCRAPING FUNCTIONS:
           To check if the the numbers of reviews extracted  in a page are 20
        """
        params_list=[]
        with open(PARAM_PATH,'r') as file:
            for line in file:
                params_list.append(line.strip())
                
        params={"term":params_list[0],"location":params_list[1],
                "categories":params_list[2]}

        tacos = all_restaurants(API_KEY, params)
        taco_restaurants_df = parse_api_response(tacos)

        # Retrieve HTML Test Case
        test_url = taco_restaurants_df.loc[1]['url']
        (status_code, html_obj) = retrieve_html(test_url)
        self.assertEqual(status_code, 200)

        # Parse Page Test Case
        self.assertIsInstance(parse_page(html_obj), list, "is list")

        # Extract Reviews Test Case
        test_reviews=extract_reviews(test_url)
        self.assertEqual(len(test_reviews),20)

if __name__ == '__main__':
    unittest.main()
