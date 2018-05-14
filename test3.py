import telebot

from telebot import types

TOKEN = "544595378:AAEVMfIyuC9_Ma_SLtW1XoWru84TY8f-W38"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Имя?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Приветствую, {name}. Выбери категорию.'.format(name=message.text))
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.row('a')
    markup.row('b')
    markup.row('c')
    markup.row('d')
    markup.row('e')
    bot.register_next_step_handler(message, category)


def category(message):
        if message.text == 'a':
            bot.send_message(message.chat.id, 'Ты выбрал категорию А'.format(name=message.text))
        elif  message.text == 'b':
            bot.send_message(message.chat.id, 'Ты выбрал категорию Б'.format(name=message.text))
        elif message.text == 'c':
            bot.send_message(message.chat.id, 'Ты выбрал категорию C'.format(name=message.text))
        elif message.text == 'e':
            bot.send_message(message.chat.id, 'Ты выбрал категорию Е'.format(name=message.text))
        elif message.text == 'd':
            bot.send_message(message.chat.id, 'Ты выбрал категорию Д'.format(name=message.text))
        else:
            bot.send_message(message.chat.id, 'Что то еще?'.format(name=message.text))


bot.polling(none_stop=True, interval=0)

