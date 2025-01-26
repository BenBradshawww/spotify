from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
import sys
import os

# Organize imports
parent_directory = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(parent_directory, 'scripts/get_album_data/'))
sys.path.append(os.path.join(parent_directory, 'scripts/general/'))

from create_table import create_table
from get_albums_with_missing_data import get_albums_with_missing_data
from push_albums_to_postgres import push_albums_to_postgres
from get_all_albums_data import get_all_albums_data

default_args = {
    'owner': 'ben',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='get_album_data',
    description='Import album data', 
    schedule=None,
    catchup=False, 
) as dag:

    task1 = PythonOperator(
        task_id='create_table',
        python_callable=create_table,
    )

    task2= PythonOperator(
        task_id='get_albums_with_missing_data',
        python_callable=get_albums_with_missing_data, 
    )

    task3= PythonOperator(
        task_id='get_all_albums_data',
        python_callable=get_all_albums_data, 
    )

    task4 = PythonOperator(
        task_id='push_albums_to_postgres',
        python_callable=push_albums_to_postgres, 
    )

    [task1, task2 >> task3] >> task4