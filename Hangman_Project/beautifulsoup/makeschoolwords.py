import re
import requests
import bs4 as bs
import urllib
from urllib.request import urlopen
import json

def get_list_href():
    url = 'https://www.makeschool.com/'
    url_request = requests.get(url)
    url_request.raise_for_status()
    soup_final = bs.BeautifulSoup(url_request.text, 'lxml')

 

    words = soup_final.get_text() 
    # words_list = []
    
    # for i in words:
    #     words_list.append(i)

    print(words)
get_list_href()