import requests
import time

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

    headers = {
        "Authorization" : "Bearer %s" % api_key
    }

    response = requests.get(search_url, params = params, headers = headers)

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

    data1 = yelp_search(api_key, params)

    records_num  = data1["total"]
    requests_num = records_num // 20 + 1
    offset = 0
    result = []

    for i in range(records_num):
        #20 restaurants per request
        curr_offset = offset + i * 20
        params["offset"] = curr_offset
        data = yelp_search(api_key, params)
        result += data["businesses"]
        #pause slightly between requests
        time.sleep(.300)

    return result



def retrieve_url(url):
    """
    Return the raw HTML for the specified URL
    """

    r = requests.get(url, auth = ("user", "pass"))

    return (r.status_code, r.text)