import unittest
from yelp_reviews.code.data_collection.reviews_scraper import *


class MyTestCase(unittest.TestCase):
    #Dummy test case, need more functions to test the scraper
    def test_something(self):
        self.assertEqual(True, True)

'''
    def test_parse_page(self):
        self.assertIsInstance(parse_page(TEST_HTML_FILE_NAME), list, "is list")
'''

if __name__ == '__main__':
    unittest.main()
