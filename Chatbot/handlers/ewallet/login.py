from passlib.hash import bcrypt
from bot import database
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import sys

from .variable import *
sys.path.append('...')
logger = logging.getLogger(__name__)


async def usern(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    # await update.message.reply_text("Username:")
    user = update.message.from_user
    logger.info("Selection %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Username:")
    return password_signin


async def password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    # await update.message.reply_text("Username:")
    context.user_data['username'] = update.message.text
    user = update.message.from_user
    user_login = update.message.text
    logger.info("Username of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Password:")
    return success_login


async def success_log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    # await update.message.reply_text("Username:")
    context.user_data['password'] = update.message.text
    user = update.message.from_user
    logger.info("Password of %s: %s", user.first_name, update.message.text)
    result = database.query_data()
    a = int(0)
    for result in result:
        if (context.user_data["username"] == result[1] and bcrypt.verify(context.user_data["password"], result[2])):
            a = a+1
            break
    if (a == 1):
        await update.message.reply_text("Dang nhap thanh cong!")
        return main_menu
    else:
        await update.message.reply_text("Sai mat khau! Vui long nhap lai username hoac thuc hien dang ky. Lua chon:")
        return choice
