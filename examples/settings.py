API_URL = 'http://localhost:4000'

# Override the above with local settings.
try:
    from settings_local import *
except ImportError:
    pass
