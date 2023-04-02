from telegram.ext import *
from telegram import *
import logging
import tracemalloc

logger = logging.getLogger(__name__)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Chúc bạn một ngày vui vẻ", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
