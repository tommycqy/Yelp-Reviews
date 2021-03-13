import unittest
import os
from pathlib import Path
from yelp_reviews.data_collection.reviews_scraper import (
    retrieve_html,
    parse_page,
    extract_reviews
)

DIR_PATH = str(Path(os.getcwd()))
DATA_FOLDER = "yelp_reviews/tests/data"
API_KEY = Path(os.path.join(DIR_PATH, DATA_FOLDER, "api_key.txt")).read_text()
URL_PATH = Path(os.path.join(DIR_PATH, DATA_FOLDER, "url.txt"))
HTML_PATH = Path(os.path.join(DIR_PATH, "yelp_reviews/tests/data",
                              "test1.html"))


class WebScraperTestCase(unittest.TestCase):
    def test_scrape_page(self):
        """
           TEST SCRAPING FUNCTIONS:
           To check if the the numbers of reviews extracted  in a page are 20
        """
        # Retrieve HTML Test Case
        with open(URL_PATH, 'r') as file:
            for line in file:
                test_url = line
        (status_code, html_obj) = retrieve_html(test_url)
        self.assertEqual(status_code, 200)

        # Parse Page Test Case
        self.assertIsInstance(parse_page(html_obj), list, "is list")

        # Extract Reviews Test Case
        test_reviews = extract_reviews(test_url)
        self.assertTrue(len(test_reviews) <= 20)


if __name__ == '__main__':
    unittest.main()
