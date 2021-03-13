import requests
import json
import time
import pandas as pd
import os
from pathlib import Path
import yelp_reviews


def yelp_search(api_key, params):
    """
    Makes an authenticated request to the Yelp API
    api_key: read text file containing API key
    parameters:
        term: keywords to search (tacos, etc.)
        location: location keywords (Seattle, etc.)
    Returns JSON
    """
    search_url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": "Bearer %s" % api_key}
    response = requests.get(search_url, params=params, headers=headers)
    data = json.loads(response.text)
    return data


def all_restaurants(api_key, params):
    """
    Retrieve ALL the restaurants on Yelp for a given query
    api_key: read text file containing API key
    parameters:
        term: keywords to search (tacos, etc.)
        location: location keywords (Seattle, etc.)
    Returns the API response as a list of dictionaries
    Max number of responses is 1000
    """
    initial_search = yelp_search(api_key, params)
    records_num = initial_search["total"]
    requests_num = records_num // 20 + 1
    offset = 0
    result = []

    for i in range(requests_num):
        # 20 restaurants per request
        curr_offset = offset + i * 20
        params["offset"] = curr_offset
        data = yelp_search(api_key, params)
        result += data["businesses"]
        # Pause slightly between requests
        time.sleep(.400)
    return result


def parse_api_response(api_response):
    """
    Parse the API response into a Pandas DataFrame
    API response is all of the restaurants matched from yelp_scraping
    """
    df = pd.DataFrame(api_response)
    category_list = []
    for i in range(len(df)):
        cat_i = [cat["alias"] for cat in df["categories"][i]]
        category_list.append(",".join(cat_i))
    latitude = [coord.get("latitude") for coord in df["coordinates"]]
    longitude = [coord.get("longitude") for coord in df["coordinates"]]
    df["category"] = category_list
    df["latitude"] = latitude
    df["longitude"] = longitude
    df_return = df.drop(columns=["coordinates", "image_url",
                                 "is_closed", "categories",
                                 "location", "display_phone",
                                 "distance"])
    return df_return


def write_api_data(api_key, params, fileName):
    """
    Write api data to pandas dataFrame and write to .csv file
    Default: filename as 'api_data.csv'
    File will be saved in separate 'Data' folder
    """
    dir_name = os.path.dirname(yelp_reviews.__file__)
    dir_path = os.path.join(str(Path(dir_name).parents[0]),"data")
    file_path = os.path.join(dir_path, fileName)
    api_response = all_restaurants(api_key, params=params)
    restaurants_df = parse_api_response(api_response)
    restaurants_df.to_csv(file_path)
    return file_path
