import os
import streamlit as st
from utils.config import Config

from azure.storage.blob import BlobServiceClient

def upload_to_blob_storage(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)

        blob_service_client = blob_service_client.get_blob_client(container=Config.CONTAINER, blob=file_name)

        blob_service_client.upload_blob(file, overwrite=True)

        return blob_service_client.url
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {e}")
        return None