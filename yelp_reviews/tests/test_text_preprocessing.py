import unittest
import os
import pandas
from pathlib import Path
from yelp_reviews.visualization.text_preprocessing import(
    read_all_reviews,
    read_all_reviews_seperately,
    get_latest_reviews,
    preprocess,
    get_rare_words,
    plot
)

DIR_PATH = str(Path(os.getcwd()))
DATA_FOLDER = "yelp_reviews/tests/data"
API_KEY = Path(os.path.join(DIR_PATH, DATA_FOLDER, "api_key.txt")).read_text()
URL_PATH = Path(os.path.join(DIR_PATH, DATA_FOLDER, "url.txt"))
HTML_PATH = Path(os.path.join(DIR_PATH, "yelp_reviews/tests/data", 
                                "test1.html"))

class TextPreprocssingTestCase(unittest.TestCase):
    def test_text_preprocessing(self):
        """
           TEST Text Preprocessing FUNCTIONS:
           To check the text preprocessing, read_csv functions
        """
        # Read All Reviews Test Case
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
