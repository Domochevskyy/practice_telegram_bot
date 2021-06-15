import detection
import os
import telebot
import time

from config import TOKEN

bot = telebot.TeleBot(token=TOKEN, parse_mode='Markdown')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = 'Вас привестствует тестовый бот Николая Медного.'
    bot.send_message(message.from_user.id, text=text)


@bot.message_handler(commands=['about'])
def send_about(message):
    text = 'Бот определяет количество объектов на фотографии и детектирует эти объекты'
    bot.send_message(message.from_user.id, text=text)


@bot.message_handler(content_types=['text'])
def text_answer(message):
    text = 'Я пока не умею разговаривать с людьми, могу принимать только фотографии'
    bot.reply_to(message=message, text=text)


@bot.message_handler(content_types=['photo'])
def receive_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_photo = bot.download_file(file_info.file_path)

    with open(f"one.jpg", "wb") as file:
        file.write(downloaded_photo)

    text = "Сейчас мы посмотрим, что у Вас на фотографии\n" \
           "Только немного подождите..."
    bot.send_message(chat_id=message.chat.id, text=text)

    result = detection.get_object_detection()

    with open("two.jpg", 'rb') as new_file:
        bot.send_photo(chat_id=message.chat.id, photo=new_file)

    text = f"Найдено {result} объектов"
    bot.send_message(chat_id=message.chat.id, text=text)

    os.remove('one.jpg')
    os.remove('two.jpg')


def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            print(error)
        time.sleep(10)


if __name__ == "__main__":
    main()
