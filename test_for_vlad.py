import telebot
import handlers

from SETTINGS import API_TOKEN, CALL_BACKS
from bot_conditions import Freshman, Showcase, Section, Goods
from models import BakeryUser, Condition, choose_condition

bot = telebot.TeleBot(API_TOKEN)
condition = Freshman(bot)


@bot.message_handler(commands=['start'])
def start_command(message):
    start_query = BakeryUser.filter(BakeryUser.user_id == f'{message.chat.id}')
    if start_query.exists():
        print('Yahoo')
    else:
        user_condition = Condition.get_by_id(1)
        BakeryUser.create(user_id=f'{message.chat.id}', condition=user_condition)
    current_user = BakeryUser.get(BakeryUser.user_id == f'{message.chat.id}')
    current_user.condition = Condition.get_by_id(1)
    current_user.save()
    current_condition = choose_condition(current_user.condition.id)(bot)
    current_condition.proceed_commands(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    current_user = BakeryUser.get(BakeryUser.user_id == f'{call.from_user.id}')
    handler = getattr(handlers, CALL_BACKS[call.data])
    handler(current_user, call, bot)


bot.polling()
