import telebot

bot = telebot.TeleBot('6914160058:AAHG9hvqqm239JJuHmc4kczbPXdvtQTCMU8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Напиши lyantik и ты узнаешь \n кто он . Также попробуй \n Z, vasya ,VZLOM',
                     parse_mode='Markdown')


@bot.message_handler(commands=['lyantik'])
def main(message):
    bot.send_message(message.chat.id, 'я родился:)', parse_mode='Markdown')


@bot.message_handler(commands=['Z'])
def main(message):
    bot.send_message(message.chat.id, '_Ты жак фреско_', parse_mode='Markdown')


@bot.message_handler(commands=['vasya'])
def main(message):
    bot.send_message(message.chat.id,
                     '*решите задачу: \n обЪем вписаного конуса \n 7 , найти площадь \n цилидра в котором \n он находится* ',
                     parse_mode='Markdown')


@bot.message_handler(commands=['VZLOM'])
def main(message):
    bot.send_message(message.chat.id, '*взлом твоей *********** начался . Отсчет 98%', parse_mode='Markdown')


bot.infinity_polling()