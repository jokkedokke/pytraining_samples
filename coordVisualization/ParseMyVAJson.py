#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 3 12:55:00 2022

@author: jokkedokke

Parse a myVideoAnalyzer json export into a pandas dataframe
"""
import pandas as pd
import os
import json

def parse_myva_file(filename):
    """
    Parses the myVA into a pandas df

    Parameters
    ----------
    filename : string
        (Preferable absolute) path to the myVA file to be opened

    Returns
    -------
    json_df : pandas dataframe
        The highlight and event data in a dataframe
    """
    json_df = pd.DataFrame()

    if os.path.isfile(filename):
        with open(filename, 'r') as data_file:
            data = json.loads(data_file.read())

    tmp_df = pd.json_normalize(data['rows'], errors='ignore', sep='_')

    i = 0
    for key, row in tmp_df.iterrows():
        for h in row.highlights:
            json_df.at[i, 'Name'] = row['name']
            json_df.at[i, 'Start'] = h['start']
            json_df.at[i, 'End'] = h['end']
            json_df.at[i, 'Duration'] = h['end'] - h['start']

            # Parse highlights extra parameters, extra name should be category:value
            for e in h['events']:
                (category, value) = e['name'].split(':')
                if (category in json_df.columns) and (not pd.isna(json_df.at[i, category])) and (not pd.isnull(json_df.at[i, category])):
                    json_df.at[i, category] = f"{json_df.at[i, category]}, {value}"
                else:
                    json_df.at[i, category] = value

            i += 1

    return json_df
