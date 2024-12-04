import json

with open('wiki_daily_featured_data.json', 'r') as inf:
    data = json.load(inf)

display_title = data['tfa']['normalizedtitle']
desktop_url = data['tfa']['content_urls']['desktop']['page']
extract_html = data['tfa']['extract']
date = data['tfa']['timestamp'].split('T')

print('\n------- Daily Wikipedia -------')
print('Featured Article for ' + date[0] + ': ' + display_title + '\n')
print(extract_html + '\n')
print('Link to article: ' + desktop_url)
print('-------------------------------\n')