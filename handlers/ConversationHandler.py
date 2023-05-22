from telegram.ext import *
import logging
import tracemalloc
from .ewallet.menu import *
from .ewallet.cancel import *
from .ewallet.login import *
from .ewallet.register import *
from .ewallet.function.menu_list import *
from .ewallet.function.function import *
from .ewallet.function.putmoney import *
from .ewallet.function.sendmoney import *
from .ewallet.function.trans import *
from .ewallet.function_en.menu_list_en import *
from .ewallet.function_en.function_en import *
from .ewallet.function_en.putmoney_en import *
from .ewallet.function_en.sendmoney_en import *
from .ewallet.function_en.trans_en import *
from .ewallet.function_en.menu_en import *
from .ewallet.function_en.cancel_en import *
from .ewallet.function_en.login_en import *
from .ewallet.function_en.register_en import *


def ewallet():
    # usn = Update.message.from_user.id
    lan = database.query_language_data(5171051870)
    if lan == 0:
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
                user_choice: [CallbackQueryHandler(select_function)],
                Approach: [CallbackQueryHandler(approach)],
                confirmsend_photo: [MessageHandler(filters.PHOTO & ~filters.COMMAND, confirm_photo)],
                put_money: [MessageHandler(filters.TEXT & ~filters.COMMAND, putmoney)],
                withdraw_money: [MessageHandler(
                    filters.TEXT & ~ filters.COMMAND, withdraw)],
                # update_money: [MessageHandler(filters.TEXT, updatemoney)],
                confirmsend: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm)],
                send_money: [MessageHandler(filters.TEXT & ~filters.COMMAND, sendmoney)],
                # transaction: [MessageHandler(filters.TEXT, trans)],
                setting: [CallbackQueryHandler(set_up)],
                changepassword: [MessageHandler(filters.TEXT & ~filters.COMMAND, change_password)],
                score: [MessageHandler(filters.TEXT & ~ filters.COMMAND, gift)],
                change_language: [MessageHandler(filters.TEXT & ~ filters.COMMAND, changelan)],
                qrcode: [MessageHandler(filters.PHOTO, qr)],
            },
            fallbacks=[CommandHandler("Cancel", cancel)],
        )
        return conv_handler
    elif lan == 1:
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("ewallet", start)],
            states={
                choice_en: [CallbackQueryHandler(register_or_login_en)],
                refcode_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, ref_code_en)],
                # username_signin_en: [MessageHandler(filters.TEXT, usern_en)],
                # password_signin_en: [MessageHandler(filters.TEXT, password_en)],
                success_login_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, success_log_en), CommandHandler("skip", skip_en)],
                # password_register_en: [MessageHandler(filters.TEXT, password_regis_en)],
                success_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, sucess_def_en), CommandHandler("skip", skip_en)],
                main_menu_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, mainmenu_en)],
                user_choice_en: [CallbackQueryHandler(select_function_en)],
                Approach_en: [CallbackQueryHandler(approach_en)],
                confirmsend_photo_en: [MessageHandler(filters.PHOTO & ~filters.COMMAND, confirm_photo_en)],
                put_money_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, putmoney_en)],
                withdraw_money_en: [MessageHandler(
                    filters.TEXT & ~ filters.COMMAND, withdraw_en)],
                # update_money_en: [MessageHandler(filters.TEXT, updatemoney_en)],
                confirmsend_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_en)],
                send_money_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, sendmoney_en)],
                # transaction_en: [MessageHandler(filters.TEXT, trans_en)],
                setting_en: [CallbackQueryHandler(set_up_en)],
                changepassword_en: [MessageHandler(filters.TEXT & ~filters.COMMAND, change_password_en)],
                score_en: [MessageHandler(filters.TEXT & ~ filters.COMMAND, gift_en)],
                change_language_en: [MessageHandler(filters.TEXT & ~ filters.COMMAND, changelan_en)],
                qrcode_en: [MessageHandler(filters.PHOTO, qr_en)],
            },
            fallbacks=[CommandHandler("Cancel", cancel)],
        )
        return conv_handler


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("/ewallet: Mở ví điện tử\n/skip: Thoát khỏi ví điện tử\nTham gia kênh hỗ trợ của chúng tôi để nhận được những lời tư vấn đỉnh cao nhất (https://t.me/+ArWxOYbmSRdmNzA1m)")
    return ConversationHandler.END


async def aboutus(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    photo_file = 'public/images/2.png'
    await update.message.reply_photo(photo_file)
    await update.message.reply_text('A Potato là một bot ví điện tử xử của Telegram được phát triển và làm màu bởi nhóm 4 với CEO Đỗ Hiếu. Để hiểu rõ hơn về chúng tôi, các bạn có thể đọc link sau đây: https://a-potato.notion.site/Hi-u-l-ai-eacb5d50b7aa4fe4a14b7cf231265aa9')
    return ConversationHandler.END


async def setting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lan_keyboard = language_keyboard()
    await update.message.reply_text("Chọn ngôn ngữ cần chuyển: ", reply_markup=lan_keyboard)
    return ConversationHandler.END
