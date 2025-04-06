import json
import os

with open('wiki_daily_featured_data.json', 'r') as inf:
    data = json.load(inf)

if 'title' in data:
    print('\n------- Daily Wikipedia -------')
    print('\nShit did not work\n')
    print('-------------------------------\n')

else:
    display_title = data['tfa']['normalizedtitle']
    desktop_url = data['tfa']['content_urls']['desktop']['page']
    extract_html = data['tfa']['extract']
    date = data['tfa']['timestamp'].split('T')

    print('\n------- Daily Wikipedia -------')
    print('Featured Article for ' + date[0] + ': ' + display_title + '\n')
    print(extract_html + '\n')
    print('Link to article: ' + desktop_url)
    print('-------------------------------\n')