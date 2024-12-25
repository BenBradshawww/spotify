from path_config import *
from logging_config import get_logger
import requests
import csv

import spotipy

logger = get_logger(__name__)

def get_last_songs(**kwargs):

    access_token = kwargs['ti'].xcom_pull(task_ids='get_access_token', key='access_token')

    sp = spotipy.Spotify(auth=access_token)

    try:
        results = sp.current_user_recently_played(limit=50)
    except Exception as e:
        logger.error("An error occurred:", e)
        raise
    
    kwargs['ti'].xcom_push(key='results', value=results)
    
    last_songs = []

    if results:
        for item in results["items"]:

            track_played_at = item['played_at']
            spotify_track_id = item["track"]['id']

            last_songs.append((track_played_at, spotify_track_id))

    else:
        logger.info("No recently played tracks found.")
    

    kwargs['ti'].xcom_push(key='last_songs', value=last_songs)

    


    
