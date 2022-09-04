import google.cloud.logging
import logging

# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.setup_logging()
logging.basicConfig(filename='./logging/discord.log', encoding='utf-8', filemode='w', level=logging.INFO)