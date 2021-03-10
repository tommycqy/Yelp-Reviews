from yelp_reviews.code.data_collection.api_data import *
from bs4 import BeautifulSoup
import json
import requests
import csv

API_KEY = 'Y0vpAcCzpLY3l5VSChBzAcRpy-JrWmmaOenf' \
          'Uf-AGrC4lKtc79YDH503ZZSURFVGsAx_I1-Xo' \
          '0T6YykBPmaOalvnGubVhpIH_K0kfIcWEh0FLftyNyUQ75MXaW0wYHYx'


def retrieve_html(url):
    """
    Return the raw HTML for the specified URL
    """
    r = requests.get(url, auth=("user", "pass"))
    return (r.status_code, r.text)


def parse_page(html):
    """
    Parse the reviews on a single page of a restaurant
    """
    soup = BeautifulSoup(html, "html.parser")
    review_soups = soup.find_all("script", type="application/ld+json")

    description_list = []
    for soup in review_soups:
        text = soup.string
        # Decode the json into python dict
        js_dict = json.loads(text)
        if "review" in js_dict:
            review_list = js_dict["review"]
            for i in range(len(review_list)):
                review_dict = review_list[i]
                description_list.append(review_dict["description"])
    return description_list


def extract_reviews(url):
    """
    Retrieve the reviews on the first page for a single restaurant on Yelp
    Returns: reviews (list): list of reviews (max 20)
    """
    api_url = url + "%3Fstart%3D40"
    html_obj = retrieve_html(url)[1]
    newest_20_reviews = parse_page(html_obj)
    return newest_20_reviews


def extract_all_restaurants_reviews(search_params):
    """
    Retrieve all of the reviews for interested businesses on Yelp.com
    Returns: reviews (list): list of reviews
    """
    restaurants = all_restaurants(API_KEY, search_params)
    restaurants_df = parse_api_response(restaurants)
    num_of_restaurants = len(restaurants)
    restaurant_url_list = restaurants_df['url'].tolist()
    result = []
    for i in range(len(restaurant_url_list)):
        url = restaurant_url_list[i]
        result += extract_reviews(url)
    return result


def write_data():
    search_params = {"term": "taco", "location": "University District,Seattle",
                     "categories": "restaurants"}
    result = extract_all_restaurants_reviews(search_params)

    # Opening the csv file in 'w' mode, write rows
    with open('reviews.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(result)
        f.close()

# write_data()
