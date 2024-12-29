import psycopg2
from psycopg2.extras import execute_values
from path_config import *
from logging_config import get_logger

from general import run_query

def push_songs_to_postgres(**kwargs):

    values = kwargs['ti'].xcom_pull(task_ids='get_last_songs', key='last_songs')
    
    query = """
        INSERT INTO spotify_last_songs (
            spotify_last_songs_track_played_at,
            spotify_last_songs_track_id,
            spotify_last_songs_artist_name,
            spotify_last_songs_track_name
        ) VALUES %s
        ON CONFLICT (spotify_last_songs_track_id, spotify_last_songs_track_played_at)
        DO UPDATE
        SET spotify_last_songs_updated_at = CURRENT_TIMESTAMP;
    """

    run_query(query, values=values)