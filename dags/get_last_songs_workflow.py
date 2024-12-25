from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
import os
parent_directory = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(parent_directory, 'scripts/get_last_songs/'))
sys.path.append(os.path.join(parent_directory, 'scripts/general/'))

from create_table import create_table
from get_last_songs import get_last_songs
from get_access_token import get_access_token
from push_songs_to_postgres import push_songs_to_postgres

default_args = {
    'owner': 'ben',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='get_last_songs_workflow',
    description='Get the last played songs',
    schedule=None,
) as dag:

    task1 = PythonOperator(
        task_id='create_table',
        python_callable=create_table,
    )

    task2 = PythonOperator(
        task_id='get_access_token',
        python_callable=get_access_token,
    )

    task3= PythonOperator(
        task_id='get_last_songs',
        python_callable=get_last_songs, 
    )

    task4 = PythonOperator(
        task_id='push_songs_to_postgres',
        python_callable=push_songs_to_postgres, 
    )

    [task1, task2 >> task3] >> task4
