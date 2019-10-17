from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pystockfish  import *

from helpers import error

from settings import TOKEN, DEPTH



st_engine = Engine(depth=DEPTH)

# command handlers
def start(update, context):
    update.message.reply_text('Hello! I\'m telegram bot who can solve chess quizzes by FEN-string. Just send me one and get solving with info')


def help(update, context):
    update.message.reply_text('Everything you need it just sends FEN-string without any additional commands/info')


def handle_FEN(update, context):
    # TODO: Somehow valid FEN-string
    fen = update.message.text
    st_engine.setfenposition(fen)
    move_info = st_engine.bestmove()
    # TODO: Add more user-friendly message formating
    update.message.reply_text(f"According to FEN you sent: {fen}\n fen-to-image.com/image/{fen}\n Best move: {move_info['move']}\nPonder: {move_info['ponder']}\nAdditional info: {move_info['info']}")


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, handle_FEN))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
