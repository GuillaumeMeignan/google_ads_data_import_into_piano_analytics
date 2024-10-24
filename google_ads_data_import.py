import http.client
import csv
import json

path = '.../google_ads_data.csv'

piano_site_id = 123456
access_key = ''
secret_key = ''

data = []

with open(path, mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        data.append({
            'key': 'google_ads_data_import',
            'period': str(row[0]),
            'values': {
                'm_ads_spend': float(row[3].replace(',', '.')),
                'm_ads_impressions': int(row[4]),
                'm_ads_clics': int(row[5]),
                'm_ads_conversions': int(row[6])
            },
            'properties': {
                'src': 'Sponsored links',
                'src_campaign_group': 'google',
                'src_campaign': '[' + str(row[1]) + ']',
                'src_variant': '[' + str(row[2]) + ']'
            },
            'site_id': piano_site_id
        })

composite_list = [data[x : x + 300] for x in range(0, len(data), 300)]

for row in composite_list:
    conn = http.client.HTTPSConnection('analytics-api-eu.piano.io')

    payload = json.dumps({ 'measurements': row })

    headers = { 'x-api-key': access_key + '_' + secret_key, 'Content-type': 'application/json' }
    conn.request('POST', '/import/measurements/v1', payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode('utf-8'))