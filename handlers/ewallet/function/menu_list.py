from bot import database
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import sys
from utils.transaction import *
from models.intents import *
from ..variable import *

sys.path.append('...')
logger = logging.getLogger(__name__)


async def mainmenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button1 = KeyboardButton('Nạp tiền 🤑')
    button2 = KeyboardButton('Cập nhật số dư 💳')
    button3 = KeyboardButton('Chuyển tiền 📤')
    button4 = KeyboardButton('Lịch sử giao dịch 📊')
    button1 = KeyboardButton('Nạp tiền')
    button2 = KeyboardButton('Cập nhật số dư')
    button3 = KeyboardButton('Chuyển tiền')
    button4 = KeyboardButton('Lịch sử giao dịch')
    reply_keyboard = [[button1], [button2], [button3], [button4]]

    await update.message.reply_text(
        "Chao mung den vi dien tu cua Nam Le. Nhap lua chon cua ban: ",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=False, one_time_keyboard=True
        ),
    )
    return user_choice


async def select_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    if text in naptien:
        await update.message.reply_text("Nhập số tiền muốn nạp: ")
        return put_money
    elif text in capnhat:
        result = database.query_balance_data(context.user_data["username"])
        balance = result[3]
        await update.message.reply_text(f"So du tai khoan cua ban hien tai la: {balance}")
        return user_choice
    elif text in chuyentien:
        await update.message.reply_text("Nhap tài khoản muốn chuyển khoản: ")

        return confirmsend
    elif text in lichsugiaodich:
        user_database = dtb1(str(context.user_data["username"]))
        results = user_database.query_data()
        await update.message.reply_text("Lich su giao dich la: ")
        for result in results:
            await update.message.reply_text(result[1])
        return user_choice
    elif text == 'Cài đặt ⚙️':
        button1 = KeyboardButton('Đổi mật khẩu')
        button2 = KeyboardButton('Đăng xuất')
        button3 = KeyboardButton('Quay lại')
        reply_keyboard = [[button1], [button3], [button2]]
        await update.message.reply_text('Thực hiện cài đặt tài khoản. Nhập lựa chọn: ', reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=False, one_time_keyboard=True))
        return setting
    else:
        await update.message.reply_text("Da huy")
        return ConversationHandler.END
