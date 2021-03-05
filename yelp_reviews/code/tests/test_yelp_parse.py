import unittest
from yelp_reviews.code.data_collection.yelp_parse import retrieve_html, parse_api_response, parse_page, extract_reviews

TEST_HTML_FILE_NAME = 'test.html'

class MyTestCase(unittest.TestCase):

   def test_parse_page(self):
    self.assertIsInstance(parse_page(TEST_HTML_FILE_NAME), list, "is list")

if __name__ == '__main__':
    unittest.main()
