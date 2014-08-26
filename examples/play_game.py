import json

import create_game
import create_leaderboard
import create_leaderboard_score
import get_leaderboard_scores


def print_heading(txt):
    print '\n\033[34m\033[1m' + txt + '\x1B[m\n'


def print_divider():
    print '\n\033[90m\n' + '*' * 79 + '\x1B[m\n'


def print_request(req):
    print_heading('Request body:')
    try:
        print json.dumps(json.loads(req.request.body), indent=2)
    except TypeError:
        print 'N/A'
    print

    print_heading('Response status code:')
    print req.status_code
    print

    print_heading('Response body:')
    print json.dumps(json.loads(req.content), indent=2)


print_divider()

print_request(create_game.make_request())

print_divider()

print_request(create_leaderboard.make_request())

print_divider()

print_request(create_leaderboard_score.make_request())

print_divider()

print_request(get_leaderboard_scores.make_request())

print_divider()
