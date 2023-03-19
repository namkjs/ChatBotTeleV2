from utils.database import database
from telegram.ext import *
from telegram import *
import logging
import tracemalloc
import sys

from ..variable import *
sys.path.append('...')
logger = logging.getLogger(__name__)


async def putmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    context.user_data["money"] = update.message.text
    result = database.query_data()
    balance = int()
    for result in result:
        balance = int(result[3])
    print(balance)
    database.update_data(
        context.user_data["username"], context.user_data["money"], balance)
    await update.message.reply_text("Nap tien thanh cong")
    return main_menu


async def updatemoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = database.query_balance_data(context.user_data["username"])
    balance = result[3]
    await update.message.reply_text(f"So du tai khoan cua ban hien tai la: {balance}")
    return main_menu

user_money = int()
receiver_money = int()
value = str()
receiver = str()


async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global receiver
    receiver = update.message.text
    results = database.query_data()
    a = int(0)
    for result in results:
        if receiver == result[1]:
            a = a+1
            break
    if a > 0:
        await update.message.reply_text("Nhap so tien can chuyen: ")
        return send_money
    else:
        await update.message.reply_text("Ten nguoi dung khong hop le! Vui long nhap lai ten dang nhap: ")
        return confirmsend


async def sendmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = database.query_balance_data(context.user_data["username"])
    balance = result[3]
    money = int(update.message.text)
    global receiver
    database.send(context.user_data["username"], receiver,
                  receiver_money, balance, money)
    await update.message.reply_text("Chuyen tien thanh cong")
    return main_menu
