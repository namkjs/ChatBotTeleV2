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
sys.path.append('...')
logger = logging.getLogger(__name__)

user_money = int()
receiver_money = int()
value = str()
receiver = str()


async def putmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    money = str(update.message.text)
    if money.isnumeric() == False:
        await update.message.reply_text("Số tiền không hợp lệ vui lòng nhập lại số tiền: ")
        return put_money
    else:
        money = int(update.message.text)
        if money < 0:
            await update.message.reply_text("Số tiền không hợp lệ vui lòng nhập lại số tiền: ")
            return put_money
        else:
            context.user_data["money"] = update.message.text
            result = database.query_balance_data(context.user_data["username"])
            balance = int(result[3])
            database.update_data(
                context.user_data["username"], context.user_data["money"], balance)
            await update.message.reply_text("Nạp tiền thành công", reply_markup=ReplyKeyboardMarkup(
                                            menu_keyboard(), resize_keyboard=True,  selective=True
                                            ),)
            return user_choice


async def updatemoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = database.query_balance_data(context.user_data["username"])
    balance = result[3]
    await update.message.reply_text(f"Số dư tài khoản hiện tại của bạn là: {balance}", reply_markup=ReplyKeyboardMarkup(
        menu_keyboard(), resize_keyboard=True,  selective=True
    ),)
    return user_choice


async def approach(update: Update, context: ContextTypes.DEFAULT_TYPE):
    temp = update.message.text
    if temp == 'Số tài khoản':
        await update.message.reply_text("Nhập số tài khoản muốn chuyển")
        return confirmsend
    elif temp == 'Mã QR':
        await update.message.reply_text("Nhập mã QR: ")
        return confirmsend_photo


async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global receiver
    receiver = update.message.text
    results = database.query_data()
    button1 = KeyboardButton('10000')
    button2 = KeyboardButton('20000')
    button3 = KeyboardButton('50000')
    button4 = KeyboardButton('100000')
    button5 = KeyboardButton('200000')
    button6 = KeyboardButton('500000')
    reply_keyboard = [[button1, button2], [
        button3, button4], [button5, button6]]
    a = int(0)
    for result in results:
        if receiver == result[1]:
            global receiver_money
            receiver_money = result[3]
            a = a+1
            break
    if a > 0:
        await update.message.reply_text("Nhập số tiền muốn chuyển: ",
                                        reply_markup=ReplyKeyboardMarkup(
                                            reply_keyboard, resize_keyboard=True,  selective=True
                                        ),
                                        )
        return send_money
    else:
        await update.message.reply_text("Tên người dùng không hợp lệ. Vui lòng thực hiện lại", reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True
        ),)
        return user_choice


async def confirm_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global receiver
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("user_photo.jpg")
    receiver = str(read_qr_code(update, context))
    os.remove("user_photo.jpg")

    results = database.query_data()
    button1 = KeyboardButton('10000')
    button2 = KeyboardButton('20000')
    button3 = KeyboardButton('50000')
    button4 = KeyboardButton('100000')
    button5 = KeyboardButton('200000')
    button6 = KeyboardButton('500000')
    reply_keyboard = [[button1, button2], [
        button3, button4], [button5, button6]]
    a = int(0)
    for result in results:
        if receiver == result[1]:
            global receiver_money
            receiver_money = result[3]
            a = a+1
            break

    if a > 0:
        await update.message.reply_text("Nhập số tiền muốn chuyển: ",
                                        reply_markup=ReplyKeyboardMarkup(
                                            reply_keyboard, resize_keyboard=True,  selective=True
                                        ),
                                        )
        return send_money
    else:
        await update.message.reply_text("Tên người dùng không hợp lệ. Vui lòng thực hiện lại", reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True
        ),)
        return user_choice


