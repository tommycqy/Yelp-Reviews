import unittest
import os
from pathlib import Path
from yelp_reviews.visualization.text_preprocessing import (
    read_all_reviews,
    read_all_reviews_seperately,
    get_latest_reviews,
    preprocess,
    get_rare_words
)

DIR_PATH = str(Path(os.getcwd()))
DATA_FOLDER = "data"


class TextPreprocssingTestCase(unittest.TestCase):
    def test_text_preprocessing(self):
        """
           TEST Text Preprocessing FUNCTIONS:
           To check the text preprocessing, read_csv functions
        """
        mini_reviews = Path(os.path.join(DIR_PATH, DATA_FOLDER,
                            "mini_reviews.csv"))
        # Read All Reviews Test Case
        test_string = 'Doing well! How about you?,'\
                      'a..a. .a . a.,word-of-mouth self-esteem'
        self.assertEqual(read_all_reviews(mini_reviews), test_string)

        # Read Reviews Seperately Test Case
        test_reviews = Path(os.path.join(DIR_PATH, DATA_FOLDER,
                                         "test_reviews.csv"))
        test_reviewCount = Path(os.path.join(DIR_PATH, DATA_FOLDER,
                                             "test_reviewCount.csv"))
        (m1, L2) = read_all_reviews_seperately(test_reviews, test_reviewCount)
        self.assertEqual(list(m1), [2, 1, 1, 1])
        self.assertEqual(len(L2), 5)

        # Preprocess Test Cases
        # Punctuation and space handling
        self.assertEqual(preprocess(" a..a. .a . a."), ['a', 'a', 'a', 'a'])
        self.assertEqual(preprocess("word-of-mouth self-esteem"),
                         ['word', 'of', 'mouth', 'self', 'esteem'])

        # Apostrophe handling
        self.assertEqual(preprocess("you've"), ['youve'])
        self.assertEqual(preprocess("She's"), ['she'])
        self.assertEqual(preprocess("Cea'sar"), ['ceaar'])

        # Lemmatizer
        self.assertEqual(preprocess("walks"), ['walk'])

        # Long sentence Test Case
        long_review = L2[4]
        long_output = ['rt', 'gopconvention', 'oregon', 'vote', 'today',
                       'that', 'mean', '62', 'day', 'until', 'the',
                       'gopconvention']
        self.assertEqual(preprocess(long_review), long_output)

        # Get Latest Reviews Test Case
        latest_reviews = get_latest_reviews(test_reviews, test_reviewCount)
        self.assertEqual(len(latest_reviews), 4)
        self.assertEqual(latest_reviews[1], 'word-of-mouth self-esteem')

        # Get Rare Words Test Case
        test_tokens = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'e', 'f']
        rare_token_set = {'d', 'f', 'e'}
        self.assertEqual(get_rare_words(test_tokens), rare_token_set)


if __name__ == '__main__':
    unittest.main()
