import os
import urllib.parse

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from logging_config import get_logger

logger = get_logger(__name__)

from dotenv import load_dotenv
load_dotenv()

def get_access_token(**kwargs):

    sp_oauth = SpotifyOAuth(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        redirect_uri=os.environ.get('REDIRECT_URI'),
        scope="user-read-recently-played",
        cache_path=os.environ.get('CACHE_PATH'),
    )
    
    if os.path.exists(os.environ.get('CACHE_PATH')):
        logger.info(f"Cache file found at {os.environ.get('CACHE_PATH')}")
    else:
        logger.warning(f"No cache file found at {os.environ.get('CACHE_PATH')}")


    token_info = sp_oauth.get_access_token()
    access_token = token_info['access_token']

    kwargs['ti'].xcom_push(key='access_token', value=access_token)
