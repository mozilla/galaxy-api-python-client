#-*- coding: utf-8 -*-
import json

import requests

import settings


def make_request(data=None):
    data = json.dumps(data or {
        'name': u'Pokémon',
        'slug': u'pokemon',
        'app_url': u'http://www.fullscreenpokemon.com/',
        'description': u'Full Screen Pokemon is an open source HTML5 remake of '
                       u'the original Pokemon games. You can play the original '
                       u'two generations (Red/Blue through Crystal), literally '
                       u'billions of procedurally generated maps, or create '
                       u'your own using the level editor.'
    })

    return requests.post(settings.API_URL + '/games', data)


if __name__ == '__main__':
    make_request()
