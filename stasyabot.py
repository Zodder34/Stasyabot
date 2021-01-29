import telebot
bot = telebot.TeleBot("1628615137:AAGknur9YxXEaAr0DSf0pUU02pWU-8fDw34")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Твоё отношение к Стасе: хорошее/плохое ?: ")

@bot.message_handler(content_types=['text'])
def send_echo(message):


    a = message.text
    if a == "плохое":
        anwser = "ты не хороший человек, а Стася очень хорошая девочка" + "\n" + "удали себя в реальной жизни"
    elif a == "хорошее":
        anwser = "ты очень разумный человек, а Стася ещё более разумная"

    bot.send_message(message.chat.id, anwser)

bot.polling( none_stop = True)
