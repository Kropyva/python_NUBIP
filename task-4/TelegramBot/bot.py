import json
import config
import telebot
import http.client
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


## Парсимо з серверу.
def update(first_part, second_part, country):
    global statistics
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "e18063930fmsh479c75bb05b434bp1e641bjsn49bf81d7ecdc",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()

    parsed_json = json.loads(data.decode("utf-8"))
    array = []

    if first_part:
        for i in parsed_json:
            array.append(i['Country'])
        return array

    if second_part:
        for i in parsed_json:
            if country in parsed_json[parsed_json.index(i)]["Country"]:
                statistics = (
                        "ID: " + str(parsed_json[parsed_json.index(i)]['id']) + '\n' +
                        "Rank: " + str(parsed_json[parsed_json.index(i)]['rank']) + '\n' +
                        "Country: " + str(parsed_json[parsed_json.index(i)]['Continent']) + '\n' +
                        "Two Letter Symbol: " + str(parsed_json[parsed_json.index(i)]['TwoLetterSymbol']) + '\n' +
                        "Three Letter Symbol: " + str(parsed_json[parsed_json.index(i)]['ThreeLetterSymbol']) + '\n' +
                        "Infection Risk: " + str(parsed_json[parsed_json.index(i)]['Infection_Risk']) + '\n' +
                        "Case Fatality Rate: " + str(parsed_json[parsed_json.index(i)]['Case_Fatality_Rate']) + '\n' +
                        "Recovery Proporation: " + str(
                    parsed_json[parsed_json.index(i)]['Recovery_Proporation']) + '\n' +
                        "Total Cases: " + str(parsed_json[parsed_json.index(i)]['TotalCases']) + '\n' +
                        "New Cases: " + str(parsed_json[parsed_json.index(i)]['NewCases']) + '\n' +
                        "Total Deaths: " + str(parsed_json[parsed_json.index(i)]['TotalDeaths']) + '\n' +
                        "New Deaths: " + str(parsed_json[parsed_json.index(i)]['NewDeaths']) + '\n' +
                        "Total Recovered: " + str(parsed_json[parsed_json.index(i)]['TotalRecovered']) + '\n' +
                        "New Recovered: " + str(parsed_json[parsed_json.index(i)]['NewRecovered']) + '\n' +
                        "Total Cases: " + str(parsed_json[parsed_json.index(i)]['ActiveCases']) + '\n' +
                        "Total Tests: " + str(parsed_json[parsed_json.index(i)]['TotalTests']) + '\n' +
                        "Population: " + str(parsed_json[parsed_json.index(i)]['Population']) + '\n' +
                        "One Case Every X PPL: " + str(
                    parsed_json[parsed_json.index(i)]['one_Caseevery_X_ppl']) + '\n' +
                        "One Death Every X PPL: " + str(
                    parsed_json[parsed_json.index(i)]['one_Deathevery_X_ppl']) + '\n' +
                        "One Test Every X PPL:" + str(parsed_json[parsed_json.index(i)]['one_Testevery_X_ppl']) + '\n' +
                        "Deaths 1M POP: " + str(parsed_json[parsed_json.index(i)]['Deaths_1M_pop']) + '\n' +
                        "Serious Critical: " + str(parsed_json[parsed_json.index(i)]['Serious_Critical']) + '\n' +
                        "Tests 1M POP: " + str(parsed_json[parsed_json.index(i)]['Tests_1M_Pop']) + '\n' +
                        "Total Cases 1M POP: " + str(parsed_json[parsed_json.index(i)]['TotCases_1M_Pop'])
                )
        return statistics


## Створюємо глобальні змінні.
step_back = 0
step_forward = 9

reserved_step_back = -39
reserved_step_forward = -48


## Функція для стоврення кнопок в чаті.
def make_markup(countries, isTrue, showButton):
    global step_back, step_forward, reserved_step_back, reserved_step_forward
    if isTrue and showButton:

        markup = types.InlineKeyboardMarkup(row_width=2)

        for i in countries[step_back: step_forward]:
            country = types.InlineKeyboardButton(i, callback_data=i)
            markup.add(country)

        forward = types.InlineKeyboardButton(">>>", callback_data=">>>")
        back = types.InlineKeyboardButton("<<<", callback_data="<<<")

        markup.add(back, forward)

        return markup
    elif isTrue:
        markup = types.InlineKeyboardMarkup(row_width=2)

        step_back += 9
        step_forward += 9
        reserved_step_back += 9
        reserved_step_forward += 9

        if step_back > 47:
            step_back = 0
            step_forward = 9
            reserved_step_forward = -48
            reserved_step_back = -39

        for i in countries[step_back: step_forward]:
            country = types.InlineKeyboardButton(i, callback_data=i)
            markup.add(country)

        forward = types.InlineKeyboardButton(">>>", callback_data=">>>")
        back = types.InlineKeyboardButton("<<<", callback_data="<<<")

        markup.add(back, forward)

        return markup
    else:
        markup = types.InlineKeyboardMarkup(row_width=2)
        step_back -= 9
        step_forward -= 9
        reserved_step_back -= 9
        reserved_step_forward -= 9

        if reserved_step_back <= -48:
            step_back = 38
            step_forward = 47
            reserved_step_forward = -10
            reserved_step_back = -1

        if reserved_step_back == -1:
            for i in countries[reserved_step_forward + 1:]:
                country = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(country)
        else:
            for i in countries[reserved_step_forward + 1: reserved_step_back + 1]:
                country = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(country)

        forward = types.InlineKeyboardButton(">>>", callback_data=">>>")
        back = types.InlineKeyboardButton("<<<", callback_data="<<<")

        markup.add(back, forward)

        return markup


## Старт бота.
@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_sticker = open('stickers/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, welcome_sticker)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Show information.")

    markup.add(item)

    bot.send_message(message.chat.id,
                     '''Welcome, {0.first_name}!\nMy name is <b>{1.first_name}</b>.\nI was created to inform you about Corona Virus statistics in Europe!'''.format(
                         message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup)


## Створюємо реакцію бота на повідомлення.
@bot.message_handler(content_types=['text'])
def show_message(message):
    if message.chat.type == 'private':
        countries = update(True, False, None)
        isTrue = True
        if message.text == "Show information.":
            isTrue = False

            bot.send_message(message.chat.id, "Choose the country:", reply_markup=make_markup(countries, True, True))

        for j in countries:
            if message.text == j:
                isTrue = False
                bot.send_message(message.chat.id, update(False, True, j))
        if isTrue:
            bot.send_message(message.chat.id, "This is not a European country or does not exist!")


## Функція для змінни візуальних кнопок в чаті.
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    countries = update(True, False, None)
    try:
        if call.message:
            for j in countries:
                if call.data == j:
                    info = update(False, True, j)
                    bot.send_message(call.message.chat.id, info)

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='You have chosen ' + j, reply_markup=None)

                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text='You have chosen ' + j)
                elif call.data == '<<<':

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Choose the country", reply_markup=make_markup(countries, False, False))
                    return

                elif call.data == '>>>':

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Choose the country", reply_markup=make_markup(countries, True, False))
                    return

    except Exception as e:
        print(repr(e))


## Запуск!
bot.polling(none_stop=True)
