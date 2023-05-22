from bot import database
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import sys
from utils.transaction import *
from models.intents import *
from ..variable import *
from models.Keyboard import *
from telegram.constants import ParseMode
import prettytable as pt

sys.path.append('...')
logger = logging.getLogger(__name__)


async def mainmenu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Chao mung den vi dien tu cua Nam Le. Nhap lua chon cua ban: ",
        reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=False, one_time_keyboard=True
        ),
    )
    return user_choice


async def select_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if update.callback_query.data == 'Nạp tiền':
        await query.edit_message_text("Nhập số tiền muốn nạp: ")
        return put_money
    # elif update.callback_query.data in capnhat:
    #     result = database.query_balance_data(context.user_data["username"])
    #     balance = result[3]
    #     await update.message.reply_text(f"Số dư tài khoản của bạn là: {balance}")
    #     return user_choice
    elif update.callback_query.data in chuyentien:
        keyboard = [
            [
                InlineKeyboardButton(
                    "Số tài khoản", callback_data="Số tài khoản"),
                InlineKeyboardButton("Mã QR", callback_data="Mã QR"),
            ]
        ]
        approach_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Chọn hình thức nhập: ",  reply_markup=approach_markup)
        return Approach
    elif update.callback_query.data == "Rút tiền":
        await query.edit_message_text("Nhập số tiền muốn rút: ")
        return withdraw_money
    elif update.callback_query.data in lichsugiaodich:
        # user_database = dtb1(str(context.user_data["username"]))
        # results = user_database.query_data()
        # await query.message.reply_text("Lịch sử giao dịch: ")
        # await query.message.reply_text("           Ngày                |             Giờ            |          Tiền         ")
        # for result in results:
        #     await query.message.reply_text(f'      {result[1]}     |           {result[2]}     |        {result[3]}')
        menu_keyboard = InlineKeyboardMarkup(inline_keyboard_menu())
        # results = database.query_balance_data(context.user_data["username"])
        # balance = results[3]
        table = pt.PrettyTable(['Ngày', 'Giờ', 'Tiền'])
        table.align['Ngày'] = 'l'
        table.align['Giờ'] = 'l'
        table.align['Tiền'] = 'r'
        user_database = dtb1(str(context.user_data["username"]))
        results = user_database.query_data()
        await query.message.reply_text(text="<b>Lịch sử giao dịch là: </b>", parse_mode=ParseMode.HTML)
        for result in results:
            table.add_row([result[1], result[2], result[3]])
        await query.message.reply_text(
            text=f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)
        results = database.query_balance_data(context.user_data["username"])
        balance = results[3]
        await query.message.reply_text(f"💰 Ví của bạn\nSố tài khoản: {context.user_data['username']}\nSố dư: {balance} VND ",
                                       reply_markup=menu_keyboard)
        return user_choice
    elif update.callback_query.data == 'Đổi quà':
        button1 = KeyboardButton('Thẻ điện thoại')
        button4 = KeyboardButton('Mã giảm giá Coffee')
        button2 = KeyboardButton('Mã giảm giá Massage')
        button3 = KeyboardButton('Quay lại')
        menu_keyboard1 = [[button1], [button4], [button2], [button3]]
        results = database.query_balance_data(context.user_data["username"])
        await query.message.reply_text(f'Điểm thành viên của bạn là: {results[5]}. Thực hiện đổi điểm: ',  reply_markup=ReplyKeyboardMarkup(
            menu_keyboard1, resize_keyboard=False, one_time_keyboard=True))
        return score

    elif update.callback_query.data == 'Cài đặt':
        menu_setting = InlineKeyboardMarkup(keyboard_setting())
        await query.edit_message_text("Thực hiện cài đặt: ", reply_markup=menu_setting)
        return setting
    elif update.callback_query.data == 'Về chúng tôi':
        photo_file = 'public/images/2.png'
        await update.message.reply_photo(photo_file)
        await update.message.reply_text('A Potato là một bot ví điện tử xử của Telegram được phát triển và làm màu bởi nhóm 4 với CEO Đỗ Hiếu. Để hiểu rõ hơn về chúng tôi, các bạn có thể đọc link sau đây: https://a-potato.notion.site/Hi-u-l-ai-eacb5d50b7aa4fe4a14b7cf231265aa9')
        return user_choice
    else:
        await query.edit_message_text("Da huy")
        return ConversationHandler.END
