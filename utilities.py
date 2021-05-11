# -*- encoding: utf-8 -*-

"""Web-Scrapping of a URL using Beautiful-Soup"""

__author__       = "Debmalya Pramanik"
__author_email__ = "Debmalya.18KT0018@ee.iitism.ac.in"

__credits__      = None

__status__       = "Development"
__version__      = "0.1-deleop"
__docformat__    = "camelCasing"

__copyright__    = "Copyright (c) 2021 Debmalya Pramanik"
__affiliation__  = "Reliance Jio Platforms Ltd. | IIT Dhanbad"


import requests
import bs4 as bs

def getContent(url : str, ) -> list:
    """Given a URL, this function Parse all the `<a>...</a>`, and returns it as a List"""

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    try:
        html = requests.get(url, headers)
    except Exception as err:
        raise ConnectionError("Unable to Fetch Data from URL", err)

    soup = bs.BeautifulSoup(html.content, "html.parser")
    return soup.find_all("a")