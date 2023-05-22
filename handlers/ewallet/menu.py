from telegram.ext import *
from telegram import *
import logging
import tracemalloc
from .variable import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    keyboard = [
        [
            InlineKeyboardButton("🔐 Đăng nhập", callback_data="Đăng nhập"),
            InlineKeyboardButton("📝 Đăng ký", callback_data="Đăng ký"),
        ],
        [
            InlineKeyboardButton("⚙️ Cài đặt", callback_data="Cài đặt"),
            InlineKeyboardButton("🤝 Hỗ trợ", callback_data="Hỗ trợ")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    photo_file = "public/images/APOTATO.png"
    await update.message.reply_photo(photo_file)
    await update.message.reply_text("Thêm @Silun_bot vào Telegram để mua, gửi và chuyển tiền trực tiếp trong Telegram. Biến nó thành ví tiền điện tử chính thức của bạn! Tham gia kênh của chúng tôi (https://t.me/apotatonews) để nhận thông tin cập nhật và khuyến mãi.", reply_markup=reply_markup)

    return choice

# selection choice in queue


async def register_or_login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    if update.callback_query.data == "Đăng nhập":
        await query.edit_message_text("Nhập mật khẩu: (Nhấn vào /skip để hủy)")
        return success_login
    elif update.callback_query.data == "Đăng ký":
        # await update.message.reply_text("Nhập mã giới thiệu (Nếu có (/skip)): ")
        await query.edit_message_text("Nhập mật khẩu: (Nhấn vào /skip để hủy)")
        return success
    elif update.callback_query.data == "Cài đặt":
        await query.edit_message_text("Đổi ngôn ngữ\n Đổi tiền tệ")
        return choice
    elif update.callback_query.data == "Hỗ trợ":
        await query.edit_message_text("Tham gia kênh hỗ trợ của chúng tôi để nhận được những lời tư vấn đỉnh cao nhất (https://t.me/+ArWxOYbmSRdmNzA1m)")
        return choice
    else:
        await update.message.reply_text("Đã hủy")
        return ConversationHandler.END