async def sendmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = database.query_balance_data(context.user_data["username"])
    balance = result[3]
    money = str(update.message.text)
    if money.isnumeric() == False:
        await update.message.reply_text("Số tiền không hợp lệ. Vui lòng nhập lại số tiền: ")
        return confirmsend
    else:
        money = int(update.message.text)
    if money < 0:
        await update.message.reply_text("Số tiền không hợp lệ. Vui lòng nhập lại số tiền: ")
        return confirmsend
    elif money > balance:
        await update.message.reply_text("Số dư trong tài khoản không khả dụng! Vui lòng nạp thêm tiền và thực hiện lại: ", reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True
        ),)
        return confirmsend
    else:
        global receiver
        database.send(context.user_data["username"], receiver,
                      receiver_money, balance, money)
        # trans = str(str(current_time) + ": " + str(-money))
        # trans_receive = str(str(current_time) + ": +" + str(money))
        day = datetime.datetime.today().strftime('%d-%m-%Y')
        time = datetime.datetime.today().strftime('%H:%M:%S')
        fr = context.user_data["username"]
        print(">>> check trans: ", trans)
        user_database = dtb1(str(context.user_data["username"]))
        user_database.insert_user(day, time, -money, receiver)

        user_database1 = dtb1(receiver)
        user_database1.insert_user(day, time, money, fr)
        button1 = KeyboardButton(
            'Nạp tiền ' + u'🤑')
        button2 = KeyboardButton('Cập nhật số dư ' + u'💳')
        button3 = KeyboardButton('Chuyển tiền ' + u'📤')
        button4 = KeyboardButton('Lịch sử giao dịch ' + u'📊')
        button5 = KeyboardButton('Cài đặt ⚙️')
# create KeyboardButton objects for each line

        reply_keyboard = [[button1], [button2],
                          [button3], [button4], [button5]]
        await update.message.reply_text("Chuyển tiền thành công!",
                                        reply_markup=ReplyKeyboardMarkup(
                                            menu_keyboard(), resize_keyboard=True,  selective=True
                                        ),
                                        )
        return user_choice


async def trans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_database = dtb1(str(context.user_data["username"]))
    results = user_database.query_data()
    await update.message.reply_text("Lich su giao dich la: ")
    await update.message.reply_text("           Ngày          |             Giờ            |          Tiền         ")
    for result in results:
        await update.message.reply_text(f'      {result[1]}     |       {result[2]}         {result[3]}')
    return user_choice


async def set_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    button1 = KeyboardButton(
        'Nạp tiền ' + u'🤑')
    button2 = KeyboardButton('Cập nhật số dư ' + u'💳')
    button3 = KeyboardButton('Chuyển tiền ' + u'📤')
    button4 = KeyboardButton('Lịch sử giao dịch ' + u'📊')
    button5 = KeyboardButton('Cài đặt ⚙️')
    reply_keyboard = [[button1], [button2],
                      [button3], [button4], [button5]]
    if (text == 'Đổi mật khẩu'):
        await update.message.reply_text('Nhập mật khẩu mới: ')
        return changepassword
    elif (text == 'Đăng xuất'):
        await update.message.reply_text("Đăng xuất thành công. Chúc bạn một ngày vui vẻ")
        return ConversationHandler.END
    elif (text == 'Xem số tài khoản | Mã giới thiệu'):
        await update.message.reply_text(f"Số tài khoản | Mã giới thiệu của bạn là: {context.user_data['username']}", reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, selective=True
        ),)
        return user_choice
    elif (text == 'Đổi ngôn ngữ'):
        language1 = 'Tiếng Việt'
        language2 = 'English'
        keyboard = [[language1], [language2]]
        await update.message.reply_text("Lựa chọn ngôn ngữ muốn đổi", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, selective=True))
        return change_language
    elif (text == 'Quay lại'):
        await update.message.reply_text('Menu: ', reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True, selective=True
        ),
        )
        return user_choice
    elif (text == 'Mã QR'):
        await update.message.reply_text("Mã QR của bạn là: ")
        photo_file = f'public/images/qr/{context.user_data["username"]}.png'
        await update.message.reply_photo(photo_file)
        return user_choice
    elif (text == 'Test QR'):
        await update.message.reply_text("Test QR: ")
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
    await update.message.reply_text("Đổi mật khẩu thành công.", reply_markup=ReplyKeyboardMarkup(
        menu_keyboard(), resize_keyboard=True,  selective=True
    ),)
    return user_choice


async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if (text == 'Thẻ điện thoại'):
        await update.message.reply_text('Bla bla', reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True))
        return user_choice
    elif (text == 'Mã giảm giá Coffee'):
        await update.message.reply_text("Abc", reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True))
        return user_choice
    elif (text == 'Mã giảm giá Massage'):
        await update.message.reply_text("Bú", reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True))
        return user_choice
    elif (text == 'Quay lại'):
        # create KeyboardButton objects for each line
        await update.message.reply_text('Menu: ', reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True
        ),
        )
        return user_choice


async def changelan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if (text == 'Tiếng Việt'):
        await update.message.reply_text("Đổi ngôn ngữ thành công! ", reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True))
        return user_choice
    elif (text == 'English'):
        await update.message.reply_text('Success', reply_markup=ReplyKeyboardMarkup(
            menu_keyboard(), resize_keyboard=True,  selective=True))
        return user_choice
