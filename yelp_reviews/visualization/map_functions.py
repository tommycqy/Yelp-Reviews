import numpy as np
import pandas as pd
import re
from mapboxgl.utils import create_color_stops, df_to_geojson
from mapboxgl.viz import CircleViz

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


def get_filter_indicator_df(df, filter_col, col_list):
    """
    Filter indicator dataframe based on list of columns
    Returns dataframe
    """

    df_indicator = get_indicators(df, filter_col)
    df_filter = pd.DataFrame(columns = df_indicator.columns)

    for col in col_list:

        df_temp = df_indicator.loc[df_indicator[col] == 1]
        df_filter = df_filter.append(df_temp)

    return df_filter


def get_viz(df):
    """
    Converts dataframe to geoJSON
    Then renders to MapBox map
    Returns: MapBox map
    """

    access_token = 'pk.eyJ1IjoiZW1pOTAiLCJhIjoiY2tsaG9penkxMmY1cTJ2czZyNmQ5c3I2MCJ9.AaHgMWQdOv-SwzWj_nYvDg'

    rest_json = df_to_geojson(df.fillna(''),
                              properties=['name', 'rating', 'price'],
                              precision=4)

    df_center = get_center(df)

    category_color_stops = [['$', 'rgb(211,47,47)'],
                            ['$$', 'rgb(81,45,168)'],
                            ['$$$', 'rgb(2,136,209)'],
                            ['$$$$', 'rgb(255,160,0)']]

    viz = CircleViz(rest_json,
                    access_token=access_token,
                    label_property='name',
                    color_property='price',
                    color_function_type='match',
                    color_stops=category_color_stops,
                    center=df_center,
                    zoom=13)

    return viz