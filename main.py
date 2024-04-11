from my_token import token  # Импорт токена API
from my_functions import stop_words  # Импорт списка стоп-слов
import telebot

bot = telebot.TeleBot(token)

@bot.channel_post_handler(content_types=['text'])
def check_stop_words(message):
    message_text = message.text.lower()
    stop_words_lower = [word.lower() for word in stop_words]
    # Проверка наличия стоп-слова в тексте сообщения
    if any(stop_word in message_text for stop_word in stop_words_lower):
        try:
            bot.delete_message(message.chat.id, message.message_id)
            print("Сообщение удалено из-за наличия стоп-слова.")
        except Exception as e:
            print(f"Ошибка при удалении сообщения: {e}")

if __name__ == '__main__':
    bot.polling(none_stop=True)
