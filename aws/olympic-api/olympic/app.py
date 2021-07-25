import json
import requests
import time
from bs4 import BeautifulSoup

PAGE_URL = 'https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm'

def get_table(html=None):
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
    
def lambda_handler(event, context):
    try:
        country = event['queryStringParameters']['country']
    except:
        country = None 

    print(f'Request -> Country: {country}')
    
    rankings = get_rankings()
    
    if country:
        if len(country) == 3:
            for country_ranking in rankings:
                if country == country_ranking['country_alpha3']:
                    rankings = country_ranking
    
    return {
        "statusCode": 200,
        "body": json.dumps(rankings),
        "isBase64Encoded": False
    }