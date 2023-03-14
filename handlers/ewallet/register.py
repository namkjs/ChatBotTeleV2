

from bot import database
from telegram.ext import *
from telegram import *
import os
import sys
import logging
import tracemalloc

from .variable import *
sys.path.append('...')

logger = logging.getLogger(__name__)


async def password_regis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    context.user_data["username"] = str(update.message.text)
    logger.info("Username of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Password to register: ")
    return success


async def sucess_def(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    context.user_data["password"] = str(update.message.text)
    logger.info("Password of %s: %s", user.first_name, update.message.text)
    print("Check", context.user_data["username"],
          context.user_data["password"])
    database.insert_user(context.user_data["username"],
                         context.user_data["password"])
    await update.message.reply_text("Dang ky thanh cong! Nhap username de dang nhap: ")
    return password_signin
