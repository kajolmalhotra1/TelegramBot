from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5391356157:AAHwoxmFv6GnHk4vTSno_Wk2jdaqNrLei_I", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello mam, Welcome to the Bot.Please write\/help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/youtube - To get the youtube URL
	/linkedin - To get the LinkedIn profile URL
	/gmail - To get gmail URL
	/geeks - To get the GeeksforGeeks URL""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("Your gmail link =>\https://mail.google.com/mail/u/1/#inbox")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("LinkedIn URL => \https://www.linkedin.com/in/kajolmalhotra")


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text("GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

def shutdown():
    updater.stop()
    updater.is_idle = False
def stop(bot, update):
    threading.Thread(target=shutdown).start()
def main():
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('stop', stop))
    updater.bot.send_message(chat_id=settings.my_id, text="Here is a message from the bot")
    updater.start_polling()
    print("Bot is waiting for user input")
    updater.idle()
print("Last row is reached")
updater.start_polling()
updater.idle()
updater.stop()
