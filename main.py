import telebot.types
from Texts import *
from keyboards import *
import re
from config import *
from seatable_api import Base
from telebot import types

TOKEN = "6006927963:AAE432VmnRy23a1YQw8fyhrA2nKpCnRB4o0"
#TOKEN = "1294819792:AAEfufqcwDhkBkMDQ0_W8SMc_i23NnQkGpM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    request = ('select User_ID from Main where User_ID = %s' % message.chat.id)
    check = base.query(request)
    if len(check) > 0:
        print("Это старый пользователь!")

    else:
        print("Пользователь НЕ найден")
        row_data = {
            "User_ID": "%s" % message.chat.id,
            "User_state": "Starting",
            "User_FirstName": "%s" % message.from_user.first_name,
            "User_LastName": "%s" % message.from_user.last_name,
            "User_Username": "%s" % message.from_user.username,
        }
        base.append_row('Main', row_data)

    bot.send_photo(message.chat.id, "https://imgur.com/a/Mlx3e1j","Добрый день! \n"
"Это бот предзаписи на вебинар «Внешний трафик для маркетплейсов» от Анастасии Лапай и Андрея Брицко."
"\n"
"\n"                                      
"*КТО МЫ?*\n"
"○ Авторы практических курсов и личных наставничеств\n"
"○ Знаем, как запускать прибыльные проекты на маркетплейсах\n"
"○ Делимся навыками экологичного бизнеса\n"
"○ Даём инструкции и стратегии\n"
"\n"
"Анастасия Лапай\n"
"○ Основатель агентства по продвижению товаров на маркетплейсах StepUp\n"
"○ Более 7 лет опыта в маркетинге\n"
"\n"
"Андрей Брицко\n"
"○ 19 лет работаю с Китаем\n"
"○ Помогаю наладить работу с Китаем от поиска поставщиков до эффективного открытия производства продукции\n"
"\n"
"Если хочешь получить гайд для роста продаж - записывайся на вебинар и забирай подарок.", parse_mode='Markdown',reply_markup=start_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call.data)
    if call.data == 'start_ok':

        #bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Введите ваше имя!")
        base.query('update Main set User_state = "Name" where User_ID = %s' % call.message.chat.id)

    if call.data == 'newsletter_48':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_photo(value, "https://imgur.com/0Z5lUtP","У тебя осталось 48 часов!")
                bot.send_message(value, "По статистике, люди которые внедряют в работу новые знания в первые 72 часа после их получения - делают результаты. Остальные просто забывают и продолжают поступать как привыкли. А вы уже что-то применили в бизнесе?\n\n"
                    "Прочитать и отложить на потом - верный способ не применить информацию никогда.\n\n"
                    "Например, вы уже посмотрели гайд? Отметили что сможете применить в бизнесе?"
                    "Мы, авторы этого гайда, сразу после обучения или получения новой информации находим 1-2 действия, которые внедряем в работу. И это помогает бизнесу расти.\n\n"
                    "Подробнее о том, как гарантированно получить результат от обучения, мы рассказали в посте на нашем канале: https://t.me/BritskoLapay/51")

    if call.data == 'newsletter_3days':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_message(value, "Когда пора делать внешнюю рекламу для товаров на маркетплейсах? И какую - блогеры, таргет, контекст? А вы к ней готовы?\n\n"
                                        "'Страшно сделать рекламу и не получить от нее отдачи' - частая проблема у селлеров.\n"
                                        "Но без рекламы и трафика карточка может висеть бесконечно долго, товар будет лежать на складе и вместо прибыли приносить убытки."
                                        "Можно пробовать привлечь людей по бартеру, но это занимает много времени и тоже не понятно, с чего начать, кому предлагать.\n\n"
                                       "А хотелось бы иметь понятные критерии эффективности и прогноз, какую отдачу даст реклама, чтобы не уйти в минус.\n\n"
                                        "9 апреля в 19:00 на вебинаре «Внешний трафик для маркетплейсов» Анастасия расскажет, как выбрать блогера или канал для рекламы, и подскажет, на что обратить внимание в карточке товара, чтобы аудитория не просто пришла, но еще и купила.")

                bot.send_message(value,"Самые частые ошибки в этой зоне почти у всех одинаковые. Мы собрали их в пост и разбираем в канале.\n\n"
                                            "Присоединяйтесь! Заодно проверите себя, что вы совершили, а что смогли предотвратить.", reply_markup=InlineKeyboardMarkup([
                                            [InlineKeyboardButton(text='Подписаться на канал', url='https://t.me/BritskoLapay/51')],]))

    if call.data == 'newsletter_tomorrow':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_message(value,"*Нет трафика - нет продаж!*"
                                            "*Правда ли это?* И где брать трафик селлерам и тем, у кого нет бюджета на маркетолога?\n\n"
                                            "Завтра в 19:00 на вебинаре 'Маркетинг для селлеров' Анастасия Лапай и Андрей Брицко расскажут все о том, как работать с аудиторией и где ее брать.\n\n"
                                            "Анастасия работала в маркетинге 7 лет и на опыте успешных кейсов разберет варианты привлечения трафика и как сделать так, чтобы люди покупали, а не просто смотрели и клали в корзину.\n\n"
                                            "Вебинар будет полезен всем, кто занимается продажами, не обязательно только на маркетплейсах. Ведь проблемы трафика, слитых бюджетов и оценки эффективности рекламы у всех общие.\n"
                                            "Вы получите жирную пользу и уйдете с понятым алгоритмом для привлечения аудитории на ваш товар.\n\n"
                                            "*Ссылку вышлем за час до вебинара.*\n"
                                            "Готовьте ваши вопросы! Мы выделим время, чтобы поотвечать на них во время трансляции.\n"
                                            "Запланируйте около 2х часов на вебинар.\n\n"
                                            "До встречи!", parse_mode='Markdown')

    if call.data == 'newsletter_today':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_message(value,"Почему реклама всегда такая непредсказуемая и как считать прогноз ее эффективности, чтобы не слить бюджет?\n"
                                            "Расскажем сегодня в 19.00 на вебинаре «Внешний трафик для маркетплейсов».\n\n"
                                            "Через час начинаем!\n"
                                            "Подготовили вопросы?\n\n"
                                            "Ссылка на трансляцию ниже!", reply_markup=InlineKeyboardMarkup([
                                            [InlineKeyboardButton(text='Ссылка на трансляцию', url='https://t.me/BritskoLapay/51')],]))

    if call.data == 'newsletter_15':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_message(value,"Начинаем через 15 минут!\n\n"
                                            "Подготовьте 2 часа времени, блокнот, ручки и ваше внимание :)")

    if call.data == 'newsletter_started':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_message(value,"Мы начали! Подключайтесь!", reply_markup=InlineKeyboardMarkup([
                                            [InlineKeyboardButton(text='Ссылка на трансляцию', url='https://t.me/BritskoLapay/51')],]))

    if call.data == 'newsletter_started2':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_message(value,"Уже разбираем первые кейсы и примеры, почему рекламы не работает.\n\n"
                                            "Если вы не с нами - самое время подключиться.\n\n"
                                            "Будет только мясо, никакой воды и продаж.", reply_markup=InlineKeyboardMarkup([
                                            [InlineKeyboardButton(text='Ссылка на трансляцию', url='https://t.me/BritskoLapay/51')],]))

    if call.data == 'newsletter_after':
        ads_users = base.query('select User_ID from Main')
        for i in ads_users:
            for value in i.values():
                bot.send_message(value,"Вебинар закончился, успевайте его посмотреть в течении трех дней!\n"
                                            "Дальше запись станет платной.\n\n"
                                            "Выделите 2 часа сейчас, чтобы увеличить эффективность вашей рекламы и отдачу от нее в несколько раз!\n\n"
                                            "Повтора вебинара не будет, а упущенная польза может стать успехом у ваших конкурентов.\n\n"
                                            "Запись вебинара по ссылке и доступна до 13 апреля."
                                            , reply_markup=InlineKeyboardMarkup([
                                            [InlineKeyboardButton(text='Ссылка на трансляцию', url='https://t.me/BritskoLapay/51')],]))

