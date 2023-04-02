import random
import string

from passlib.hash import bcrypt
from bot import database
from utils.transaction import *
from telegram.ext import *
from telegram import *
import os
import sys
import logging
import tracemalloc

from .variable import *
sys.path.append('...')

logger = logging.getLogger(__name__)


# async def password_regis(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = update.message.from_user
#     context.user_data["username"] = str(update.message.text)
#     logger.info("Username of %s: %s", user.first_name, update.message.text)
#     results = database.query_data()
#     a = int(0)
#     for result in results:
#         print(result[1])
#         if context.user_data["username"] == result[1]:
#             a = a+1
#     if a > 0:
#         await update.message.reply_text("Tên người dùng đã được sử dụng. Hãy thử tên khác.")
#         return password_register
#     else:
#         print(">>> check a: ", a)
#         await update.message.reply_text("Password to register: ")
#     return success


async def sucess_def(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    context.user_data["username"] = str(update.message.from_user.id)
    password = str(update.message.text)

    random_string = ''.join(random.choices(
        string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32))
    password_hash = (random_string + password +
                     random_string)
    password = bcrypt.hash(password_hash)
    context.user_data["password"] = str(password)
    logger.info("Password of %s: %s", user.first_name, update.message.text)
    results = database.query_data()
    array = []
    for result in results:
        array.append(result[1])
    if context.user_data["username"] in array:
        await update.message.reply_text("Tài khoản đã được đăng ký. Vui lòng thực hiện lại lựa chọn của bạn: ")
        return choice
    else:
        database.insert_user(context.user_data["username"],
                             context.user_data["password"],
                             random_string)
    user_database = dtb1(str(context.user_data["username"]))
    user_database.create_table()
    await update.message.reply_text("Dang ky thanh cong! Nhap lua chon ")
    return choice
