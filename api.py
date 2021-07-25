from flask import Flask, request, jsonify
from flask_caching import Cache 
from olympic.rankings import get_rankings

import logging

config = {
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 60
}

app = Flask(__name__, static_url_path='')
app.config.from_mapping(config)
cache = Cache(app)

logging.basicConfig(filename='api.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

@app.route('/')
def index(): 
    return '<h2>Olympic Games Tokyo 2020 Rankings API</h2><br><br\> \
            <a href="#">Documentation</a>'

@app.route('/api/olympic/rankings')
@cache.cached(timeout=60, query_string=True)
def rankings():
    country = request.args.get('country')
    logging.debug(f'Request -> Country: {country}')

    rankings = get_rankings()

    if country:
        return jsonify(get_country(country, rankings))

    return jsonify(rankings)

def get_country(country, rankings):
    try:
        if len(country) == 3:
            for country_ranking in rankings:
                if country.lower() == country_ranking['country_alpha3'].lower():
                    return country_ranking
        return rankings
    except Exception as e:
        logging.error(f'Error: Request for country failed -> {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0')