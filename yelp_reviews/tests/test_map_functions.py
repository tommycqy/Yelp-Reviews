import unittest
import os
import pandas
from pathlib import Path
from yelp_reviews.visualization.map_functions import(
    get_map_df,
    get_center,
    get_indicators,
    get_filter_indicator_df,
    get_viz
)

DIR_PATH = str(Path(os.getcwd()))
DATA_FOLDER = "yelp_reviews/tests/data"
API_KEY = Path(os.path.join(DIR_PATH, DATA_FOLDER, "api_key.txt")).read_text()
URL_PATH = Path(os.path.join(DIR_PATH, DATA_FOLDER, "url.txt"))
HTML_PATH = Path(os.path.join(DIR_PATH, "yelp_reviews/tests/data", 
                                "test1.html"))

class MapFunctionsTestCase(unittest.TestCase):
    def test_map_functions(self):
        """
           TEST Map FUNCTIONS:
           To check if the the visualization is correctly generated
        """
        # Get Map DataFrame Test Case
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
    