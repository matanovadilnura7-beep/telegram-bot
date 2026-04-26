import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton("📄 Документ 1")
btn2 = KeyboardButton("📄 Документ 2")
markup.add(btn1, btn2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выбери документ:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle(message):
    if message.text == "📄 Документ 1":
        bot.send_document(message.chat.id, open("doc1.pdf", "rb"))
    elif message.text == "📄 Документ 2":
        bot.send_document(message.chat.id, open("doc2.pdf", "rb"))
    else:
        bot.send_message(message.chat.id, "Нажми кнопку")

bot.polling()