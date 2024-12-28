import psycopg2
from psycopg2.extras import execute_values
from path_config import *
from logging_config import get_logger

from general import run_query

def push_songs_to_postgres(**kwargs):

    values = kwargs['ti'].xcom_pull(task_ids='get_old_songs', key='old_songs')
    
    query = """
        INSERT INTO spotify_old_songs (
            spotify_old_songs_stopped_playing_at,
            spotify_old_songs_artist_name,
            spotify_old_songs_track_name,
            spotify_old_songs_ms_player
        ) VALUES %s
        ON CONFLICT (spotify_old_songs_stopped_playing_at, spotify_old_songs_artist_name, spotify_old_songs_track_name, spotify_old_songs_ms_player)
        DO UPDATE
        SET spotify_old_songs_updated_at = CURRENT_TIMESTAMP;
    """

    run_query(query, values=values)