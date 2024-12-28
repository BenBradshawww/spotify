from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
import os
parent_directory = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(parent_directory, 'scripts/get_old_songs/'))
sys.path.append(os.path.join(parent_directory, 'scripts/general/'))

from create_table import create_table
from get_old_songs import get_old_songs
from push_songs_to_postgres import push_songs_to_postgres

default_args = {
    'owner': 'ben',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='get_old_songs_workflow',
    description='Get old the last played songs',
    schedule=None,
) as dag:

    task1 = PythonOperator(
        task_id='create_table',
        python_callable=create_table,
    )

    task2= PythonOperator(
        task_id='get_old_songs',
        python_callable=get_old_songs, 
    )

    task3 = PythonOperator(
        task_id='push_songs_to_postgres',
        python_callable=push_songs_to_postgres, 
    )

    [task1, task2] >> task3
