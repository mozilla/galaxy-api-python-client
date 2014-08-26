#-*- coding: utf-8 -*-
import json

import requests

import settings


game = {
    'name': u'Pokéballs Found',
    'slug': u'pokeballs-found',
    'description': u'This keeps track of how many pokéballs a user finds.'
}


req  = requests.post(settings.API_URL + '/games/pokemon/leaderboards',
                     json.dumps(game, indent=2))

print 'Status code:'
print req.status_code
print
print 'Response:'
print json.dumps(json.loads(req.content), indent=2)
