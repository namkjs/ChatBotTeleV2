from utils.database import database
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import sys
from datetime import datetime
from ..variable import *
from utils.transaction import *
sys.path.append('...')
logger = logging.getLogger(__name__)


async def putmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
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
        await update.message.reply_text("Nap tien thanh cong")
        return user_choice


async def updatemoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = database.query_balance_data(context.user_data["username"])
    balance = result[3]
    await update.message.reply_text(f"So du tai khoan cua ban hien tai la: {balance}")
    return user_choice

user_money = int()
receiver_money = int()
value = str()
receiver = str()


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
                                            reply_keyboard, resize_keyboard=True, one_time_keyboard=True, selective=True
                                        ),
                                        )
        return send_money
    else:
        await update.message.reply_text("Ten nguoi dung khong hop le! Vui long nhap lai ten dang nhap: ")
        return confirmsend


async def sendmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = database.query_balance_data(context.user_data["username"])
    balance = result[3]
    money = int(update.message.text)
    if money < 0:
        await update.message.reply_text("Loi vui long thuc hien lai! ")
        return confirmsend
    elif money > balance:
        await update.message.reply_text("So du khong kha dung")
        return confirmsend
    else:
        global receiver
        database.send(context.user_data["username"], receiver,
                      receiver_money, balance, money)
        current_time = datetime.now()
        trans = str(str(current_time) + ": " + str(-money))
        trans_receive = str(str(current_time) + ": +" + str(money))
        print(">>> check trans: ", trans)
        user_database = dtb1(str(context.user_data["username"]))
        user_database.insert_user(trans)

        user_database1 = dtb1(receiver)
        user_database1.insert_user(trans_receive)
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
                                            reply_keyboard, resize_keyboard=True, one_time_keyboard=True, selective=True
                                        ),
                                        )
        return user_choice


async def trans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_database = dtb1(str(context.user_data["username"]))
    results = user_database.query_data()
    await update.message.reply_text("Lich su giao dich la: ")
    for result in results:
        await update.message.reply_text(result[1])
    return user_choice

# async def hist(update: Update, context: ContextTypes.DEFAULT_TYPE):


async def set_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if (text == 'Đổi mật khẩu'):
        await update.message.reply_text('Nhập mật khẩu mới: ')
        return changepassword
    if (text == 'Đăng xuất'):
        await update.message.reply_text("Đăng xuất thành công. Chúc bạn một ngày vui vẻ")
        return ConversationHandler.END
    if (text == 'Quay lại'):
        button1 = KeyboardButton(
            'Nạp tiền ' + u'🤑')
        button2 = KeyboardButton('Cập nhật số dư ' + u'💳')
        button3 = KeyboardButton('Chuyển tiền ' + u'📤')
        button4 = KeyboardButton('Lịch sử giao dịch ' + u'📊')
        button5 = KeyboardButton('Cài đặt ⚙️')
# create KeyboardButton objects for each line

        reply_keyboard = [[button1], [button2],
                          [button3], [button4], [button5]]
        await update.message.reply_text('Menu: ', reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, one_time_keyboard=True, selective=True
        ),
        )
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
    await update.message.reply_text("Đổi mật khẩu thành công.")
    return user_choice
