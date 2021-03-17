## Yelp Reviews


## Introduction 

The goal of this project is to use yelp data to get Yelp reviews, ratings, price, location of different categories of restaurants like 'Tacos' and build a visualization app that allows for easy filtering of rating, price, and category. Also, we wanted to see what else we can extract from the text data. The Yelp data needed is obtained from both the Yelp Fusion API and the web scraper that we implemented. 


## Components

**.** Data collection and parsing tool using Yelp Fusion API
        Return JSON file of restaurant meeting criteria based on search parameters
        Read JSON file to a pandas DataFrame, keeping just relevant data points (as specified in above “Data” section). 
**.** Web scraper for the 20 newest reviews
        Using the “URL” from the above DataFrame, scrape latest 20 reviews for the selected restaurant, and returns list of the reivews
**.** Data visualization map
        Using the coordinate data from the above DataFrame, plot restaurants in a map visualization 
        TBD: Interactive visualization allowing filtering by category, price range, rating
        TBD: Other visualization components in tooltip, showing review text data for each restaurant
        TBD: Show separately distribution of ratings based on restaurants displayed in map
**.** Data visualization for text reviews
        Using web scraper function to extract the text reviews on the first webpage of each restaurant
        Preprocess the reviews using following steps:
            (Lowercase, URL removing (re.sub), Remove trailing ’s’ and apostrophe, Tokenize, 
            Remove punctuations (include white space), Break tokens on non-alpha-numeric values, 
            Lemmatize, Remove stop words (nltk.stopwords (English) and self-defined extra stop-words))
        Return a visualization for the text review (word cloud). TBD


## Project folder structure

```

 Yelp-Reviews
    ├── LICENSE
    ├── README.md
    ├── data
    │   ├── api_data.csv
    │   ├── api_data_tacos.csv
    │   ├── reviewCountOnPage.csv
    │   └── reviews.csv
    ├── docs
    │   └── Design\ Document.pdf
    ├── examples
    │   ├── mapbox_viz.ipynb
    │   └── scraper-demo.ipynb
    ├── requirements.txt
    ├── setup.py
    └── yelp_reviews
        ├── __init__.py
        ├── api_key.txt
        ├── data_collection
        │   ├── __init__.py
        │   ├── api_data.py
        │   └── reviews_scraper.py
        ├── tests
        │   ├── __init__.py
        │   ├── data
        │   │   ├── api_key.txt
        │   │   ├── dataframe.txt
        │   │   ├── mini_reviews.csv
        │   │   ├── params.txt
        │   │   ├── test1.html
        │   │   ├── test_map_df.csv
        │   │   ├── test_reviewCount.csv
        │   │   ├── test_reviews.csv
        │   │   └── url.txt
        │   ├── test_api_data.py
        │   ├── test_map_functions.py
        │   ├── test_reviews_scraper.py
        │   └── test_text_preprocessing.py
        └── visualization
            ├── __init__.py
            ├── map_functions.py
            ├── text_preprocessing.py
            └── word_distribution.png
            
```


## Installation

To install and use YelpReviews, you can follow the below steps.

**Clone the repository**: git clone https://github.com/tommycqy/Yelp-Reviews.git

**Change the Directory**: cd yelp_reviews

**Install setup.py**: python setup.py install


## Limitations

Yelp API has many limitations.It only returns 20 results for a single request and returns up to 1000 businesses for the same search query. It also has a limited request rate.To resolve this issue,we implemented a web scraper using the Requests package to retrieve HTML from url and the Beautiful Soup package to parse the HTML. The resulting scraper would find all the JSON-formatted objects within the HTML and extract all 20 reviews on the first page of the business website.
