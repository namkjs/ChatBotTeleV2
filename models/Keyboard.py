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
