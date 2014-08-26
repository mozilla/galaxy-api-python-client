#-*- coding: utf-8 -*-
import json

import requests

import settings


game = {
    'name': u'Pokémon',
    'slug': u'pokemon',
    'app_url': u'http://www.fullscreenpokemon.com/',
    'description': u'Full Screen Pokemon is an open source HTML5 remake of '
                   u'the original Pokemon games. You can play the original '
                   u'two generations (Red/Blue through Crystal), literally '
                   u'billions of procedurally generated maps, or create '
                   u'your own using the level editor.'
}


req  = requests.post(settings.API_URL + '/games',
                     json.dumps(game, indent=2))

print 'Status code:'
print req.status_code
print
print 'Response:'
print json.dumps(json.loads(req.content), indent=2)
