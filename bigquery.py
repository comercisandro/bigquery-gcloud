from enum import Flag
from google.cloud import bigquery
from google.oauth2 import service_account
from numpy import fabs
import pandas as pd

## El path corresponde al archivo JSON de la llave de la cuenta de servicio de GCP
credentials = service_account.Credentials.from_service_account_file('/home/sandro/Documentos/beca/experimentos/perfect-analog-288119-77613757dc4a.json')

project_id = 'perfect-analog-288119'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query(
  """
   SELECT *
   FROM `perfect-analog-288119.contactar.experiments-le_bluetooth` 
   
  """)

results = query_job.to_dataframe()
results.head()

results.to_csv('datosBQ-8-8.csv')