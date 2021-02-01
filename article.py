#!/usr/bin/env python3

import requests
import pandas as pd

#Created this function to help get the content from a website. If you are going to reuse a block of code maybe you should make it a function 

url = "https://countrycode.org/"

def get_url(url):
    response = requests.get(url).content
    return response 

site_url = get_url(url)
table = pd.read_html(site_url)
table_df = pd.DataFrame(table[-2])
table_df.to_csv("country_code.csv",index=False)