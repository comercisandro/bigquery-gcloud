import os
import time
from google.cloud import storage
from google.oauth2 import service_account

FOLDER_TO_UPLOAD = "/home/sandro/Documentos/beca/experimentos/upload_files_to_bucket/data_out"
TIME_BETWEEN_FILES = 5
BUCKET_NAME = "raw-le-bluetooth-csvs"

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    credentials = service_account.Credentials.from_service_account_file('/home/sandro/Documentos/beca/experimentos/upload_files_to_bucket/Contactar-1243667c60e8.json')
    project_id = 'perfect-analog-288119'
    client = storage.Client(credentials=credentials, project=project_id)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    return blob.public_url

files = sorted(os.listdir(FOLDER_TO_UPLOAD))

for file in files:

        print("uploading" , file, "...")

        url = upload_to_bucket(file, FOLDER_TO_UPLOAD + "/" + file, BUCKET_NAME)

        print("file uploaded:", url)

        time.sleep(TIME_BETWEEN_FILES)

print("FIN de carga de archivos")