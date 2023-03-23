import telebot
import random
f = open('PARIS.txt', 'r', encoding='UTF-8')
PARIS = f.read().split('\n')
f.close()
f = open('Neymar.txt', 'r', encoding='UTF-8')
Neymar = f.read().split('\n')
f.close()
f = open('MESSI.txt', 'r', encoding='UTF-8')
MESSI = f.read().split('\n')
f.close()
Mbappe_img = []
for i in range(10):
    image = open(f'M{i}.jpg', 'rb')
    Mbappe_img.append(image.read())
    image.close()
Neymar_img = []
for i in range(10):
    image = open(f'N{i}.jpg', 'rb')
    Neymar_img.append(image.read())
    image.close()
MESSI_img = []
for i in range(10):
    image = open(f'ME{i}.jpg', 'rb')
    MESSI_img.append(image.read())
    image.close()
bot = telebot.TeleBot('5912165398:AAGWzIeEscTsNHYjYyXP9OpsJV9Iy51pNjA')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Факт о команде Mbappe")
    item3 = telebot.types.KeyboardButton("фото Mbappe ")
    markup.add(item3)
    markup.add(item1)
    markup.row('Факт Neymar', 'Факт MESSI')
    markup.row('фото Neymar', 'фото MESSI')
    bot.send_message(m.chat.id,'Про какого футболиста из PARIS? Нажмите: \nMbappe, чтобы узнать факт о Mbappe' 
                              '\nMESSI, чтобы узнать факт о MESSI'
                              '\nNEYMAR JR, чтобы узнать факт о NEYMAR JR', reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт о команде Mbappe':
        answer = random.choice(PARIS)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'фото Mbappe':
        bot.send_photo(message.chat.id, random.choice(Mbappe_img))
    elif message.text.strip() == 'Факт Neymar':
        answer = random.choice(Neymar)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'фото Neymar':
        bot.send_photo(message.chat.id, random.choice(Neymar_img))
    elif message.text.strip() == 'Факт MESSI':
        answer = random.choice(MESSI)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'фото MESSI':
        bot.send_photo(message.chat.id, random.choice(MESSI_img))
bot.polling(none_stop=True, interval=0)



