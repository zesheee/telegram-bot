
#from random import choice

#from emoji import emojize

#from mongodb import mdb, search_or_save_user, save_user_anketa, save_picture_name, save_file_id, save_like_dislike
#from utility import get_keyboard
#from utility import SMILE


# функция sms() будет вызвана пользователем при отправке команды start,
# внутри функции будет описана логика при ее вызове
def sms(bot, update):
    user = search_or_save_user(mdb, bot.effective_user, bot.message)  # получаем данные из базы данных
    print(user)
    smile = emojize(choice(SMILE), use_aliases=True)  # для ответа добавили emoji
    print('Кто-то отправил команду /start. Что мне делать?')  # вывод сообщения в консоль при отправки команды /start
    bot.message.reply_text('Здравствуйте, {}! \nПоговорите со мной {}!'
                           .format(bot.message.chat.first_name, smile), reply_markup=get_keyboard())  # отправляем ответ
