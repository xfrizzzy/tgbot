import telebot
from telebot import types
token = "843870546:AAExK8Ah-1Iyp21w8kCBlDSMZbZD1HNSvhU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def any_msg(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="Список товаров", callback_data="first")
    second_button = types.InlineKeyboardButton(text="Информация", callback_data="second")
    keyboardmain.add(first_button)
    keyboardmain.add(second_button)
    bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":

        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        first_button = types.InlineKeyboardButton(text="Список товаров", callback_data="first")
        second_button = types.InlineKeyboardButton(text="Информация", callback_data="second")
        keyboardmain.add(first_button)
        keyboardmain.add(second_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Главное меню",reply_markup=keyboardmain)

    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="VIP чат (Неделя)", callback_data="1")
        rele2 = types.InlineKeyboardButton(text="VIP чат (Месяц)", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="VIP чат (6 месяцев)", callback_data="3")
        rele4 = types.InlineKeyboardButton(text="Экспресс", callback_data="4")
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="mainmenu")
        keyboard.add(rele1)
        keyboard.add(rele2)
        keyboard.add(rele3)
        keyboard.add(rele4)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите товар для покупки",reply_markup=keyboard)

    elif call.data == "second":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="О проекте", callback_data="info")
        rele2 = types.InlineKeyboardButton(text="Ответы на вопросы", callback_data="quest")
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="mainmenu")
        keyboard.add(rele1)
        keyboard.add(rele2)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="????",reply_markup=keyboard)

    elif call.data == "info":

        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="second")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Привет! Меня зоавут Василий Андреевич! Я создатель проекта kaverin_kk и это мой бот?? для упрощения связи с вами!'
                                   ' Если вы хотите максимально упростить свой заработок, то мой бот готов помочь 24/7 !) Если же вы не доверяете роботам, то всегда можете написать мне лично!) '
                                   'Всем удачи и побольше деньжат!??',
                              reply_markup=keyboard)

    elif call.data == "quest":

        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="second")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='\nВопрос: ФЫвфывфыв фвыфвыфв?'
                                   '\nОтвет: Фафыафыафыаыфафыафыафыафыафыа'
                                   '\n'
                                   '\nВопрос: ФЫjcdgdfg фвwefsdfв?'
                                   '\nОтвет: 123asfasfа'
                                   '\n'
                                   '\nВопрос: ФЫjcdgdfg фвwefsdfв?'
                                   '\nОтвет: 123asfasfа'
                                   '\n',
                              reply_markup=keyboard)


    elif call.data == "5" or call.data == "6" or call.data == "7":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="alert")
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="lastlayer", callback_data="ll")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="last layer",reply_markup=keyboard3)

    elif call.data == "1":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Перейти к оплате", url='https://1.ru')
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="first")
        keyboard.add(rele1)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Для совершения покупки "VIP чат (Неделя) - 800?" нажмите на кнопку "Перейти к оплате"', reply_markup=keyboard)

#________________________________________________________
    elif call.data == "2":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Перейти к оплате", url='https://2.ru')
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="first")
        keyboard.add(rele1)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Для совершения покупки "VIP чат (Месяц) - 1400?" нажмите на кнопку "Перейти к оплате"', reply_markup=keyboard)
# ________________________________________________________
    elif call.data == "3":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Перейти к оплате", url='https://3.ru')
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="first")
        keyboard.add(rele1)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Для совершения покупки "VIP чат (6 месяцев)- 5000?" нажмите на кнопку "Перейти к оплате"',
                              reply_markup=keyboard)

# ________________________________________________________
    elif call.data == "4":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Перейти к оплате", url='https://4.ru')
        backbutton = types.InlineKeyboardButton(text="??Назад", callback_data="first")
        keyboard.add(rele1)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Для совершения покупки "Экспресс - 2000?" нажмите на кнопку "Перейти к оплате"',
                              reply_markup=keyboard)




if __name__ == "__main__":
    bot.polling(none_stop=True)
