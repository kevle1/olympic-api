import requests
import time
#from functools import lru_cache
from bs4 import BeautifulSoup

PAGE_URL = 'https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm'

#@lru_cache()
def get_table(html=None, cache_invalidate=None):
    del cache_invalidate # Do nothing with this, simply to invalidate cache

    if not html: html = requests.get(PAGE_URL).content

    site = BeautifulSoup(html, 'html.parser')
    table = site.find('table', { 'id': 'medal-standing-table' })
    return table.findAll('tr')[1:] # Remove header

def get_num(value):
    try:
        return int(value.find('a').getText())
    except: 
        return 0

def get_counts(entry):
    values = entry.findAll('td', { 'class': 'text-center'})

    return int(values[0].find('strong').getText()), { # 4 total, 3 bronze, 2 silver, 1 gold, 0 rank 
        'gold': get_num(values[1]),
        'silver': get_num(values[2]),
        'bronze': get_num(values[3]),
        'total': get_num(values[4]),
    }

def cache_invalidate(seconds=60): # Invalidate cache 
    return round(time.time() / seconds)

def get_rankings():
    rankings = []

    for country in get_table():
        rank, medals = get_counts(country)

        rankings.append({
            'country': country.find('a', { 'class': 'country'}).getText(),
            'country_alpha3': country.find('div', { 'class': 'playerTag'})['country'],
            'rank': rank,
            'medals': medals
        })

    return rankings