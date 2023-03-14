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


# async def updatemoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     mycursor = mydb.cursor()

#     sql = "SELECT tien FROM user2 WHERE username = %s"
#     val = (context.user_data["username"],)

#     # val = val.split()
#     mycursor.execute(sql, val)

#     myresult = mycursor.fetchone()
#     print(myresult)
#     # myresult = int(myresult[0])
#     await update.message.reply_text(f"So du tai khoan cua ban hien tai la: {myresult[0]}")
#     return main_menu

# user_money = int()
# receiver_money = int()
# value = str()


# async def sendmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     mycursor = mydb.cursor()

#     sql = "SELECT tien FROM user2 WHERE username = %s"
#     val = (context.user_data["username"],)

#     # val = val.split()
#     mycursor.execute(sql, val)

#     myresult = mycursor.fetchone()
#     global user_money
#     user_money = int(myresult[0])

#     print(myresult[0])
#     context.user_data["receiver"] = str(update.message.text,)
#     val = (context.user_data["receiver"],)
#     mycursor.execute(sql, val)
#     myresult = mycursor.fetchone()
#     global receiver_money
#     receiver_money = int(myresult[0])
#     print(">>> checking money user", user_money,
#           ">> checking receiver money", receiver_money)
#     await update.message.reply_text("Nhap so tien can chuyen: ")

#     # myresult = int(myresult[0])
#     return confirmsend


# async def confirm_sendmoney(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     money = int(update.message.text)
#     global user_money
#     global receiver_money
#     print(">>> checking money send", money,
#           "\n>>>> checking money of user", user_money)
#     user_money = user_money - money
#     receiver_money = receiver_money + money
#     receiver_money = int(receiver_money)
#     print(">>> check receiver_money", receiver_money,
#           ">>> user_money", user_money)
#     mycursor = mydb.cursor()
#     sql = "UPDATE user2 SET tien = %s WHERE username = %s"
#     val = (user_money,
#            str(context.user_data["username"]))

#     mycursor.execute(sql, val)
#     mydb.commit()
#     mycursor = mydb.cursor()
#     global value
#     print("<<<", receiver_money)
#     value = context.user_data["receiver"]
#     val = (receiver_money, str(value))
#     mycursor.execute(sql, val)
#     mydb.commit()
#     await update.message.reply_text("Chuyen tien thanh cong!")
#     return main_menu
