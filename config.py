TOKEN = "6006927963:AAE432VmnRy23a1YQw8fyhrA2nKpCnRB4o0"
admin_id = 265350439
#265350439  - ya
#984468065 - anton
#718012110 - andrey
api_token = '1be934f2cb64c3ad2b7fbc7f4224919191c472fa'
server_url ='https://cloud.seatable.io'

ads_help = "После нажатия кнопки 'Сделать рассылку' следующие сообщения будут отправлены всем пользователям. " \
           "Можно прикреплять картинки. Нажмите кнопку 'Отмена рассылки' для выхода из этого режима"

poll_help = "Тут все максимально просто. Когда вы находитесь в обычном режиме, просто отправляйте боту опрос. " \
            "Он его пересобирает и отправляет от своего имени всем пользователям(не пересылает ваш опрос). " \
            "/result для просмотра результатов.   /resetpoll для очиски ВСЕЙ информации о предыдущем опросе. " \
            "Очищайте данные о старом опросе до создания следующего"

ban_help = "Не знаю, будет ли эта функция вообще использоваться, но если хотите кого-то забанить, перейдите в режим бана" \
           " (Кнопка 'Забанить кого то') и ответь на сообщение пользователя, которого следует забанить. Не забудьте " \
           "выйти из режима бана перед ответом на жалобы и вопросы! Для разбана перейди в режим разбана и напишите username пользователя"

questions_help = "Находясь в обычном режиме нажми ОТВЕТИТЬ на сообщение от пользователя и пишите свое сообщение"

def get_cell(a):
    for i in a:
        for value in i.values():
            result = value
    return result