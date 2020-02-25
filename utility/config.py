from requests_oauthlib import OAuth1Session
import json

with open('../user_tokens.json', 'r') as data:
    data = json.load(data)
client_key = data.get('client_key')
client_secret = data.get('client_secret')
resource_owner_key = data.get('resource_owner_key')
resource_owner_secret = data.get('resource_owner_secret')

trello = OAuth1Session(client_key=client_key,
                       client_secret=client_secret,
                       resource_owner_key=resource_owner_key,
                       resource_owner_secret=resource_owner_secret)
