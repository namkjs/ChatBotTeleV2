
from .function_en import *


async def approach_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if update.callback_query.data == 'Số tài khoản':
        await query.edit_message_text("Nhập số tài khoản muốn chuyển: ")
        return confirmsend_en
    elif update.callback_query.data == 'Mã QR':
        await query.edit_message_text("Nhập mã QR: ")
        return confirmsend_photo_en


async def confirm_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
            a = a+1
            break
    if a > 0:
        await update.message.reply_text("Nhập số tiền muốn chuyển: ",
                                        reply_markup=ReplyKeyboardMarkup(
                                            reply_keyboard, resize_keyboard=True,  selective=True
                                        ),
                                        )
        return send_money_en
    else:
        await update.message.reply_text("Tên người dùng không hợp lệ. Vui lòng thực hiện lại", reply_markup=menu_keyboard)
        return user_choice_en


async def confirm_photo_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global receiver
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("user_photo.jpg")
    receiver = str(read_qr_code(update, context))
    os.remove("user_photo.jpg")

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
                                            reply_keyboard, resize_keyboard=True,  selective=True
                                        ),
                                        )
        return send_money_en
    else:
        await update.message.reply_text("Tên người dùng không hợp lệ. Vui lòng thực hiện lại", reply_markup=menu_keyboard)
        return user_choice_en


async def sendmoney_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = database.query_balance_data(context.user_data["username"])
    balance = result[3]
    money = str(update.message.text)
    if money.isnumeric() == False:
        await update.message.reply_text("Số tiền không hợp lệ. Vui lòng nhập lại số tiền: ")
        return confirmsend_en
    else:
        money = int(update.message.text)
    if money < 0:
        await update.message.reply_text("Số tiền không hợp lệ. Vui lòng nhập lại số tiền: ")
        return confirmsend_en
    elif money > balance:
        await update.message.reply_text("Số dư trong tài khoản không khả dụng! Vui lòng nạp thêm tiền và thực hiện lại: ", reply_markup=menu_keyboard)
        return confirmsend_en
    else:
        global receiver
        database.send(context.user_data["username"], receiver, balance, money)
        # trans = str(str(current_time) + ": " + str(-money))
        # trans_receive = str(str(current_time) + ": +" + str(money))
        day = datetime.datetime.today().strftime('%d-%m-%Y')
        time = datetime.datetime.today().strftime('%H:%M:%S')
        fr = context.user_data["username"]
        user_database = dtb1(str(context.user_data["username"]))
        user_database.insert_user(day, time, -money, receiver)

        user_database1 = dtb1(receiver)
        user_database1.insert_user(day, time, money, fr)
# create KeyboardButton objects for each line
        results = database.query_balance_data(context.user_data["username"])
        balance = results[3]
        score_gif = results[5]

        await update.message.reply_text(f"✅<b>Chuyển tiền thành công</b>\n💰<b> Ví của bạn</b>\n<b>Số tài khoản</b>:{context.user_data['username']}\n<b>Số dư</b>: {balance} VND\n<b>Điểm thành viên:</b> {score_gif} ", reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
        return user_choice_en
