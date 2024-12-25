from path_config import *
from general import run_query

def drop_table(**kwargs):

    query = """
        DROP TABLE IF EXISTS spotify_last_songs;
    """
    
    run_query(query)
        