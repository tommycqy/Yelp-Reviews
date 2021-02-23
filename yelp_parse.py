import pandas as pd
from bs4 import BeautifulSoup
import json
from .yelp_scraping import retrieve_url


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

    df_return = df.drop(columns = ["coordinates", "image_url", "is_closed", "categories", "location", "display_phone", "distance"])

    return df_return


def parse_page(html):
    """
    Parse the reviews on a single page of a restaurant
    """

    soup = BeautifulSoup(html, "html.parser")
    review_soups = soup.find_all("script", type = "application/ld+json")

    description_list = []
    for soup in review_soups:
        text = soup.string
        #decode the json into python dict
        js_dict = json.loads(text)

        if "review" in js_dict:
            review_list = js_dict["review"]

            for i in range(len(review_list)):
                review_dict = review_list[i]
                description_list.append(review_dict["description"])

    return description_list


def extract_reviews(url, review_count):
    """
    Retrieve all of the reviews for a single restaurant on Yelp
    Returns: reviews (list): list of dictionaries containing extracted review information
    """

    api_url = url + "%3Fstart%3D40"

    html_obj = retrieve_url(url)

    review_list = parse_page(html_obj)

    result = review_list

    num_pages = review_count // 20 + 1

    for i in range(1, num_pages):
        curr_offset = i * 20
        curr_url = api_url + "&start=%d"%curr_offset

        curr_page_reviews = parse_page(retrieve_url(curr_url)[1])

        result += curr_page_reviews

    return result