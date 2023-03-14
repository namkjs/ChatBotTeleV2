from telegram.ext import *
from telegram import *
import logging
import tracemalloc
from .variable import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [["Dang nhap", "Dang ky", "Cancel"]]

    await update.message.reply_text(
        "Chuong trinh vi dien tu cung Nam Le\n"
        "Lua chon cua ban: ",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Dang nhap or Dang ky"
        ),
    )
    return choice

# selection choice in queue


async def register_or_login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    if text == "Dang nhap":
        await update.message.reply_text("Username: ")
        return password_signin
    elif text == "Dang ky":
        await update.message.reply_text("Username: ")
        return password_register
    else:
        await update.message.reply_text("Da huy")
        return ConversationHandler.END
