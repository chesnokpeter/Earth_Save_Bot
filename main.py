from telebot import types
import telebot
import random
import time
import datetime

bot = telebot.TeleBot("")

fact = [
    "🌳 Посадить дерево",
    "🕊 Построить скворечник",
    "🔥 Реже пользоваться кондиционером",
    "🚴‍♂️Больше ездить на велосипеде и ходить пешком",
    "🗑 Сортировать мусор",
    "💡 Раздавать и продавать ненужные вещи, уменьшая количество мусора",
    "🌿 Не повреждать и не рвать без нужды растения, не ломать ветки",
    "📄 Сдавать макулатуру",
    "📄 Писать на бумаге с двух сторон",
    "💦 Отключать воду во время мытья посуды и чистки зубов",
    "🔧 Устранить протечки в трубах",
    "🌵 Разводить комнатные растения",
    "🛍 Ходить за продуктами со своей тряпичной сумкой",
    "🛍 Отказаться от пластиковых пакетов",
    "⚡ Вынимать зарядное устройство из розетки, если оно не используется - это сократит расход электроэнергии",
    "🖇 Давать вещам вторую жизнь",
    "🔋 Утилизировать батарейки по всем правилам!\n\nИспользованные батарейки нельзя просто так выкинуть в мусорку.\n\nСобирайте их в отдельную коробочку, а потом относите в ближайший пункт приема старых батареек",
    "🧃 Приобретайте напитки в экологичной упаковке",
]


print('Бот работает!')

if __name__=='__main__':
    while True:
        try:

            @bot.message_handler(commands=['start'])
            def start_message(message):
                markup = types.ReplyKeyboardMarkup()
                button1 = types.KeyboardButton("Что такое окружающая среда 🌏?")
                button2 = types.KeyboardButton("Что я могу сделать для планеты 🌏?")
                button3 = types.KeyboardButton("Что такое чистая энергия ☘?")
                button4 = types.KeyboardButton("Как происходит внедрение чистой энергии ☘?")
                button5 = types.KeyboardButton("Классы опасных отходов 🍂")
                markup.add(button1, button2, button3, button4, button5)
                bot.send_message(message.chat.id, text='🤖 Привет, друг!\n\nЯ бот-помощник, который расскажет тебе про окружающую среду 🌏 и чистую энергию ☘\n\n✨ Выбирай интересующую тебя функцию!', reply_markup=markup)

            @bot.message_handler(commands=['about'])
            def about_message(message):
                bot.send_message(message.chat.id, "Этот бот создан для конкурса «Мир будущего - мир чистой энергии»\nНад проектом работал:\n\n<chesnok/> 🧑🏻‍💻 — Разработка, тестирование\n(@chesnokpeter)\n\nАнтон 👾 — Наставник\n(https://vk.com/a_d_elec)")

            @bot.message_handler(commands=['check'])
            def about_message(message):
                bot.send_message(message.chat.id, "Я работаю!")


            @bot.message_handler(content_types=['text'])
            def send_echo(message):
                if message.text == "Что такое окружающая среда 🌏?":
                    bot.send_message(message.chat.id, text='✏️ _Окружающая среда_ представляет собой совокупность условий, в которых всем жителям планеты *Земля* 🌏 приходится жить.\n\nПростыми словами, _окружающая среда_ - это *здоровье нашей планеты*.\n\nПо этой причине сохранять окружающую среду крайне важно!', parse_mode = 'Markdown')
                elif message.text == "Что я могу сделать для планеты 🌏?":
                    index = random.randint(1, len(fact) - 1)
                    bot.send_message(message.chat.id, text = fact[index])
                elif message.text == "Что такое чистая энергия ☘?":
                    bot.send_message(message.chat.id, text='✏️ _Чистая энергия_ – это энергия, которая поступает из возобновляемых ресурсов с нулевым уровнем выбросов, а также энергия, сэкономленная за счет мер по повышению энергоэффективности.\n\nЭта энергия не загрязняют атмосферу при использовании', parse_mode = 'Markdown')
                elif message.text == "Как происходит внедрение чистой энергии ☘?":
                    bot.send_message(message.chat.id, text='Внедрение чистой энергии происходит благодаря *увеличению прцента* использования возобновляемых ресурсов.\n\nВ современном мире известны следующие ресурсы возобновляемой энергии:\n\n ☀️ Солнечный свет\n 💦 Водные потоки\n 💨 Ветер\n 🌊 Приливы\n 🦠 Биотопливо (топливо из растительного сырья)\n 🔥 Геотермальная теплота (недра Земли)', parse_mode = 'Markdown')
                elif message.text == "Классы опасных отходов 🍂":
                    bot.send_photo(message.chat.id, 'https://cdn.discordapp.com/attachments/1086738361689067620/1107968492872929340/image.png')
                else:
                    bot.send_message(message.chat.id, text='Я не знаю такой команды 🧐')
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(datetime.datetime.now())
            print(e)
            time.sleep(5)
            continue