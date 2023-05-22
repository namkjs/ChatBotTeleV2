from .function_en import *


async def putmoney_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    money = str(update.message.text)
    if money.isnumeric() == False:
        await update.message.reply_text("❗️ Số tiền không hợp lệ vui lòng nhập lại số tiền: ")
        return put_money_en
    else:
        money = int(update.message.text)
        if money < 0:
            await update.message.reply_text("❗️ Số tiền không hợp lệ vui lòng nhập lại số tiền: ")
            return put_money_en
        else:
            context.user_data["money"] = update.message.text
            result = database.query_balance_data(context.user_data["username"])
            balance = int(result[3])
            database.update_data(
                context.user_data["username"], context.user_data["money"], balance)
            results = database.query_balance_data(
                context.user_data["username"])
            balance = results[3]
            score_gif = results[5]

            await update.message.reply_text(f"✅ Nạp tiền thành công\n<b>💰 Ví của bạn</b>\n<b>Số tài khoản:</b> {context.user_data['username']}\n<b>Số dư:</b> {balance} VND\n<b>Điểm thành viên:</b> {score_gif} ",
                                            reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
            return user_choice_en


async def withdraw_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    results = database.query_balance_data(context.user_data["username"])
    balance = results[3]
    money = str(update.message.text)
    if money.isnumeric() == False:
        await update.message.reply_text("❗️ Số tiền không hợp lệ vui lòng nhập lại số tiền: ")
        return withdraw_money_en
    else:
        money = int(update.message.text)
        if money < 0:
            await update.message.reply_text("❗️ Số tiền không hợp lệ vui lòng nhập lại số tiền: ")
            return withdraw_money_en
        elif money > balance:
            await update.message.reply_text("Số dư không khả dụng. Vui lòng nhập lại số tiền: ")
            return withdraw_money_en
        else:
            result = database.query_balance_data(context.user_data["username"])
            balance = int(result[3])
            database.update_data(
                context.user_data["username"], -(money), balance)
            results = database.query_balance_data(
                context.user_data["username"])
            balance = results[3]
            score_gif = results[5]

            await update.message.reply_text(f"✅ Rút tiền thành công\n<b>💰 Ví của bạn</b>\n<b>Số tài khoản:</b> {context.user_data['username']}\n<b>Số dư:</b> {balance} VND\n<b>Điểm thành viên:</b> {score_gif} ",
                                            reply_markup=menu_keyboard, parse_mode=ParseMode.HTML)
            return user_choice_en
