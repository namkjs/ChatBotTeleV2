
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import os
from dotenv import load_dotenv
import requests
from flask import Flask
#import file
import handlers.ConversationHandler as handlers
from utils.database import *
database = dtb()

load_dotenv()
# Start recording information about memory usage
tracemalloc.start()

# Start recording status about prj
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run the bot."""
    application = Application.builder().token(os.getenv("API_TELE_KEY")).build()

    application.add_handler(handlers.ewallet())
    application.start_webhook(listen="0.0.0.0",
                              port=int(os.environ.get('PORT', 5000)),
                              url_path=os.getenv("API_TELE_KEY"),
                              webhook_url=+ os.getenv("API_TELE_KEY")
                              )


if __name__ == "__main__":
    main()
