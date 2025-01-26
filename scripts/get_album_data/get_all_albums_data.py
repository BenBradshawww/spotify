from path_config import *
from logging_config import get_logger
import spotipy
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

logger = get_logger(__name__)

def get_all_albums_data(**kwargs):

    albums = kwargs['ti'].xcom_pull(task_ids='get_albums_with_missing_data', key='albums')

    rows = []
    for album in albums:
        rows.extend(get_album_data(album[0]))
    
    kwargs['ti'].xcom_push(key='album_data', value=rows)

def get_album_data(album: str):
    auth_manager = SpotifyClientCredentials(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)

    results = sp.search(q='album:' + album, type='album', limit=1, offset=0)
    
    album_data = []

    if results['albums']['items']:
        item = results['albums']['items'][0]
        
        album_info = (
            item['id'],                     # album_id
            item['name'],                   # album_name
            item['album_type'],             # album_type
            item['total_tracks'],           # total_tracks
            item['release_date'],           # release_date
            item['artists'][0]['name'],     # artist_name
            item['artists'][0]['id'],       # artist_id
        )
        
        album_data.append(album_info)
        logger.info(f"Found album data for: {album}")
    else:
        logger.info(f"No album found for: {album}")
    
    return album_data