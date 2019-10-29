import sys

import requests


def main():

    token = get_token()
    return token


def get_token():
    data = {'test': 'testThing'}
    response = requests.post('url',
                             data=data,
                             headers={
                                'Authorization': 'Auth'})

    token = response.json()
    return token['access_token']
