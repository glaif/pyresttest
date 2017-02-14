import requests

APP_ID = 'a864c29e-ae26-4c91-9e1e-c66b6557d78a'

def _url(path):
    return 'https://' + path

def get_itemid():
    pass

def get_itemid_root():
    pass

#GET https://login.live.com/oauth20_authorize.srf?client_id={client_id}&scope={scope}&response_type=token&redirect_uri={redirect_uri}
def authenticate(scope, redirect_uri):
    payload = {'client_id':APP_ID, 'scope':scope, 'response_type':'token',
            'redirect_uri':redirect_uri}
    return requests.get('https://login.live.com/oauth20_authorize.srf', params=payload)

resp = authenticate('onedrive.readwrite ', 'http://localhost:8000/')
print(resp)

