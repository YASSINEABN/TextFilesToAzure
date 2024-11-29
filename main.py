from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

connection_string = BlobEndpoinp
container_name = "store"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client(container_name)

local_file_path = "test.txt"

file_name = os.path.basename(local_file_path)

blob_client = container_client.get_blob_client(file_name)

with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"File {file_name} uploaded successfully to the container {container_name}")
