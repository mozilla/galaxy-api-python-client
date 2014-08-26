#-*- coding: utf-8 -*-
import json

import requests

import settings


game = {
    'name': u'Pokéballs Found',
    'slug': u'pokeballs-found',
    'description': u'This keeps track of how many pokéballs a user finds.'
}

data = json.dumps(game, indent=2)

req  = requests.post(settings.API_URL + '/games/pokemon/leaderboards', data)

print 'Request body:'
print data
print
print 'Response status code:'
print req.status_code
print
print 'Response body:'
print json.dumps(json.loads(req.content), indent=2)
