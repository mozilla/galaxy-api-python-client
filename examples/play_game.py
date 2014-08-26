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

scores = [
    {
        'user': 'bill',
        'score': 39
    },
    {
        'user': 'cvan',
        'score': 50
    },
    {
        'user': 'david',
        'score': 72
    },
    {
        'user': 'toby',
        'score': 84
    },
    {
        'user': 'mark',
        'score': 99
    },
    {
        'user': 'rick',
        'score': 101
    },
    {
        'user': 'wil',
        'score': 4
    }
]

for score in scores:
    print_divider()

    print_request(create_leaderboard_score.make_request(score))

print_divider()

print_request(get_leaderboard_scores.make_request())

print_divider()
