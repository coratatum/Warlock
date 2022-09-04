import google.cloud.logging as glog
import logging


def setup_gcp_logging(project_id, logger_name):
    client = glog.Client(project=project_id)
    client.setup_logging()
    # cloud_handler = glog.handlers.CloudLoggingHandler(client)
    logging.basicConfig(filename='./logging/discord.log', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(logger_name)
    # logger.addHandler(cloud_handler)