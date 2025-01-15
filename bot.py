from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# بوټ جوړ کړئ
async def start(update: Update, context):
    await update.message.reply_text("سلام! زه ستاسو بوټ یم. څنګه درسره مرسته کولی شم؟")

async def echo(update: Update, context):
    await update.message.reply_text(f"تاسو وویل: {update.message.text}")

if __name__ == "__main__":
    application = ApplicationBuilder().token("ستاسو_API_Token_دلته_واچوئ").build()

    # د کمانډ او پیغامونو لپاره هندلرونه اضافه کړئ
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # بوټ چالان کړئ
    application.run_polling()
