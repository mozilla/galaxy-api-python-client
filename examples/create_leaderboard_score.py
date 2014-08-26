#-*- coding: utf-8 -*-
import json

import requests

import settings


def make_request(data=None):
    data = json.dumps(data or {
        'user': u'cvan',
        'score': 50
    })

    return requests.post(settings.API_URL +
       '/games/pokemon/leaderboards/pokeballs-collected/scores', data)


if __name__ == '__main__':
    make_request()
