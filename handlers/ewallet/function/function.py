from utils.database import database
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import sys
import datetime
from ..variable import *
from utils.transaction import *
from models.Keyboard import *
import glob
import cv2
import pandas as pd
import pathlib
import os
from telegram.constants import ParseMode

sys.path.append('...')
logger = logging.getLogger(__name__)

user_money = int()
receiver_money = int()
value = str()
receiver = str()
menu_keyboard = InlineKeyboardMarkup(inline_keyboard_menu())


async def set_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if (update.callback_query.data == 'Đổi mật khẩu'):
        await query.edit_message_text('Nhập mật khẩu mới: ')
        return changepassword
    elif (update.callback_query.data == 'Đăng xuất'):
        await query.edit_message_text("Đăng xuất thành công. Chúc bạn một ngày vui vẻ")
        return ConversationHandler.END
    elif (update.callback_query.data == 'Xem số tài khoản'):
        results = database.query_balance_data(context.user_data["username"])
        balance = results[3]
        score_gif = results[5]

        await query.edit_message_text(f"Số tài khoản của bạn là:{context.user_data['username']}\n<b>💰 Ví của bạn</b>\n<b>Số dư</b>: {balance} VND\n<b>Điểm thành viên:</b> {score_gif} ", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice
    elif (update.callback_query.data == 'Đổi ngôn ngữ'):
        language1 = 'Tiếng Việt'
        language2 = 'English'
        keyboard = [[language1], [language2]]
        await query.edit_message_text("Lựa chọn ngôn ngữ muốn đổi", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, selective=True))
        return change_language
    elif (update.callback_query.data == 'Quay lại'):
        results = database.query_balance_data(context.user_data["username"])
        balance = results[3]
        score_gif = results[5]
        await query.edit_message_text(f"<b>💰 Ví của bạn</b>\n<b>Số tài khoản:</b> {context.user_data['username']}\n<b>Số dư:</b> {balance} VND\n<b>Điểm thành viên: </b>{score_gif} ", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice
    elif (update.callback_query.data == 'Mã QR'):
        await query.edit_message_text("Mã QR của bạn là: ")
        photo_file = f'public/images/qr/{context.user_data["username"]}.png'
        await query.message.reply_photo(photo_file)
        return user_choice
    elif (update.callback_query.data == 'Test QR'):
        await query.edit_message_text("Test QR: ")
        return qrcode


def read_qr_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # nparr = np.frombuffer(filename, np.uint8)
    # convert to image array
    img = cv2.imread(f'user_photo.jpg')

    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)
    return value


async def qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("user_photo.jpg")
    value = str(read_qr_code(update, context))
    await update.message.reply_text(value)
    os.remove("user_photo.jpg")
    # await update.message.reply_photo(image)
    return user_choice


async def change_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = database.query_data()

    for result in result:
        if (context.user_data["username"] == result[1]):
            password = bcrypt.hash(result[4] + text +
                                   result[4])
            break
    database.update_pass(context.user_data['username'], password)
    await update.message.reply_text("Đổi mật khẩu thành công.", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
    return user_choice


async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    results = database.query_balance_data(context.user_data["username"])
    balance = results[3]
    score_gif = results[5]
    if (text == 'Thẻ điện thoại'):
        await update.message.reply_text(f"Bla bla \n<b>💰 Ví của bạn</b>\n<b>Số tài khoản:</b>{context.user_data['username']}\n<b>Số dư: </b>{balance} VND\nĐ<b>iểm thành viên:</b> {score_gif}", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice
    elif (text == 'Mã giảm giá Coffee'):
        await update.message.reply_text(f"Abc\n<b>💰 Ví của bạn</b>\n<b>Số tài khoản:</b>{context.user_data['username']}\n<b>Số dư: </b>{balance} VND\nĐ<b>iểm thành viên:</b> {score_gif}", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice
    elif (text == 'Mã giảm giá Massage'):
        await update.message.reply_text(f"Bú\n<b>💰 Ví của bạn</b>\n<b>Số tài khoản:</b>{context.user_data['username']}\n<b>Số dư: </b>{balance} VND\nĐ<b>iểm thành viên:</b> {score_gif}", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice
    elif (text == 'Quay lại'):
        # create KeyboardButton objects for each line
        await update.message.reply_text(f"\n<b>💰 Ví của bạn</b>\n<b>Số tài khoản:</b>{context.user_data['username']}\n<b>Số dư: </b>{balance} VND\nĐ<b>iểm thành viên:</b> {score_gif}", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML
                                        )
        return user_choice


async def changelan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if (text == 'Tiếng Việt'):
        await update.message.reply_text("Đổi ngôn ngữ thành công! ", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice
    elif (text == 'English'):
        await update.message.reply_text('Success', reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice
