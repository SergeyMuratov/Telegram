import telebot
from telebot import types
from time import sleep
import math

bot = telebot.TeleBot('876987152:AAGKhUYvNNCeVwa9o8AohFKNm5q5_OEY3RE')

#Функция для определения пола ребенка
def man_or_girl(husband,wife):
    a = float(husband)
    b = float(wife)
    y = 2020

    m = float((y - a)/4)
    d = float((y - b)/3)

    if m > d:
        #Boy
        return True
    else:
        #Girl
        return False

@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, 'Данный бот может определить пол вашего будущего ребенка! и прочее описание...')

    print(m.from_user.first_name)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Начать', 'Продолжить']])
    bot.send_message(m.chat.id, 'Выберите:',
        reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def name(m):
    if m.text == 'Начать':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Главное меню']])
        bot.send_message(m.chat.id, 'Введите год рождения отца и через пробел матери, пример\n1986 1990',
            reply_markup=keyboard)
    elif m.text == 'Продолжить':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(m.chat.id, 'Функция в разработке',
            reply_markup=keyboard)
    elif m.text == 'Главное меню':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start(m)
    else:
        try:
            husband,wife = m.text.split(' ')
            rez = man_or_girl(husband,wife)

            if rez:
                msg = 'У вас будет мальчик поздравляем!'
            else:
                msg = 'У вас будет девочка поздравляем!'
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(advert) for advert in ['Главное меню']])

            bot.send_message(m.chat.id, msg,
                             reply_markup=keyboard)
        except:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(advert) for advert in ['Главное меню']])

            bot.send_message(m.chat.id, 'Вы ввели что-то неверно',
                             reply_markup=keyboard)




bot.polling()
