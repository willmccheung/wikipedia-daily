import datetime

today = datetime.datetime.now()
date = today.strftime('%Y/%m/%d') # Gets the day; may make it random for the year just for some variety

import requests

# Just so the key is (hopefully ^_^) not on the github
with open ('api_key.txt', 'r') as infile:
    api_key = infile.read()

language_code = 'en' # English
headers = {
    'Authorization': api_key,
    'User-Agent': 'Wiki-daily (willmccheung@gmail.com)'
}

base_url = 'https://api.wikimedia.org/feed/v1/wikipedia/'
url = base_url + language_code + '/featured/' + date
response  = requests.get(url, headers=headers)

import json

response = json.loads(response.text)

with open ('wiki_daily_featured_data.json', 'w') as out:
    json.dump(response, out, indent=4)