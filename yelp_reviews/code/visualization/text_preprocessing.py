import nltk
import collections
import csv
import string
import re
import matplotlib.pyplot as plt

def nltk_download():
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt')

# nltk_download()

def read_all_reviews(filename = 'yelp_reviews/data/reviews.csv'):
    """ Read CSV file that contains all reviews into a string
    
    Outputs:
        text(string)
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f) 
        for row in reader:
            text = ','.join(row) 
    f.close()
    return text

def read_all_reviews_seperately():
    filename1 = 'yelp_reviews/data/reviews.csv'
    filename2 = 'yelp_reviews/data/reviewCountOnPage.csv'

    with open(filename2, 'r') as f2:
        reader = csv.reader(f2) 
        reviewCount_list = []
        for row in reader:
            reviewCount_list += row
    f2.close()
    reviewCounts = map(int, reviewCount_list)

    with open(filename1, 'r') as f1:
        reader = csv.reader(f1)
        L = []
        for row in reader:
            L += row
        f1.close()
    return (reviewCounts, L)

def get_latest_reviews():
    (reviewCounts, L) = read_all_reviews_seperately()
    newest_review_list = []
    for reviewCount in reviewCounts:
        index = 0
        if reviewCount == 0:
            newest_review_list.append('')
        else:
            newest_review_list.append(L[index])
            index += reviewCount
    return newest_review_list

def preprocess(text, stopwords={}, lemmatizer=nltk.stem.wordnet.WordNetLemmatizer()):
    """ Normalizes case and handles punctuation
    
    args:
        text: str -- raw text
        stopwords : Set[str] -- lemmatized tokens to exclude from the output
        lemmatizer : Lemmatizer -- an instance of a class implementing the lemmatize() method

    Outputs:
        list(str): tokenized text
    """
    #lowercase strings
    text = text.lower()
    
    #get rid of urls
    text = re.sub(r'http:\/\/t.co/\w\w\w\w\w\w\w\w\w\w', " ", text)
    text = re.sub(r'https:\/\/t.co/\w\w\w\w\w\w\w\w\w\w', " ", text)
    
    #remove "'s" and apostrophe
    text = re.sub("'s", "", text)
    text = re.sub("'", "",text)

    #calling tokenize to create a token list
    tokens = nltk.word_tokenize(text)
    
    filtered_tokens = []
    for i in range(len(tokens)):
        token = tokens[i]

            #remove all punctuations
        if token in string.punctuation:
            continue
        else:
            filtered_tokens.append(token)
    
    #break the tokens
    break_list = []
    for i in range(len(filtered_tokens)):
        append_bool = False
        token = filtered_tokens[i]
        #break tokens at all characters that are not in string.ascii_letters or string.digits
        for c in token:
            if (c in string.ascii_letters) or (c in string.digits):
                continue
            else:
                append_bool = True
        if append_bool == True:
            break_list.append(token)

    if break_list != []:
        for break_token in break_list:
            #print(break_token)
            break_index = filtered_tokens.index(break_token)
            #print(break_index)
            
            insert_string_list = re.split('[^\d | ^a-zA-Z]', break_token)
            #print(insert_string_list) 
            insert_string_list = [x for x in insert_string_list if x != ""]
            #print(insert_string_list)
            filtered_tokens[break_index: break_index+1] = tuple(insert_string_list)

     #lemmatize and then remove stopwords
    result = []
    for token in filtered_tokens:
        new_token = lemmatizer.lemmatize(token)
        if new_token in stopwords:
            continue
        else: 
            result.append(new_token)
            
    return result

def get_distribution(tokens):
    """ Calculates the word count distribution, excluding stopwords.

    args: 
        data_train -- the training data

    return : collections.Counter -- the distribution of word counts
    """
    distribution = collections.Counter(tokens)
    return distribution

def get_rare_words(dist):
    """use the word count information from the training data to find more stopwords

    args:
        dist: collections.Counter -- the output of get_distribution

    returns : Set[str] -- a set of all words that appear exactly once in the training data
    """
    
    result = []
    for key in dist:
        if dist[key] == 1:
            result.append(key)
    
    return set(result)


def plot():
    text = read_all_reviews()
    extra_stopwords=set()
    stopwords = set(nltk.corpus.stopwords.words('english')) | set(["http", "co", "rt", "amp"]) | extra_stopwords
    tokens = preprocess(text, stopwords)
    distribution = get_distribution(tokens)
    plt.hist(distribution.values(), bins=100)
    plt.yscale('log')
    plt.savefig('yelp_reviews/word_distribution.png')

    rare_words_set = get_rare_words(distribution)
    print(len(rare_words_set))

# plot()



