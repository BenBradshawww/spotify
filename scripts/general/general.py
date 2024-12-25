import psycopg2
from psycopg2.extras import execute_values
import os

from logging_config import get_logger

logger = get_logger(__name__)

def run_query(query, values=None):

    conn = psycopg2.connect(
        host="postgres",
        database=os.getenv('POSTGRES_DATABASE'),
        user=os.getenv('POSTGRES_USERNAME'),
        password=os.getenv('POSTGRES_PASSWORD'),
        port=os.getenv('POSTGRES_PORT'),
    )

    cursor = conn.cursor()

    try:
        logger.info(f'Running query: {query}')

        if 'INSERT' in query:
            execute_values(cursor, query, values)
            logger.info(f'Query run successfully')
            conn.commit()

        elif 'SELECT' in query:
            execute_values(cursor, query)
            logger.info(f'Query run successfully')
            conn.commit()

            if cursor.description:
                return cursor.fetchall()
            else:
                logger.info("No rows returned for the query.")
                return []
        else:
            cursor.execute(query)
            logger.info(f'Query run successfully')
            conn.commit()

    except psycopg2.OperationalError as e:
        logger.error(f"Operational Error: {e.pgcode} - {e.pgerror}")
        conn.rollback()
        raise ValueError(f"Operational issue occurred: {e.pgcode}")

    except psycopg2.IntegrityError as e:
        logger.error(f"Integrity Error: {e.pgcode} - {e.pgerror}")
        conn.rollback()
        raise ValueError(f"Integrity issue occurred: {e.pgcode}")

    except psycopg2.Error as e:
        logger.error(f"Database Error: {e.pgcode} - {e.pgerror}")
        conn.rollback()
        raise ValueError(f"Database issue occurred: {e.pgcode}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        conn.rollback()
        raise RuntimeError("An unexpected error occurred")
    
    finally:
        cursor.close()
        conn.close()