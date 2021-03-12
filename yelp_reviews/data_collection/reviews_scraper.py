from yelp_reviews.data_collection.api_data import *
from bs4 import BeautifulSoup
import json
import requests
import csv


DIR_PATH = str(Path(os.getcwd()))
API_KEY = Path(os.path.join(DIR_PATH, "yelp_reviews", 
                            "api_key.txt")).read_text()


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
    Returns: (all_reviews (list): list of reviews, reviewCount_list (list))
    """
    restaurants = all_restaurants(API_KEY, search_params)
    restaurants_df = parse_api_response(restaurants)
    num_of_restaurants = len(restaurants)
    restaurant_url_list = restaurants_df['url'].tolist()
    all_reviews = []
    reviewCount_list = []
    for i in range(len(restaurant_url_list)):
        url = restaurant_url_list[i]
        newest_page_reviews = extract_reviews(url)
        all_reviews += newest_page_reviews
        reviewCount_list.append(len(newest_page_reviews))
    return (all_reviews, reviewCount_list)


def write_data():
    search_params={"term":"taco","location":"University District,Seattle", 
                "categories": "restaurants"}
    (all_reviews, reviewCount_list) = extract_all_restaurants_reviews(search_params)
  
    # Opening the csv file in 'w' mode, write rows
    with open('./data/reviews.csv', 'w') as f:
        writer = csv.writer(f) 
        writer.writerow(all_reviews)
        f.close()
    
    with open('./data/reviewCountOnPage.csv', 'w') as f:
        writer = csv.writer(f) 
        writer.writerow(reviewCount_list)
        f.close()

# write_data()