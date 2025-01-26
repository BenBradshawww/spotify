import psycopg2
from psycopg2.extras import execute_values
from path_config import *
from logging_config import get_logger

from general import run_query

def push_albums_to_postgres(**kwargs):

    values = kwargs['ti'].xcom_pull(task_ids='get_all_albums_data', key='album_data')
    print(values)
    query = """
        INSERT INTO spotify_albums (
            spotify_albums_album_id,
            spotify_albums_album_name,
            spotify_albums_album_type,
            spotify_albums_album_total_tracks,
            spotify_albums_album_release_date,
            spotify_albums_artist_name,
            spotify_albums_artist_id
        ) VALUES %s
        ON CONFLICT (spotify_albums_album_id, spotify_albums_album_name)
        DO UPDATE
        SET spotify_albums_updated_at = CURRENT_TIMESTAMP;
    """

    run_query(query, values=values)


    