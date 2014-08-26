#-*- coding: utf-8 -*-
import json

import requests

import settings


def make_request(data=None):
    data = json.dumps(data or {
        'name': u'Pokéballs Collected',
        'slug': u'pokeballs-collected',
        'description': u'This keeps track of how many pokéballs a user finds.'
    })

    return requests.post(settings.API_URL + '/games/pokemon/leaderboards', data)


if __name__ == '__main__':
    make_request()
