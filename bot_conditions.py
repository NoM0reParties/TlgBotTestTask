import telebot

from models import SectionModel, GoodsModel


class Condition:

    def __init__(self, bot):
        self.bot = bot
        self.keyboard = telebot.types.InlineKeyboardMarkup()


class Freshman(Condition):

    def proceed_commands(self, message):
        continue_key = telebot.types.InlineKeyboardButton(text='Продолжить', callback_data='showcase_1')
        self.keyboard.add(continue_key)
        self.bot.send_message(message.chat.id, "Добрый день! Добро пожаловать в нашу кондитерскую!",
                              reply_markup=self.keyboard)


class Showcase(Condition):

    def proceed_commands(self, message, model):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        for section in SectionModel.select().where(SectionModel.showcase == model):
            section_key = telebot.types.InlineKeyboardButton(text=section.description, callback_data=f'section_{section.id}')
            self.keyboard.row(section_key)
        self.bot.send_photo(message.chat.id, open(model.picture_path, 'rb'), model.description,
                            reply_markup=self.keyboard)


class Section(Condition):

    def proceed_commands(self, message, model):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        for goods in GoodsModel.select().where(GoodsModel.section == model):
            section_key = telebot.types.InlineKeyboardButton(text=goods.description,
                                                             callback_data=f'goods_key_{goods.id}')
            self.keyboard.row(section_key)
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_showcase_1')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open(model.picture_path, 'rb'), model.description,
                            reply_markup=self.keyboard)


class Goods(Condition):

    def proceed_commands(self, message, model):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_id = model.section.id
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data=f'back_section_{back_id}')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open(model.picture_path, 'rb'), model.description,
                            reply_markup=self.keyboard)


def choose_condition(number):
    if number == 1:
        return Freshman
    elif number == 2:
        return Showcase
    elif number == 3:
        return Section
    elif number == 4:
        return Goods
