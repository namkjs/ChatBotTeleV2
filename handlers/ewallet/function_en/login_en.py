from passlib.hash import bcrypt
from bot import database
from telegram.ext import *
from telegram import *
from telegram.constants import ParseMode
import logging
import tracemalloc
import sys

from ..variable import *
from models.Keyboard import *
sys.path.append('...')
logger = logging.getLogger(__name__)


async def success_log_en(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    # await update.message.reply_text("Username:")
    user = update.message.from_user
    context.user_data['password'] = update.message.text

    context.user_data['username'] = str(update.message.from_user.id)
    logger.info("Password of %s: %s", user.first_name, update.message.text)
    result = database.query_data()
    a = int(0)
    results = database.query_balance_data(context.user_data["username"])
    balance = results[3]
    gift_score = results[5]
    for result in result:
        if (context.user_data["username"] == result[1] and bcrypt.verify(str(result[4] + context.user_data["password"]+result[4]), result[2])):
            a = a+1
            break
    if (a == 1):
        reply_markup = InlineKeyboardMarkup(inline_keyboard_menu())
        await update.message.reply_text(text=f"💰 <b>Ví của bạn</b>\n<b>Số tài khoản:</b> {context.user_data['username']}\n<b>Số dư:</b> {balance} VND\n<b>Điểm thành viên:</b> {gift_score} ",
                                        reply_markup=reply_markup, parse_mode=ParseMode.HTML)
        return user_choice_en
    else:
        await update.message.reply_text("Sai mat khau! Vui long nhap lai username hoac thuc hien dang ky. Lua chon:")
        return choice_en


async def skip_en(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    button1 = KeyboardButton('Đăng nhập')
    button2 = KeyboardButton('Đăng ký')
    button3 = KeyboardButton('Hủy')
    reply_keyboard = [[button1, button2, button3]]
    await update.message.reply_text(
        "Chương trình ví điện tử Appotato. Hãy thêm @Silun để thực hiện các chức năng hấp dẫn cùng Appotato.\n"
        "Thực hiện lựa chọn: ",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True
        ),
    )

    return choice_en
