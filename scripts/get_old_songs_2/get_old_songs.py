from path_config import *
from logging_config import get_logger
import os
import json

logger = get_logger(__name__)

old_songs = []

def process_songs(file_path):

    with open(file_path, "r") as f:
        data = f.read()
        json_data = json.loads(data)
        process_json_data(json_data)

def process_json_data(json_data):
    for item in json_data:
        if item['master_metadata_track_name'] is not None:
            track_id = item['spotify_track_uri'].split(':')[-1]
            started_playing_at = item['ts']
            artist_name = item['master_metadata_album_artist_name']
            track_name = item['master_metadata_track_name']
            album_name = item['master_metadata_album_album_name']
            ms_played = item['ms_played']
            reason_start = item['reason_start']
            reason_end = item['reason_end']
            shuffle = item['shuffle']
            skipped = item['skipped']
            offline = item['offline']
            
            old_songs.append((
                track_id,
                started_playing_at,
                artist_name,
                track_name, 
                album_name,
                ms_played,
                reason_start,
                reason_end,
                shuffle,
                skipped,
                offline,
            ))

def get_old_songs(**kwargs):
    
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data/streaming_history/")
    files = os.listdir(path)

    json_files = [file for file in files if file.endswith(".json")]

    if not json_files:
        logger.warning(f"No JSON files found in: {path}")
        return

    for file in json_files:
        file_path = os.path.join(path, file)
        process_songs(file_path)
    
    kwargs['ti'].xcom_push(key='old_songs', value=old_songs)
