import logging
from os import environ
from dotenv import load_dotenv

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv(".env")
logger = logging.getLogger(__name__)

SLACK_BOT_TOKEN = environ["SLACK_BOT_TOKEN"]
channel_id = environ["CHANNEL_ID"]

client = WebClient(token=SLACK_BOT_TOKEN)

try:
    result = client.chat_postMessage(channel=channel_id, text="Hello world")
    logger.info(result)
except SlackApiError as e:
    logger.error(f"Error posting message: {e}")
