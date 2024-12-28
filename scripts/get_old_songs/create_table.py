from path_config import *
from logging_config import get_logger
from general import run_query

logger = get_logger(__name__)


def create_table(**kwargs):

    query = """
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    """

    run_query(query)

    query = """
        DROP TABLE IF EXISTS spotify_old_songs;
    """
    
    run_query(query)

    query = """
        CREATE TABLE spotify_old_songs (
            spotify_old_songs_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
            spotify_old_songs_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            spotify_old_songs_stopped_playing_at TIMESTAMP NOT NULL,
            spotify_old_songs_artist_name VARCHAR(255) NOT NULL,
            spotify_old_songs_track_name VARCHAR(255) NOT NULL,
            spotify_old_songs_ms_player INTEGER NOT NULL,
            UNIQUE (spotify_old_songs_stopped_playing_at, spotify_old_songs_artist_name, spotify_old_songs_track_name, spotify_old_songs_ms_player)
        );
    """
    
    run_query(query)