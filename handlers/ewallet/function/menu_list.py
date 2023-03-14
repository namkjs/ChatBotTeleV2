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
    await update.message.reply_text("Chao mung den vi dien tu cua Nam Le. Nhap lua chon cua ban: ")
    return user_choice


async def select_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    if text == "Nap tien":
        await update.message.reply_text("Nhap so tien muon nap: ")
        return put_money
    elif text == "Cap nhat so du":
        await update.message.reply_text("So du tai khoan: ", end='')
        return update_money
    elif text == "Chuyen tien":
        await update.message.reply_text("Nhap username muon chuyen khoan: ")
        return send_money
    else:
        await update.message.reply_text("Da huy")
        return ConversationHandler.END
