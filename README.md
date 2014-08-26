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



### Game creation

    python examples/create_game.py

### User creation

    python examples/create_user.py

### Leaderboard creation

    python examples/create_game.py

### Leaderboard score creation

    python examples/create_game.py
