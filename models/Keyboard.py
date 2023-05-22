from telegram.ext import *
from telegram import *


def menu_keyboard():
    button1 = KeyboardButton(
        'Nạp tiền ' + u'🤑')
    button2 = KeyboardButton('Cập nhật số dư ' + u'💳')
    button3 = KeyboardButton('Chuyển tiền ' + u'📤')
    button4 = KeyboardButton('Lịch sử giao dịch ' + u'📊')
    button6 = KeyboardButton('Đổi quà ' + u'🎁')
    button5 = KeyboardButton('Cài đặt ' + u'⚙️')
    button7 = KeyboardButton('Về chúng tôi')
    # create KeyboardButton objects for each line

    reply_keyboard = [[button1], [button2],
                      [button3], [button4], [button6], [button7], [button5]]
    return reply_keyboard


def start_keyboard():
    button1 = KeyboardButton('Đăng nhập')
    button2 = KeyboardButton('Đăng ký')
    button3 = KeyboardButton('Hủy')
    reply_keyboard = [[button1, button2, button3]]
    return reply_keyboard


def keyboard_setting():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔐 Đổi mật khẩu", callback_data="Đổi mật khẩu"),
            InlineKeyboardButton(
                "🌐 Đổi ngôn ngữ", callback_data="Đổi ngôn ngữ"),
        ],
        [
            InlineKeyboardButton(
                "🔠 Xem số tài khoản | Mã giới thiệu", callback_data="Xem số tài khoản"),
        ],
        [
            InlineKeyboardButton("🔗 Mã QR",
                                 callback_data="Mã QR"),
        ],
        [
            InlineKeyboardButton("↩️ Quay lại", callback_data="Quay lại"),
        ],
        [
            InlineKeyboardButton("🔒 Đăng xuất", callback_data="Đăng xuất"),
        ]
    ]
    return keyboard


def inline_keyboard_menu():
    keyboard = [
        [
            InlineKeyboardButton("➕ Nạp tiền", callback_data="Nạp tiền"),
            InlineKeyboardButton("💸 Rút tiền", callback_data="Rút tiền"),
        ],
        [
            InlineKeyboardButton("📤 Chuyển tiền", callback_data="Chuyển tiền"),
        ],
        [
            InlineKeyboardButton("📊 Lịch sử giao dịch",
                                 callback_data="Lịch sử giao dịch"),
        ],
        [
            InlineKeyboardButton("🎁 Đổi quà", callback_data="Đổi quà"),
        ],
        [
            InlineKeyboardButton("⚙️ Cài đặt", callback_data="Cài đặt"),
        ]
    ]
    return keyboard
