import unittest
import os
from pathlib import Path
from yelp_reviews.data_collection.api_data import (
    yelp_search,
    all_restaurants,
    parse_api_response,
)

'''
Placed globally as the paths are used throughout the testcases.
Using data from the file to test.
Change the file if need to test for other cases.
'''

DIR_PATH = str(Path(os.getcwd()))
DATA_FOLDER = "yelp_reviews/tests/data"
API_KEY = Path(os.path.join(DIR_PATH, DATA_FOLDER, "api_key.txt")).read_text()
PARAM_PATH = Path(os.path.join(DIR_PATH, DATA_FOLDER, "params.txt"))
URL_PATH = Path(os.path.join(DIR_PATH, DATA_FOLDER, "url.txt"))
DF_PATH = Path(os.path.join(DIR_PATH, DATA_FOLDER, "dataframe.txt"))


class APIDataTestCase(unittest.TestCase):
    def test_api_response(self):
        """
        TEST FOR API RESPONSE
        To check if the data in json frame
        is parsed into a panda dataframe correctly.
        """
        params_list = []
        with open(PARAM_PATH, 'r') as file:
            for line in file:
                params_list.append(line.strip())
        params = {"term": params_list[0], "location": params_list[1],
                  "categories": params_list[2]}

        # Yelp Search Test Case
        data = yelp_search(API_KEY, params)
        total = data['total']
        self.assertEqual(total, 156)

        # All Restaurants Test Case
        tacos = all_restaurants(API_KEY, params)
        taco_restaurants_df = parse_api_response(tacos)
        self.assertEqual(len(tacos), len(taco_restaurants_df))
        self.assertEqual(taco_restaurants_df.shape, (156, 12))

        """
            TEST FOR A SINGLE ROW:
            Using a particular restaurant url
                to check if all the rows in the dataframe are correct:
            Scope: If we want to check for any other cases,
                need to change the url as test data needed is hardcoded.
        """
        with open(URL_PATH, 'r') as file:
            for line in file:
                url = line.strip()
        df_list = []
        with open(DF_PATH, 'r') as file:
            for line in file:
                df_list.append(line.strip())
        t_df = taco_restaurants_df
        TNT_Taqueria = t_df.loc[t_df['url'] == url]
        rating_value = df_list[2]
        self.assertEqual(TNT_Taqueria.iloc[0]['name'], df_list[0])
        self.assertEqual(TNT_Taqueria.iloc[0]['price'], df_list[1])
        self.assertEqual(TNT_Taqueria.iloc[0]['rating'], int(rating_value))
        self.assertEqual(TNT_Taqueria.iloc[0]['category'], df_list[3])


if __name__ == '__main__':
    unittest.main()
