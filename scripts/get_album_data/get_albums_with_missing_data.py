import psycopg2
from psycopg2.extras import execute_values
from path_config import *
from logging_config import get_logger

from general import run_query

def get_albums_with_missing_data(**kwargs):
    
    query = """
        SELECT DISTINCT
            spotify_old_songs_album_name
        FROM base_spotify__old_songs
        WHERE spotify_old_songs_album_name IS NOT NULL
    """

    albums = run_query(query)

    kwargs['ti'].xcom_push(key='albums', value=albums)