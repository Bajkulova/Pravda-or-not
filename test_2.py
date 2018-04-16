from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler


def start(bot, update):
    update.message.reply_text("Есть в мире такие вещи, в которые сложно поверить, даже если они являются правдой. Сможете ли вы разобраться где выдумка, а где нет? /Да, с удовольствием /Нет, спасибо")

    # Это то число, которое является ключем в словаре states — втором параметре ConversationHandler'а.
    return 1

    # Оно указывает, что дальше на сообщения от этого пользователя должен отвечать обработчик states[1].

    # До этого момента обработчиков текстовых сообщений для этого пользователя не существовало,

    # поэтому текстовые сообщения игнорировались.


def first_response(bot, update):
    # Сохраняем ответ в словаре.
    update.message.reply_text('OK, тогда начинаем. Первый факт: \n'
                              'Писатель Марк Твен изобрёл и запатентовал застёжку для бюстгальтера\n'
                              '/Правда\n'
                              '/Ложь\n')
    return 2

def x_x(bot,update):
    update.message.reply_text('Правда. Марк Твен был не промах: и про Тома Сойера интересно писал, и на бюстгальтеры время оставалось.')
    return 2


def second_response(bot, update):

    update.message.reply_text("Так-с, следующий факт:\n"
                              "Блоха может разгоняться быстрее, чем космический шаттл\n"
                              "/Ложь\n"
                              "/Правда")
    return 3

def x_x_3(bot,update):
    update.message.reply_text('Правда. Блохи очень шустрые: во время прыжка они способны достичь умопомрачительной скорости — 8 сантиметров в миллисекунду. Каждый прыжок придаёт блохе ускорение, в 50 раз превышающее ускорение космического корабля.')
    return 3

def stop(bot, update):
    update.message.reply_text(

        "Жаль...всего доброго!")

    return ConversationHandler.END  # Константа, означающая конец диалога.


def tree_response(bot, update):

    update.message.reply_text("Итак, продолжим, новый факт:\n"
                              'Эверест - самая высокая гора на планете.\n'
                              '/Ложь\n'
                              '/Правда')
    return 4

def x_y(bot,update):
    update.message.reply_text('Ложь. Высота Эвереста 8 848 метров, но на Земле существует гора высотой в 10 203 метра. Это Мауна-Кеа на Гавайях. Ее подножие находится на дне океана и только 4 205 метров торчат на поверхности. На вершине горы находятся телескопы, так как это самая высокая точка Гавайев.')
    return 4

def four_response(bot, update):
    update.messege.reply_text('Ииии еще один фактик\n'
                              'Японцы - лидеры по продолжительности жизни.\n'
                              '/Ложь\n'
                              '/Правда')
    return 5

def x_y_2(bot,update):
    update.message.reply_text('Ложь. На самом деле пальму первенства тут удерживают жители княжества Монако. Продолжительность жизни тут 89,7 года. ‎Мужчины, как правило, живут в этой стране до 85,7 лет, женщины – до 93,7. Японцы же по этому показателю лишь на пятом месте, уступая Макао, Сан-Марино и Андорре.')
    return 5


def five_response(bot, update):
    update.messege.reply_text('У осьминога два сердца\n'
                              '/Правда\n'
                              '/Ложь')
    return 6

def x_y_2_2(bot, update):
    update.message.reply_text('Ложь. У осьминога целых три сердца, девять мозгов, восемь щупалец и голубая кровь.')
    return 6

def six_response(bot, update):
    update.messege.reply_text('Отправляясь на обед, самка бегемота находит няньку для своего детеныша\n'
                              '/Правда\n'
                              '/Ложь')
    return 7

def x_y_z(bot, update):
    update.message.reply_text('ПРАВДА. В каждом стаде бегемотов есть своего рода детский сад, где пасутся самки и детеныши. Покидая своего малыша на какое-то время, мать оставляет его под присмотром других самок.')
    return 7

def seven_response(bot, update):
    update.messege.reply_text('Верблюды во время странствий по пустыне хранят запас воды в своих горбах\n'
                              '/Правда\n'
                              '/Ложь')
    return 8

def x_y_z_2(bot, update):
    update.message.reply_text('НЕТ. Их горбы на самом деле наполнены салом, за счет которого верблюды живут при недостатке или полном отсутствии пищи.')
    return 8


def ccc(bot, update):
    update.messege.reply_text('Надеюсь, ты узнал что-то новое сегодня. Ну, а если ты не сделал ни одной ошибки, то вероятно ты очень любознательный')
    return ConversationHandler.END


def main():
    # Создаем объект updater. Вместо слова "TOKEN" надо разместить полученнй от @BotFather токен

    updater = Updater("501086201:AAEQvsdUVjeuh-4FFR3u7JMTHeqaXsSuRSU")

    # Получаем из него диспетчер сообщений.

    dp = updater.dispatcher

    # Добавили словарь user_data в параметры.


    conv_handler = ConversationHandler(
        # Без изменений
        entry_points=[CommandHandler('start', start)],

        states={
            # Добавили user_data для сохранения ответа.
            1: [MessageHandler(Filters.text, first_response), CommandHandler('Нет, спасибо', stop)],
            2: [MessageHandler(Filters.text, second_response),CommandHandler('Ложь', x_x), CommandHandler('Правда', x_x)],
            3: [MessageHandler(Filters.text, tree_response), CommandHandler('Правда', x_x_2), CommandHandler('Ложь', x_x_2)],
            4: [MessageHandler(Filters.text, four_response),CommandHandler('Правда', x_y), CommandHandler('Ложь', x_y)],
            5: [MessageHandler(Filters.text, five_response), CommandHandler('Правда', x_y_2), CommandHandler('Ложь', x_y_2)],
            6: [MessageHandler(Filters.text, six_response), CommandHandler('Правда', x_y_2_2), CommandHandler('Ложь', x_y_2_2)],
            7: [MessageHandler(Filters.text, seven_response), CommandHandler('Правда', x_y_z),CommandHandler('Ложь', x_y_z)],
            8: [MessageHandler(Filters.text, ccc), CommandHandler('Правда', x_y_z_2), CommandHandler('Ложь', x_y_z_2)]

        },

        # Без изменений
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)

    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждем завершения приложения. (например, получение сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()