from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! زه ستا بوټ یم.")

if __name__ == "__main__":
    app = ApplicationBuilder().token("1095818301:AAEXh1vV3WsMf8Vxoy5aC6yslmIOGQ7_t_0").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

