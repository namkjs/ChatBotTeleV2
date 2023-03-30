
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import os
from dotenv import load_dotenv
import requests
from flask import Flask
# import file
import handlers.ConversationHandler as handlers
from utils.database import *
database = dtb()
PORT = int(os.environ.get('PORT', '3306'))
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
    application = Application.builder().token(
        '6040924293:AAEW1ot_lAxltrZ8-F0WDnKHkDMPwlYuie').build()

    application.add_handler(handlers.ewallet())

    application.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path='6040924293:AAEW1ot_lAxltrZ8-F0WDnKHkDMPwlYuie',
        webhook_url='https://telegrambot123.herokuapp.com/6040924293:AAEW1ot_lAxltrZ8-F0WDnKHkDMPwlYuie'
    )


if __name__ == "__main__":
    main()
