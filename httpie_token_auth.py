"""
Token Auth plugin for HTTPie.
"""

import os
import sys
try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit

import requests
from httpie.plugins import AuthPlugin, builtin


auth_endpoint = os.environ.get('HTTPIE_TOKEN_AUTH_URL', '/api/token/new.json')


class TokenAuth(builtin.HTTPBasicAuth):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, r):
        host = "{0.scheme}://{0.netloc}".format(urlsplit(r.url))
        login_url = host + auth_endpoint
        print(login_url)
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = requests.post(login_url, data=data)
        json = response.json()
        try:
            user = str(json['user'])
            token = json['token']
        except KeyError:
            print('Invalid credentials')
            sys.exit()
        r.headers['Authorization'] = type(self).make_header(user, token).encode('latin1')
        return r


class TokenAuthPlugin(AuthPlugin):

    name = 'token auth'
    auth_type = 'token'
    description = 'Sign requests using a token authentication method like AWS'

    def get_auth(self, username=None, password=None):
        return TokenAuth(username, password)
