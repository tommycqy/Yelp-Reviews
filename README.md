# DATA515 Yelp Reviews


## Introduction 

### Objective

Yelp search does not allow for simple filtered search by ratings - can we build an intuitive, interactive map that allows users to search for restaurants given a ratings range? 

Further, given Yelp's rich text data, what sort of insights can be gained from their reviews?  

- Can ratings be predicted from review text?
- Can we extract keywords from the reviews?
- How accurate are the restaurant searches? (A search for "tacos" in Seattle returns restaurants that aren't even marginally related to tacos, for example)

The objective of this project is to use the Yelp Fusion API to get restaurant data such as location, price, restaurant category, as well as user reviews, to build a visualization app that allows for simple filtering. 

### Data and Packages 



| Package      | Description |
| :----------- | :----------- |
| Yelp Fusion API    | Restaurant Data based on search parameters (location, price, category, etc).       |
| BeautifulSoup   | Scrape/Parse user reviews of restaurant based on URL returned from API call        |
| NLTK   | Text processing of review text data     |
| MapBox   | Process coordinate data and convert to geoJSON format, render map visualization|



## Components

**Data collection and parsing tool using Yelp Fusion API** \
Return JSON file of restaurant meeting criteria based on search parameters. \
Read JSON file to a pandas DataFrame, keeping just relevant data points (as specified in above “Data” section).

**Web scraper for the reviews on the first page** \
Using the “URL” from the above DataFrame, scrape latest reviews (20 at max) for the selected restaurant, and returns list of the reivews.

**Data visualization map** \
Using the coordinate data from the above DataFrame, plot restaurants in a map visualization. \
Filter returned map coordinates by price, category, transaction, rating 

**Data visualization for text reviews** \
Using web scraper function to extract the text reviews on the first webpage of each restaurant. \
Preprocess the reviews using following steps:

1. Lowercase
2. Remove URL
3. Remove Trailing ’s’ and Apostrophe
4. Tokenize Text (NLTK.word_tokenize)
5. Remove Punctuations (including white space)
6. Break Tokens on Non-alpha-numeric Values
7. Lemmatize the Tokens
8. Remove stopwords (NLTK.stopwords (english) and self-defined extra stopwords) 

Return visualizations for the text reviews including a distribution plot and a wordcloud plot.


## Project Folder Structure

```

 Yelp-Reviews
    ├── LICENSE
    ├── README.md
    ├── data
    │   ├── api_data.csv
    │   ├── api_data_tacos.csv
    │   ├── reviewCountOnPage.csv
    │   └── reviews.csv
    ├── docs
    │   └── Design Document.pdf
    ├── examples
    │   ├── mapbox_viz.ipynb
    │   └── scraper-demo.ipynb
    ├── requirements.txt
    ├── setup.py
    └── yelp_reviews
        ├── __init__.py
        ├── api_key.txt
        ├── data_collection
        │   ├── __init__.py
        │   ├── api_data.py
        │   └── reviews_scraper.py
        ├── tests
        │   ├── __init__.py
        │   ├── data
        │   │   ├── api_key.txt
        │   │   ├── dataframe.txt
        │   │   ├── mini_reviews.csv
        │   │   ├── params.txt
        │   │   ├── test1.html
        │   │   ├── test_map_df.csv
        │   │   ├── test_reviewCount.csv
        │   │   ├── test_reviews.csv
        │   │   └── url.txt
        │   ├── test_api_data.py
        │   ├── test_map_functions.py
        │   ├── test_reviews_scraper.py
        │   └── test_text_preprocessing.py
        └── visualization
            ├── __init__.py
            ├── map_functions.py
            ├── text_preprocessing.py
            └── word_distribution.png
            
```


## Installation

To install and use Yelp-Reviews, you can follow the below steps.

**Clone the repository**: \
```git clone https://github.com/tommycqy/Yelp-Reviews.git```

**Run the Python Modules from the Root Directory**: \
For Testing: \
```python3 -m yelp_reviews.tests.test_api_data ```\
```python3 -m yelp_reviews.tests.test_text_preprocessing```

For Running a Single Module: \
```python3 -m yelp_reviews.data_collection.api_data```

**Install setup.py**: \
```python setup.py install```

**Install requirements.txt**: \
```pip3 install -r requirements.txt```


## Limitations

Yelp Fusion API has a few limitations. For example, it only returns 20 responses for a single request and returns up to 1000 businesses for the same search query. It also has a limited request rate. 

In terms of collecting the reviews data, the Fusion API only returns 3 reviews for each business. To resolve this problem, we implemented a web scraper using the Requests package to retrieve HTML from url and the Beautiful Soup package to parse the HTML. The resulting scraper would find all the JSON-formatted objects within the HTML and extract all reviews (20 at max) on the first page of the business website.


## Next Steps

#### Visualization

- Interactive visualization allowing filtering by category, price range, rating 
- Other visualization components in tooltip, showing review text data for each restaurant 
- Show separately distribution of ratings based on restaurants displayed in map 

#### Machine Learning/Text Processing

- Train a model to predict restaurant rating based on user reviews
- Extract keywords of the restaurant based on review text 