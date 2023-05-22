import random
import string
import qrcode
from passlib.hash import bcrypt
from bot import database
from utils.transaction import *
from telegram.ext import *
from telegram import *
import os
import sys
import logging
import tracemalloc

from ..variable import *
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

async def ref_code_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/skip' or update.message.text == '/Skip':
        context.user_data['code'] == 0
        await update.message.reply_text("Nhập mật khẩu: ")
        return success_login_en
    else:
        context.user_data['code'] = str(update.message.text)
        await update.message.reply_text("Mật khẩu: ")
        return success_login_en


async def sucess_def_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        return choice_en
    else:
        database.insert_user(context.user_data["username"],
                             context.user_data["password"],
                             random_string)
    user_database = dtb1(str(context.user_data["username"]))
    user_database.create_table()
    await update.message.reply_text("Đăng ký thành công. Nhập lựa chọn: ")

    data = str(context.user_data["username"])

    img = qrcode.make(data)

    img.save(f'public/images/qr/{context.user_data["username"]}.png')
    return choice_en
