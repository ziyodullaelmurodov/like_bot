from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from telegram.ext import Updater
likes = 0
dislikes = 0
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! \n" 
                              "👍 - Like \n"
                              "or\n"
                              "👎 - Dislike")
def handle_message(update: Updater, context: CallbackContext):
    global likes, dislikes
    if update.message.text in "👍👍🏻👍🏼👍🏽👍🏾👍🏿":
        likes += 1
        update.message.reply_text(f"💥Like: {likes}\n"f"💣Dislike: {dislikes}")
    elif update.message.text in "👎👎🏻👎🏼👎🏽👎🏾👎🏿":
        dislikes += 1
        update.message.reply_text(f"💥Like: {likes}\n"f"💣Dislike: {dislikes}")
    elif update.message.text in "😀😃😄😁😆🥹😅😂🤣":
        update.message.reply_text(f"Kulmang, faqat 👍 yoki 👎 yuboring!")
    else:
        update.message.reply_text("Faqat 👍 yoki 👎 yuboring!")
def main():
    TOKEN = "7963935887:AAGAtRooOT5l67tgxyk0BtSC9osHlRUCNa8"  
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main() 