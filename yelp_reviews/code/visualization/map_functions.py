import numpy as np
import pandas as pd
import re

def get_map_df(df):
    """
    Prepares dataframe output from api_data.py for
    reading to mapbox function
    """
    df = df.rename(columns={"latitude": "lat", "longitude": "lon"})
    df["name"] = df["name"].str.replace("'", "")

    return df


def get_center(df):
    """
    Read lat/lon coordinates from dataFrame
    Return coordinate tuple
    """

    length = len(df)
    sum_x = np.sum(df['lat'])
    sum_y = np.sum(df['lon'])

    return [sum_y / length, sum_x / length]


def get_indicators(df, col_name):
    """
    Append indicator columns to dataframe from selected column
    I.E. Transactions: ["delivery", "pickup"]
    --> Get indicator column for "delivery", "pickup"
    Returns: appended dataframe
    """
    split_column = df[col_name].apply(lambda x: re.sub('[^A-Za-z0-9,_]+', '', x).split(","))
    temp_df = pd.DataFrame(data=split_column)
    split_df = temp_df[col_name].apply(pd.Series)

    col_list = []

    for col in split_df.columns:
        col_list.append(list(split_df[col].unique()))

    flat_list = list(set([trans for sublist in col_list for trans in sublist if trans not in [np.nan, ""]]))

    df_t = split_df.transpose()

    for item in flat_list:
        df_contains = df_t == item
        contains_ser = df_contains.sum()
        df[item] = contains_ser

    return df