@bot.message_handler(content_types=['text'])
def name_handling(message):
    user_state = base.query('select User_state from Main where User_ID = %s' % message.chat.id)
    print(user_state)

    if user_state == [{'User_state': 'Admin'}]:
        bot.send_message(message.chat.id, "ыыыыы", reply_markup=admin_inline())

    if user_state == [{'User_state': 'Name'}]:
        base.query('update Main set User_RealName = "{name}" where User_ID = {ID}'.format(
                             name=message.text, ID=message.chat.id))
        base.query('update Main set User_state = "Email" where User_ID = %s' % message.chat.id)
        bot.send_message(message.chat.id, "%s, спасибо!" % message.text)
        bot.send_message(message.chat.id, "Введите email")


    if user_state == [{'User_state': 'Email'}]:
        base.query('update Main set User_email = "{email}" where User_ID = {ID}'.format(
            email=message.text, ID=message.chat.id))
        base.query('update Main set User_state = "Phone" where User_ID = %s' % message.chat.id)
        bot.send_message(message.chat.id, "Осталось немного! Введите номер телефона.\n"
                                                "Обещаем не звонить, дышать в трубку тоже не будем.")

    if user_state == [{'User_state': 'Phone'}]:
        base.query('update Main set User_phone = "{phone}" where User_ID = {ID}'.format(
            phone=message.text, ID=message.chat.id))
        base.query('update Main set User_state = "AllDone" where User_ID = %s' % message.chat.id)
        bot.send_message(message.chat.id, "Супер! Спасибо!\n"
                                          "Встречаемся 9 апреля в 19:00 по мск. Ссылку на вебинар пришлем позже.\n \n"
                                           "Гайд для роста продаж ниже. Забирайте и внедряйте сразу после прочтения!")
        bot.send_message(message.chat.id, "***********Здесь будет гайд*********")





if __name__ == '__main__':
     bot.polling(none_stop=True, interval=0)