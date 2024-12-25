from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta

import sys
import os
parent_directory = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(parent_directory, 'scripts/drop_table/'))
sys.path.append(os.path.join(parent_directory, 'scripts/general/'))

from drop_table import drop_table

default_args = {
    'owner': 'ben',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    default_args=default_args,
    dag_id='drop_table',
    description='Drop table workflow'
) as dag:

    task0 = PythonOperator(
        task_id='drop_table',
        python_callable=drop_table,
    )

    task0