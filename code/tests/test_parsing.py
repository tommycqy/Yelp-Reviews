import unittest
from pathlib import Path

from code.yelp_parse import parse_api_response
from code.yelp_scraping import all_restaurants

def read_api_key(filepath="key.txt"):
    return Path(filepath).read_text().strip()

class MyTestCase(unittest.TestCase):
    def test_api_response(self):
        api_key = 'Y0vpAcCzpLY3l5VSChBzAcRpy-JrWmmaOenfUf-AGrC4lKtc79YDH503ZZSURFVGsAx_I1-Xo0T6YykBPmaOalvnGubVhpIH_K0kfIcWEh0FLftyNyUQ75MXaW0wYHYx'
        tacos = all_restaurants(api_key, params={"term":"taco","location":"University District,Seattle"})
        taco_restaurants_df = parse_api_response(tacos)
        self.assertEqual(len(tacos), len(taco_restaurants_df))
        self.assertEqual(len(df.columns), 8)


if __name__ == '__main__':
    unittest.main()
