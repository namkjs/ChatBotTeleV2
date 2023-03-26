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


async def success_log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    # await update.message.reply_text("Username:")
    user = update.message.from_user
    context.user_data['password'] = update.message.text

    context.user_data['username'] = str(update.message.from_user.id)
    logger.info("Password of %s: %s", user.first_name, update.message.text)
    result = database.query_data()
    a = int(0)
    for result in result:
        if (context.user_data["username"] == result[1] and bcrypt.verify(str(result[4] + context.user_data["password"]+result[4]), result[2])):
            a = a+1
            break
    if (a == 1):
        button1 = KeyboardButton('Nạp tiền '+u'🤑')
        button2 = KeyboardButton('Cập nhật số dư ' + u'💳')
        button3 = KeyboardButton('Chuyển tiền ' + u'📤')
        button4 = KeyboardButton('Lịch sử giao dịch ' + u'📊')

# create KeyboardButton objects for each line

        reply_keyboard = [[button1], [button2], [button3], [button4]]
        await update.message.reply_text("Dang nhap thanh cong!"
                                        "Chao mung den vi dien tu cua Nam Le. Nhap lua chon cua ban: ",
                                        reply_markup=ReplyKeyboardMarkup(
                                            reply_keyboard, resize_keyboard=True, one_time_keyboard=True
                                        ),
                                        )
        return user_choice
    else:
        await update.message.reply_text("Sai mat khau! Vui long nhap lai username hoac thuc hien dang ky. Lua chon:")
        return choice
