import unittest
from yelp_project.yelp_parse import parse_api_response
from yelp_project.yelp_scraping import all_restaurants


class MyTestCase(unittest.TestCase):

    def test_apiresponse(self):
        tacos=all_restaurants('Y0vpAcCzpLY3l5VSChBzAcRpy-JrWmmaOenfUf-AGrC4lKtc79YDH503ZZSURFVGsAx_I1-Xo0T6YykBPmaOalvnGubVhpIH_K0kfIcWEh0FLftyNyUQ75MXaW0wYHYx', params={"term":"taco","location":"University District,Seattle"})
        taco_restaurants_df = parse_api_response(tacos)
        self.assertEqual(len(tacos), len(taco_restaurants_df))


if __name__ == '__main__':
    unittest.main()
