# Tokyo 2020 Olympics Rankings API 

![tokyo](https://i.imgur.com/0K6DUZa.png)

Simple Flask or ApiGateway + Lambda powered implementation of an endpoint that returns the current Tokyo Olympic rankings and medal tallys in a JSON format. 

Data source: [Official Olympic Site](https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm) 

## Usage 

Endpoint currently hosted on AWS EC2 for free use: http://3.25.134.23/ 

**Get the entire ranking table:** 

http://3.25.134.23/api/olympic/rankings

**Retrieve country current standings:** 

Using [ISO Alpha 3 Country Codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)

http://3.25.134.23/api/olympic/rankings?country=AUS

## Example Response 

```
[
  {
    "country": "Japan",
    "country_alpha3": "JPN",
    "rank": 1,
    "medals": {
      "gold": 3,
      "silver": 1,
      "bronze": 0,
      "total": 4
    }
  },
  {
    "country": "United States of America",
    "country_alpha3": "USA",
    "rank": 3,
    "medals": {
      "gold": 1,
      "silver": 2,
      "bronze": 4,
      "total": 7
    }
  },
  {
    "country": "Australia",
    "country_alpha3": "AUS",
    "rank": 4,
    "medals": {
      "gold": 1,
      "silver": 1,
      "bronze": 1,
      "total": 3
    }
  },
  ...
]
```

## Running 

### AWS 

#### Requirements

- [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- AWS Account 

#### Deploying 

1. In the `aws\olympic-api` folder 
2. `sam build`
3. `sam deploy`

### Locally with Flask

#### Requirements

- Python 3.8+ 
- Gunicorn 

#### Running

1. Install requirements: `pip install -r requirements.txt` 
2. Run development server with: `python api.py` OR 
3. Run production server with: `./run.sh` 


## Other

Branding, data, and other relevant properties. 

© 2021 – The Tokyo Organising Committee of the Olympic and Paralympic Games