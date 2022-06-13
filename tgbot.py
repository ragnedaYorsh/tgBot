#БОТ ТЕЛЕГРАМ-БОТ

import telebot
from pyowm import OWM
from pyowm.utils import config

config_dict = config.get_default_config_for_subscription_type('professional')
config_dict['language'] = 'ru' 

owm = OWM('0845827a57a1c6a439ae5c14f31b2ffc', config_dict)
bot = telebot.TeleBot("5238781398:AAHgviIUkTWcC7BK3DvbFNTplTtF24Rb3gA") # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):

# Search for current weather and get details
  mgr = owm.weather_manager()
  observation = mgr.weather_at_place(message.text)
  w = observation.weather
  temp = w.temperature('celsius')["temp"]

  answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
  answer += "Температура сейчас приблизительно " + str(temp) + "\n\n"

  if temp < 10:
    answer += "Пипец холодно, сиди дома ты чо!"
  elif temp < 20:
    answer += "Ну такое...Я бы на твоем месте дома сидел рил..."
  else:
    answer += "Вообще заебись...Хоть голым ходи)))"

  #bot.reply_to(message, message.text)
  bot.send_message(message.chat.id,answer) #чтобы бот не пересылал сообщения

bot.polling(none_stop = True)