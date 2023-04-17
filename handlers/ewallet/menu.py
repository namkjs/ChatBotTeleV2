from telegram.ext import *
from telegram import *
import logging
import tracemalloc
from .variable import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    button1 = KeyboardButton('Đăng nhập')
    button2 = KeyboardButton('Đăng ký')
    button3 = KeyboardButton('Hủy')
    reply_keyboard = [[button1, button2, button3]]
    photo_file = "public/images/APOTATO.png"
    await update.message.reply_photo(photo_file)
    await update.message.reply_text(
        "Chương trình ví điện tử Appotato. Hãy thêm @Silun để thực hiện các chức năng hấp dẫn cùng Appotato.\n"
        "Thực hiện lựa chọn: ",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True
        ),
    )

    return choice

# selection choice in queue


async def register_or_login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    if text == "Đăng nhập":
        await update.message.reply_text("Nhập mật khẩu: (Nhấn vào /skip để hủy)")
        return success_login
    elif text == "Đăng ký":
        # await update.message.reply_text("Nhập mã giới thiệu (Nếu có (/skip)): ")
        await update.message.reply_text("Nhập mật khẩu: (Nhấn vào /skip để hủy)")
        return success
    else:
        await update.message.reply_text("Đã hủy")
        return ConversationHandler.END
