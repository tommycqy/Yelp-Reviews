import unittest
import os
from pathlib import Path
from yelp_reviews.visualization.map_functions import (
    get_map_df,
    get_center,
    get_indicators,
    get_filter_indicator_df,
    get_filter_df,
    get_viz
)

DIR_PATH = str(Path(os.getcwd()))
DATA_FOLDER = "yelp_reviews/tests/data"
API_KEY = Path(os.path.join(DIR_PATH, DATA_FOLDER, "api_key.txt")).read_text()
URL_PATH = Path(os.path.join(DIR_PATH, DATA_FOLDER, "url.txt"))
HTML_PATH = Path(os.path.join(DIR_PATH, "yelp_reviews/tests/data",
                              "test1.html"))


class MapFunctionsTestCase(unittest.TestCase):
    def test_map_center(self):
        """
        Test: if returned coordinates is close to UW coordinates
        """

        df_map = get_map_df(os.path.join(DATA_FOLDER, "test_map_df.csv"))
        center = get_center(df_map)
        uw_coord = [-122.3038, 47.6498]
        self.assertAlmostEqual(round(center[0], 1), round(uw_coord[0], 1))

    def test_get_map_df(self):
        """
        Test: if returned dataframe includes column "lat"
        """

        df_map = get_map_df(os.path.join(DATA_FOLDER, "test_map_df.csv"))
        cols = list(df_map.columns)
        self.assertTrue("lat" in cols)

    def test_get_indicators(self):
        """
        Test: if returned dataframe includes indicators
        """

        df = get_map_df(os.path.join(DATA_FOLDER, "test_map_df.csv"))
        df_indicators = get_indicators(df, "transactions")
        self.assertEqual(df_indicators.pickup.max(), 1)

    def test_get_filter_indicator_df(self):
        """
        Test: if all indicators filtered is True
        """

        df = get_map_df(os.path.join(DATA_FOLDER, "test_map_df.csv"))
        ind = "transactions"
        df_indicators = get_indicators(df, ind)
        col = ["pickup"]
        df_filter = get_filter_indicator_df(df_indicators, ind, col)
        self.assertEqual(df_filter.pickup.min(), 1)

    def test_get_filter_df(self):
        """
        Test: if filtered df filters based on logic
        """
        df_map = get_map_df(os.path.join(DATA_FOLDER, "test_map_df.csv"))
        df_filter = get_filter_df(df_map, "price", "$")
        self.assertEqual(len(df_filter), 172)

    def test_get_viz(self):
        """
        Test: if mapbox map rendered from the correct dataset
        """

        viz = get_viz(os.path.join(DATA_FOLDER, "test_map_df.csv"))
        data1 = viz.data[0]
        df_data = get_map_df(os.path.join(DATA_FOLDER, "test_map_df.csv"))
        self.assertEqual(data1["properties"]["name"], df_data["name"][0])


if __name__ == '__main__':
    unittest.main()
