from google.cloud import secretmanager

async def access_secret_version(project_id, secret_id, version_id):
    # Create a client
    client = secretmanager.SecretManagerServiceAsyncClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = await client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
