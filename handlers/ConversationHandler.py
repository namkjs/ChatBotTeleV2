from telegram.ext import *
import logging
import tracemalloc
from .ewallet.menu import *
from .ewallet.cancel import *
from .ewallet.login import *
from .ewallet.register import *
from .ewallet.function.menu_list import *
from .ewallet.function.function import *


def ewallet():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("ewallet", start)],
        states={
            choice: [CallbackQueryHandler(register_or_login)],
            refcode: [MessageHandler(filters.TEXT & ~filters.COMMAND, ref_code)],
            # username_signin: [MessageHandler(filters.TEXT, usern)],
            # password_signin: [MessageHandler(filters.TEXT, password)],
            success_login: [MessageHandler(filters.TEXT & ~filters.COMMAND, success_log), CommandHandler("skip", skip)],
            # password_register: [MessageHandler(filters.TEXT, password_regis)],
            success: [MessageHandler(filters.TEXT & ~filters.COMMAND, sucess_def), CommandHandler("skip", skip)],
            main_menu: [MessageHandler(filters.TEXT & ~filters.COMMAND, mainmenu)],
            user_choice: [MessageHandler(filters.TEXT & ~filters.COMMAND, select_function)],
            Approach: [MessageHandler(filters.TEXT & ~filters.COMMAND, approach)],
            confirmsend_photo: [MessageHandler(filters.PHOTO & ~filters.COMMAND, confirm_photo)],
            put_money: [MessageHandler(filters.TEXT & ~filters.COMMAND, putmoney)],
            # update_money: [MessageHandler(filters.TEXT, updatemoney)],
            confirmsend: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm)],
            send_money: [MessageHandler(filters.TEXT & ~filters.COMMAND, sendmoney)],
            # transaction: [MessageHandler(filters.TEXT, trans)],
            setting: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_up)],
            changepassword: [MessageHandler(filters.TEXT & ~filters.COMMAND, change_password)],
            score: [MessageHandler(filters.TEXT & ~ filters.COMMAND, gift)],
            change_language: [MessageHandler(filters.TEXT & ~ filters.COMMAND, changelan)],
            qrcode: [MessageHandler(filters.PHOTO, qr)],
        },
        fallbacks=[CommandHandler("Cancel", cancel)],
    )
    return conv_handler
