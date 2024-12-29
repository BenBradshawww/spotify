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
        CREATE TABLE IF NOT EXISTS spotify_last_songs (
            spotify_last_songs_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
            spotify_last_songs_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            spotify_last_songs_track_played_at TIMESTAMP NOT NULL,
            spotify_last_songs_track_id VARCHAR(255) NOT NULL,
            spotify_last_songs_artist_name VARCHAR(255) NOT NULL,
            spotify_last_songs_track_name VARCHAR(255) NOT NULL,
            UNIQUE (spotify_last_songs_track_id, spotify_last_songs_track_played_at)
        );
    """
    
    run_query(query)