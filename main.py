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
from cred import TOKEN
from key_buttons import tele_button, button
from menu import main_menu_keyboard, course_menu_keyboard

def record(update: Update, context: CallbackContext):
    text = update.message.text
    if text[:6] == 'htt' or '':
        context.bot.send_message(
            chat_id='-1001633827268',
            text=text
        )

def on_click(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="""
1) Напишите сообщение "Запись: " и ваше ФИО
2) Ваш номер телефона
3) Выберите удобное вам время
        """
    )

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgIAAxkBAAEGbY9jc3pO1zKHSoA-1YbgcXvzIXhnzQACcgADDzZdOZ_Pb3hTdrssKwQ'
    )
    update.message.reply_text(
        f"Добро Пожаловать {update.effective_user.username}",
        reply_markup=main_menu_keyboard()
    )

ABOUT = tele_button[0]
COURSE_MENU = tele_button[1]
BACK = button[3]
PYTHON = button[0]
JS = button[1]
UX_UI = button[2]
LOCATION = tele_button[2]
RECORD = button[4]


def resive_course_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите курс',
        reply_markup=course_menu_keyboard()
    )

def about(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Образовательное учреждение в котором люди любого возраста за короткие сроки могут получить качественное образование в сфере IT. Основная концепция OGOGO академии это дарить знания вместе с эмоциями, развивая не только технические навыки, но и личные качества наших студентов. Целью компании является взращивание новых конкурентоспособных IT специалистов для мирового рынка компьютерных технологий.',
        reply_markup=main_menu_keyboard()
    )

def nazad(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Вы вернулись в главное меню',
        reply_markup=main_menu_keyboard()
    )

def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        InlineKeyboardButton('Lesson', callback_data='python_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def js_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='js_mentor'),
        InlineKeyboardButton('Lesson', callback_data='js_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='js_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def ux_ui_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='ux_ui_mentor'),
        InlineKeyboardButton('Lesson', callback_data='ux_ui_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='ux_ui_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def location(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
            update.effective_chat.id,
            text = 'Location of OGOGO'
        )
    update.message.reply_location(
        #42.873646049273276, 74.61991206663981
        longitude=42.873646049273276,
        latitude=74.61991206663981,
        reply_to_message_id=msg.message_id
    )

def button_(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        
    ],
    [InlineKeyboardButton('Lesson', callback_data='python_lesson'),],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    if query.data == 'js_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/dima-evtushenko.jpg', 'rb'),
            caption = """
name: Dima
age: 17
expirience: 7 years
work place: doma
            """,
            reply_markup =reply_murkup
        )

    if query.data == 'js_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = "160000 som per month"
        )
    
    if query.data == 'js_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'Курсы с понедельника по пятницу, 5 раз в неделю. Курсы проходят в Огого Академии по адрессу Ибраимова 115/2, Бишкек'
        )
    
    if query.data == 'ux_ui_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/nursik.jpg', 'rb'),
            caption = """
name: Nursik
age: 16
expirience: 77 years
work place: в маке
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'ux_ui_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = "160000 som per month"
        )
    
    if query.data == 'ux_ui_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'Курсы с понедельника по пятницу, 5 раз в неделю. Курсы проходят в Огого Академии по адрессу Ибраимова 115/2, Бишкек'
        )

    if query.data == 'python_mentor':
        context.bot.send_photo(
            update.effective_chat.id,
            photo = open('img/ilias.jpg', 'rb'),
            caption = """
name: ILIIAAS
age: 16
expierence: 6 years
work place: Google, Microsoft, Facebook, Oazis
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'python_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = "16000 som per month"
        )
    
    if query.data == 'python_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'Курсы с понедельника по пятницу, 5 раз в неделю. Курсы проходят в Огого Академии по адрессу Ибраимова 115/2, Бишкек'
        )


updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_MENU),
    resive_course_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    nazad
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UX_UI),
    ux_ui_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RECORD),
    on_click
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    record
))

updater.dispatcher.add_handler(CallbackQueryHandler(button_))
updater.start_polling()
updater.idle()