import telebot
from telebot import types

bot = telebot.TeleBot('1321264160:AAH3ATDdtQYxcgFwA_ibSpLGq-sN2AHhyN0')


# @bot.message_handler(commands=['gruppa'])
# def open_website(message):
# 	markup = types.InlineKeyboardMarkup()
# 	markup.add(types.InlineKeyboardButton("Bizning gruppa", url="https://t.me/iforlarolami"))
# 	bot.send_message(message.chat.id,
# 			"Gruppamizga azo boling yangiliklardan habardor bolib turing",
# 			parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "nivea":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('duxi')
        btn2 = types.KeyboardButton('qrem')
        btn3 = types.KeyboardButton('adikalon')
        btn4 = types.KeyboardButton('dezodarant')
        btn5 = types.KeyboardButton('posle britya')
        btn6 = types.KeyboardButton('nazad')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)


@bot.message_handler(commands='start')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('NIVEA')
    btn2 = types.KeyboardButton('CHANNEL')
    btn3 = types.KeyboardButton('DIOR')
    btn4 = types.KeyboardButton('AXE')
    btn5 = types.KeyboardButton('EXCITE')
    btn6 = types.KeyboardButton('AVON')
    btn7 = types.KeyboardButton('ORIFLAME')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    user = message.from_user
    if (user.last_name == None):
        send_mess = f"<b>Salom {message.from_user.first_name} </b>!\nSizni qanaqa mahsulotlar qiziqtiradi?"
    else:
        send_mess = f"<b>Salom {message.from_user.first_name} {message.from_user.last_name}</b>!\nSizni qanaqa mahsulotlar qiziqtiradi?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)