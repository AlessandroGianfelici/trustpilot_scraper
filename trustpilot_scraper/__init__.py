# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:04:00 2018

@author: Alessandro Gianfelici
"""

__version__ = '0.2.0'

from bs4 import BeautifulSoup
import pandas as pd
from langdetect import detect

myLongNamedDictionary = {}
null = None

def scrapeTrustPilot(body : str):
    """
    This function take the url of the trustpilot page of the company you are interested in 
    and return as output a pandas dataframe containing the following columns:
     - review_title
     - review_text
     - review_stars
    :param input_url: The url of the trustpilot page of the company you are interested in.
    :type input_url: str
    :return: reviews
    :rtype: pd.DataFrame
    """   
    titolo = []
    testo = []
    stelle = []
    lingua = []
    html_soup = BeautifulSoup(body, 'html.parser')
    recensioni = html_soup.find_all('div', class_ = 'review-card')
    for recensione in recensioni:
        false = 'False'
        exec(f"global myLongNamedDictionary; global null; myLongNamedDictionary = {recensione.script.contents[0][1:-1]}")
        titolo.append(myLongNamedDictionary['reviewHeader'])
        testo.append(myLongNamedDictionary['reviewBody'])
        stelle.append(myLongNamedDictionary['stars'])
        lingua.append(detect(myLongNamedDictionary['reviewBody']))
    data = {'company_name' : myLongNamedDictionary['businessUnitDisplayName'],
            'review_title' : titolo,
            'review_text' : testo,
            'review_stars' : stelle,
            'language' : lingua}
    return pd.DataFrame(data).drop_duplicates()
