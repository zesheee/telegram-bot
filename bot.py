import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)


name = ''
surname = ''
patronym = ''
adres = ''
t = 0
job=''
age = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Как ваше имя?")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у вас фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Отчество?')
    bot.register_next_step_handler(message, get_patronym)


def get_patronym(message):
    global patronym
    patronym = message.text
    bot.send_message(message.from_user.id, 'Пожалуйста, укажите адрес проживания по прописке')
    bot.register_next_step_handler(message, get_adres)


def get_adres(message):
    global adres
    adres = message.text
    bot.send_message(message.from_user.id, 'Пожалуйста укажите температуру через точку \n Пример: 36.6')
    bot.register_next_step_handler(message, get_temperature)


def get_temperature(message):
    global t
    t = float(message.text)
    bot.send_message(message.from_user.id, 'Пожалуйста, укажите место вашей текущей работы')
    bot.register_next_step_handler(message, get_job)


def get_job(message):
    global job
    job = message.text
    bot.send_message(message.from_user.id, 'И ваш возраст')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    age = int(message.text)
    bot.send_message(message.from_user.id, 'Спасибо за сотрудничество!')

bot.polling()