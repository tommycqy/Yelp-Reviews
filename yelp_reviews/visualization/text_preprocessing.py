import nltk
import collections
import csv
import string
import re
import matplotlib.pyplot as plt


def nltk_download():
    """
    Run nltk_download() if nltk doesn't install the above packages
    """
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt')


nltk_download()


def read_all_reviews(filepath):
    """
    Read CSV file that contains all reviews into a string
    Returns:
        text (string)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        L = []
        for row in reader:
            L += row
    f.close()
    text = ','.join(L)
    return text


def read_all_reviews_seperately(filename1, filename2):
    """
    Read all the reviews and the reviewCount for each restaurant
    Returns:
        Tuple(reviewCount for each restaurant, list of all reviews)
    """
    with open(filename2, 'r', encoding='utf-8') as f2:
        reader = csv.reader(f2)
        reviewCount_list = []
        for row in reader:
            reviewCount_list += row
    f2.close()
    reviewCounts = map(int, reviewCount_list)

    with open(filename1, 'r', encoding='utf-8') as f1:
        reader = csv.reader(f1)
        L = []
        for row in reader:
            L += row
        f1.close()
    return (reviewCounts, L)


def get_latest_reviews(f1, f2):
    """
    Get the latest single review for each restaurant
    Returns:
        List of latest single review for each restaurant
    """
    (reviewCounts, L) = read_all_reviews_seperately(f1, f2)
    newest_review_list = []
    index = 0
    for reviewCount in reviewCounts:
        if reviewCount == 0:
            newest_review_list.append('')
        else:
            newest_review_list.append(L[index])
            index += reviewCount
    return newest_review_list


def preprocess(text, stopwords={},
               lemmatizer=nltk.stem.wordnet.WordNetLemmatizer()):
    """
    Normalizes case and handles punctuation
    args:
        text: str -- raw text
        stopwords : Set[str] -- lemmatized tokens to exclude from the output
        lemmatizer : Lemmatizer --
            an instance of a class implementing the lemmatize() method
    Returns:
        list(str): tokenized text
    """
    # Lowercase strings
    text = text.lower()
    # Get rid of urls
    text = re.sub(r'http:\/\/t.co/\w\w\w\w\w\w\w\w\w\w', " ", text)
    text = re.sub(r'https:\/\/t.co/\w\w\w\w\w\w\w\w\w\w', " ", text)
    # Remove "'s" and apostrophe
    text = re.sub("'s", "", text)
    text = re.sub("'", "", text)
    # Calling nltk.tokenize to create a token list
    tokens = nltk.word_tokenize(text)

    filtered_tokens = []
    for i in range(len(tokens)):
        token = tokens[i]
        # Remove all punctuations
        if token in string.punctuation:
            continue
        else:
            filtered_tokens.append(token)

    # Break the tokens
    break_list = []
    for i in range(len(filtered_tokens)):
        append_bool = False
        token = filtered_tokens[i]
        # Break tokens at all characters that are
        # not in string.ascii_letters or string.digits
        for c in token:
            if c in string.ascii_letters:
                continue
            elif c in string.digits:
                continue
            else:
                append_bool = True
        if append_bool:
            break_list.append(token)

    if break_list != []:
        for break_token in break_list:
            break_index = filtered_tokens.index(break_token)
            b = break_index
            insert_string_list = re.split(r'[^\d | ^a-zA-Z]', break_token)
            insert_string_list = [x for x in insert_string_list if x != ""]
            filtered_tokens[b: b+1] = tuple(insert_string_list)

    # Lemmatize and then remove stopwords
    result = []
    for token in filtered_tokens:
        new_token = lemmatizer.lemmatize(token)
        if new_token in stopwords:
            continue
        else:
            result.append(new_token)
    return result


def get_rare_words(tokens):
    """
    Calculates the word count distribution, excluding stopwords.
    Use the word count information to find rare words (more stopwords)
    Returns: Set[str] -- a set of all words that appear exactly once
    """
    result = []
    dist = collections.Counter(tokens)
    for key in dist:
        if dist[key] == 1:
            result.append(key)

    return set(result)
