from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv
import os 
import pandas as pd 

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
_CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
_PROJECT_ID = os.getenv('GCP_PROJECT_ID')


def running_query(client):
    QUERY = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    for row in rows:
        print(row.name)

def saving_queries_as_pandas_df(client):
    QUERY = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
    query_job = client.query(QUERY)
    result_df = query_job.to_dataframe() 
    return result_df.head() 


if __name__ == "__main__":

    client = bigquery.Client(
        project=_PROJECT_ID,
        credentials=_CREDENTIALS
        )

    print(running_query(client))
    print(saving_queries_as_pandas_df(client))


    


