from bot import database
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import sys

from ..variable import *
sys.path.append('...')
logger = logging.getLogger(__name__)


async def mainmenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button1 = KeyboardButton('Nạp tiền')
    button2 = KeyboardButton('Cập nhật số dư')
    button3 = KeyboardButton('Chuyển tiền')
    reply_keyboard = [[button1, button2, button3]]

    await update.message.reply_text(
        "Chao mung den vi dien tu cua Nam Le. Nhap lua chon cua ban: ",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, one_time_keyboard=True
        ),
    )
    return user_choice


async def select_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    if text == "Nạp tiền":
        await update.message.reply_text("Nhập số tiền muốn nạp")
        return put_money
    elif text == "Cập nhật số dư":
        # await update.message.reply_text("So du tai khoan: ")
        return update_money
    elif text == "Chuyển tiền":
        await update.message.reply_text("Nhap username muon chuyen khoan: ")
        return confirmsend
    else:
        await update.message.reply_text("Da huy")
        return ConversationHandler.END
