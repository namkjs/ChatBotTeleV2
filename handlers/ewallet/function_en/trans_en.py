from .function_en import *
import prettytable as pt


async def trans_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    table = pt.PrettyTable(['Ngày', 'Giờ', 'Tiền'])
    table.align['Ngày'] = 'l'
    table.align['Giờ'] = 'l'
    table.align['Tiền'] = 'r'
    user_database = dtb1(str(context.user_data["username"]))
    results = user_database.query_data()
    await update.message.reply_text("Lịch sử giao dịch là: ")
    for result in results:
        table.add_row([result[1], result[2], result[3]])
    update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)
    return user_choice_en
