from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from hbt import TOKEN
from key_buttons import hp_button
from menu import hp_menu_keyboard

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgIAAxkBAAEGcXxjdQt_0Bj2ksv1Lr0-3CxUhaVdhwACoQMAAvJ-ggyAOwNrOvMhLCsE'
    )
    update.message.reply_text(
        f"Добро пожаловать именинни(к\ца)) {update.effective_user.username}!\nВыберите чьё пожелания вы хотели бы прочитать?'",
        reply_markup=hp_menu_keyboard()
    )


HB_BUTTONS_A = hp_button[0]
HB_BUTTONS_E = hp_button[1]
HB_BUTTONS_UM = hp_button[2]
HB_BUTTONS_UL = hp_button[3]


def button1(update: Update, context: CallbackContext):
    update.message.reply_text(
"""
С днём рождения Апа! Желаю вам чтобы вы никогда не болели и были удачливой! 
Я вас очень люблю, живите долго и счястливо! И конечно же будте богатыми!
        """,
    reply_markup=hp_menu_keyboard()
    )


def button2(update: Update, context: CallbackContext):
    update.message.reply_text(
"""
Апа туулган кунунуз менен! Оорубаныз, маанайыныз эч качан бузулбасын, 
башка кундорлордун баарысы жакшы отсун, эчким мени урушпасын.
    """,
    reply_markup=hp_menu_keyboard()
    )

def button3(update: Update, context: CallbackContext):
    update.message.reply_text(
"""
Апа с днём рождения? Пожелать я вам ничего кроме здоровья не могу,
Так как пожелания это ничего кроме слов, но вот помочь не все смогут.
Я помогу вам с решением в хоть какой проблеме! Будьте счастливы!
    """,
    reply_markup=hp_menu_keyboard()
    )

def button4(update: Update, context: CallbackContext):
    update.message.reply_text(
"""
С днём рождения солнышко :3! 
    """,
    reply_markup=hp_menu_keyboard()
    )


updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HB_BUTTONS_A),
    button1
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HB_BUTTONS_UM),
    button2
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HB_BUTTONS_E),
    button3
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HB_BUTTONS_UL),
    button4
))

# updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()