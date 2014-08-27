# galaxy-api-python-client

This is a collection of Python scripts demonstrating use of [Galaxy's REST API](https://github.com/mozilla/galaxy-api).


## Installation

If you don't already have `pip` installed, do that now:

    sudo easy_install pip

If you do have `pip` installed, make sure you have an up-to-date version installed:

    pip install --upgrade pip

Install the required Python packages:

    pip install -r requirements.txt

Initialise the local settings:

    cp examples/settings_local.py.dist examples/settings_local.py

Any setting specified here overrides the respective setting defined in `settings.py`.


## Examples

## Run everything

    python examples/play_game.py

### Game creation

    python examples/create_game.py

### User creation

    python examples/create_user.py

### Leaderboard creation

    python examples/create_leaderboard.py

### Leaderboard score creation

    python examples/create_leaderboard_score.py

## Example output

```
%% python examples/play_game.py


*******************************************************************************


Request body:

{
  "app_url": "http://www.fullscreenpokemon.com/", 
  "slug": "pokemon", 
  "description": "Full Screen Pokemon is an open source HTML5 remake of the original Pokemon games. You can play the original two generations (Red/Blue through Crystal), literally billions of procedurally generated maps, or create your own using the level editor.", 
  "name": "Pok\u00e9mon"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "slug": "pokeballs-collected", 
  "description": "This keeps track of how many pok\u00e9balls a user finds.", 
  "name": "Pok\u00e9balls Collected"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "score": 39, 
  "user": "bill"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "score": 50, 
  "user": "cvan"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "score": 72, 
  "user": "david"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "score": 84, 
  "user": "toby"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "score": 99, 
  "user": "mark"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "score": 101, 
  "user": "rick"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

{
  "score": 4, 
  "user": "wil"
}


Response status code:

200


Response body:

{
  "success": true
}


*******************************************************************************


Request body:

N/A


Response status code:

200


Response body:

[
  {
    "member": "rick", 
    "score": "101"
  }, 
  {
    "member": "mark", 
    "score": "99"
  }, 
  {
    "member": "toby", 
    "score": "84"
  }, 
  {
    "member": "david", 
    "score": "72"
  }, 
  {
    "member": "cvan", 
    "score": "50"
  }, 
  {
    "member": "bill", 
    "score": "39"
  }, 
  {
    "member": "wil", 
    "score": "4"
  }
]


*******************************************************************************


```
