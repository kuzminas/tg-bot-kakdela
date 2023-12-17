# модуль описывающий работу бота

import telebot
from random import randint

# @eekakdela_bot
token = '6858070579:AAF0ZEyd4m8wvRJv0R4MX3G-W3U-eaWJVqo' # токен бота

# возможные ответы
bot = telebot.TeleBot(token) # создаем бота
answers = ['Отлично!', 'Сегодня как-то тяжело, но терпимо...', 'Все хорошо, спасибо!']

# приветствие в ответ на /start
@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Спросите, как у меня "Как дела?", и я с удовольствием отвечу\n')


# обработка сообщения с текстом
@bot.message_handler(content_types=["text"])
def answer(message):
    question = message.text # текст сообщения
    if question.lower() == 'как дела?': # если спрашивают про дела
        idx = randint(0, len(answers)-1) # случайный номер ответа
        bot.send_message(message.chat.id, answers[idx])

