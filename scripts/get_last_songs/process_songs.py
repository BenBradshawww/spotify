import pandas as pd
import json

from path_config import *
from logging_config import get_logger

logger = get_logger(__name__)


def process_songs(data):
    
    list_of_dataframes = []

    for item_path, json_string in data: 

        if json_string.startswith('```json'):
            json_string = json_string.strip('```json').strip('```').strip()

        item = json.loads(json_string)
        
        questions_list = []
        answers_list = []

        for question_and_answer in item['questions']:
            questions_list.append(question_and_answer['question'])
            answers_list.append(question_and_answer['question'])
        
        df = pd.DataFrame([questions_list, answers_list], columns=['question', 'answer'])
        df['item_path'] = item_path
        df['title'] = item['title']
        df['authors'] = ', '.join(item['authors'])
        df['pdf_created_at'] = get_pdf_creation_data(pdf_path=item_path)
        df['pdf_updated_at'] = get_pdf_updated_data(pdf_path=item_path)

        list_of_dataframes.append(df)

    combined_df = pd.concat(list_of_dataframes, ignore_index=True)


    kwargs['ti'].xcom_push(key='df', value=combined_df)
