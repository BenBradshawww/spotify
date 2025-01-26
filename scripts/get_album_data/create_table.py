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
        DROP TABLE IF EXISTS spotify_albums;
    """
    
    run_query(query)

    query = """
        CREATE TABLE IF NOT EXISTS spotify_albums (
            spotify_albums_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
            spotify_albums_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            spotify_albums_album_name VARCHAR(255) NOT NULL,
            spotify_albums_album_id VARCHAR(255) NOT NULL,
            spotify_albums_album_type VARCHAR(255) NOT NULL,
            spotify_albums_album_total_tracks INT NOT NULL,
            spotify_albums_album_release_date VARCHAR(255) NOT NULL,
            spotify_albums_artist_name VARCHAR(255) NOT NULL,
            spotify_albums_artist_id VARCHAR(255) NOT NULL,
            UNIQUE (spotify_albums_album_id, spotify_albums_album_name)
        );
    """
    
    run_query(query)