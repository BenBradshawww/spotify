from path_config import *
from logging_config import get_logger
import csv

logger = get_logger(__name__)

def save_last_songs(**kwargs):

    results = kwargs['ti'].xcom_pull(task_ids='get_last_songs', key='results')
    
    csv_rows = []

    for item in results["items"]:

        track_played_at = item['played_at']
        spotify_track_id = item["track"]['id']

        csv_rows.append((spotify_track_id, track_played_at))

    csv_path = '/Users/benbradshaw/Documents/Code/spotify/csvs/recently_played_tracks.csv'

    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_rows)

    logger.info(f"CSV file '{csv_path}' created successfully!")
