#-*- coding: utf-8 -*-
import requests

import settings


def make_request(data=None):
    return requests.get(settings.API_URL +
        '/games/pokemon/leaderboards/pokeballs-collected/scores')


if __name__ == 'main':
    make_request()
