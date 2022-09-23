import http.client, urllib.parse
import json

class Geocoding:

    def __init__(self , address):
        self.address = address
        conn = http.client.HTTPConnection('api.positionstack.com')

        params = urllib.parse.urlencode({
            'access_key': 'e183e10f93703be8bd0aa183b6217af4',
            'query': self.address,
            'region': 'New York',
            'limit': 1,
            })

        conn.request('GET', '/v1/forward?{}'.format(params))

        res = conn.getresponse()
        data = res.read()

        self.json_string = data.decode('utf-8')

    def get_lat_long(self):
        data = json.loads(self.json_string)
        return float(data['data'][0]['latitude']) , float(data['data'][0]['longitude'])