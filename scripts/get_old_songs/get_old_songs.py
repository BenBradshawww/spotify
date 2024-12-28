from path_config import *
from logging_config import get_logger
import os
import json

logger = get_logger(__name__)

old_songs = []

def get_songs(file_path):

    with open(file_path, "r") as f:
        data = f.read()
        json_data = json.loads(data)
        process_json_data(json_data)

def process_json_data(json_data):
    for item in json_data:
        old_songs.append((item['endTime'], item['artistName'], item['trackName'], item['msPlayed']))
        

def get_old_songs(**kwargs):
    
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data/streaming_history/")
    files = os.listdir(path)

    json_files = [file for file in files if file.endswith(".json")]

    if not json_files:
        logger.warning(f"No JSON files found in: {path}")
        return

    for file in json_files:
        file_path = os.path.join(path, file)
        get_songs(file_path)
    
    kwargs['ti'].xcom_push(key='old_songs', value=old_songs)
    

    
    