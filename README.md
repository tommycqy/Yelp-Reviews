## Yelp Reviews

## Introduction 

The goal of this project is to use the yelp data to get Yelp reviews, rating, price,location of different categories of restaurants like  'Tacos' and build a visualization app that allows for easy filtering of rating, price and category.Also, we wanted to see what else we can extraxt from the text data. The Yelp data  needed is obtained from both the Yelp Fusion API and the web scraper that we implemented. 



## Objective

**.** Build  a web scraper using the  package to retrieve HTML from url and then parse the HTML. 

**.** The resulting scraper would find all the JSON-formatted objects within the HTML and extract reviews(20 as limited by yelp).

**.** Given the rating, price and category , serach the API response and filter the varibles and show the appropriate restaurants.


## Data Preprocessing

**.** Read all the reviews of the data in the CSV file and preprocess the data in following steps:

      Lowercase, URL removing (re.sub), Remove trailing ’s’ and apostrophe, Tokenize, 
      Remove punctuations (include white space), Break tokens on non-alpha-numeric values, 
      Lemmatize, Remove stop words (nltk.stopwords (English))

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

**Install setup.py**    :python setup.py install


## Limitations
Yelp API has many limitations.It only returns 20 results for a single request and returns up to 1000 businesses for the same search query. It also has a limited request rate.To resolve this issue,we implemented a web scraper using the Requests package to retrieve HTML from url and the Beautiful Soup package to parse the HTML. The resulting scraper would find all the JSON-formatted objects within the HTML and extract all 20 reviews on the first page of the business website.
