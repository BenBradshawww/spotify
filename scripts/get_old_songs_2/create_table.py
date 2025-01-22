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
        DROP TABLE IF EXISTS spotify_old_songs CASCADE;
    """
    
    run_query(query)

    query = """
        CREATE TABLE spotify_old_songs (
            spotify_old_songs_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
            spotify_old_songs_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            spotify_old_songs_track_id VARCHAR(255) NOT NULL,
            spotify_old_songs_started_playing_at TIMESTAMP NOT NULL,
            spotify_old_songs_artist_name VARCHAR(255) NOT NULL,
            spotify_old_songs_track_name VARCHAR(255) NOT NULL,
            spotify_old_songs_album_name VARCHAR(255) NOT NULL,
            spotify_old_songs_ms_player INTEGER NOT NULL,
            spotify_old_songs_reason_start VARCHAR(255),
            spotify_old_songs_reason_end VARCHAR(255),
            spotify_old_songs_shuffle BOOLEAN,
            spotify_old_songs_skipped BOOLEAN,
            spotify_old_songs_offline BOOLEAN
        );
    """
    
    run_query(query)
