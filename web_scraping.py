import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def web_scrapping(dict):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}
    out = {}
    out1 = {}
    for key, value in dict.items():
        url = key
        req = urllib.request.Request(url, None, headers)
        with urllib.request.urlopen(req) as response:
            page = response.read()
        for v1, v2 in value.items():
            soup = BeautifulSoup(page, 'html.parser')
            out1.update({v2 : soup.find(re.compile(v1), attrs={'class': re.compile(v2)}).text.strip()})
        out.update({url:out1})
    return(out)

print(web_scrapping({'http://www.bloomberg.com/quote/SPX:IND': {'div':'companyName','span':'priceText'}}))