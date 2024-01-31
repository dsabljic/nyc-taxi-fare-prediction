import http.client, urllib.parse
import json
import streamlit as st

class Geocoding:

    def __init__(self , address):
        self.address = address
        conn = http.client.HTTPConnection('api.positionstack.com')

        params = urllib.parse.urlencode({
            'access_key': st.secrets['position_stack_api'], # replace with your own API key if you're running it locally
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