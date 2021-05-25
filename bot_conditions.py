import telebot


class Condition:

    def __init__(self, bot):
        self.bot = bot
        self.keyboard = telebot.types.InlineKeyboardMarkup()


class Freshman(Condition):

    def proceed_commands(self, message):
        continue_key = telebot.types.InlineKeyboardButton(text='Продолжить', callback_data='continue')
        self.keyboard.add(continue_key)
        self.bot.send_message(message.chat.id, "Добрый день! Добро пожаловать в нашу кондитерскую!", reply_markup=self.keyboard)


class Showcase(Condition):

    def proceed_commands(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        section_key_1 = telebot.types.InlineKeyboardButton(text='Круассаны', callback_data='section_1')
        section_key_2 = telebot.types.InlineKeyboardButton(text='Пирожки', callback_data='section_2')
        section_key_3 = telebot.types.InlineKeyboardButton(text='Блины', callback_data='section_3')
        section_key_4 = telebot.types.InlineKeyboardButton(text='Торты', callback_data='section_4')
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел', callback_data='back')
        self.keyboard.row(section_key_1, section_key_2, section_key_3, section_key_4)
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/bakery_main.jpeg', 'rb'), "Выберите нужный раздел:",
                            reply_markup=self.keyboard)


class Section(Condition):

    def proceed_section_1(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        goods_key_1 = telebot.types.InlineKeyboardButton(text='Классический круассан', callback_data='goods_key_1')
        goods_key_2 = telebot.types.InlineKeyboardButton(text='Круассан с миндалем', callback_data='goods_key_2')
        goods_key_3 = telebot.types.InlineKeyboardButton(text='Круассан с шоколадом', callback_data='goods_key_3')
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел', callback_data='back')
        self.keyboard.row(goods_key_1)
        self.keyboard.row(goods_key_2)
        self.keyboard.row(goods_key_3)
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/croissant_main.jpg', 'rb'), "Круассаны для вашего кофе",
                            reply_markup=self.keyboard)

    def proceed_section_2(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        goods_key_4 = telebot.types.InlineKeyboardButton(text='Пирожок с капустой', callback_data='goods_key_4')
        goods_key_5 = telebot.types.InlineKeyboardButton(text='Пирожок с яйцом', callback_data='goods_key_5')
        goods_key_6 = telebot.types.InlineKeyboardButton(text='Пирожок с мясом', callback_data='goods_key_6')
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел', callback_data='back')
        self.keyboard.row(goods_key_4)
        self.keyboard.row(goods_key_5)
        self.keyboard.row(goods_key_6)
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/pies_main.jpg', 'rb'), "Свежайшие пирожки",
                            reply_markup=self.keyboard)

    def proceed_section_3(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        goods_key_7 = telebot.types.InlineKeyboardButton(text='Блинчик с лососем', callback_data='goods_key_7')
        goods_key_8 = telebot.types.InlineKeyboardButton(text='Классический блинчик', callback_data='goods_key_8')
        goods_key_9 = telebot.types.InlineKeyboardButton(text='Блинчик с ветчиной и сыром', callback_data='goods_key_9')
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел', callback_data='back')
        self.keyboard.row(goods_key_7)
        self.keyboard.row(goods_key_8)
        self.keyboard.row(goods_key_9)
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/pancake_main.jpg', 'rb'), "Блины на любой вкус",
                            reply_markup=self.keyboard)

    def proceed_section_4(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        goods_key_10 = telebot.types.InlineKeyboardButton(text='Киевский торт', callback_data='goods_key_10')
        goods_key_11 = telebot.types.InlineKeyboardButton(text='Птичье молоко', callback_data='goods_key_11')
        goods_key_12 = telebot.types.InlineKeyboardButton(text='Прага', callback_data='goods_key_12')
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел', callback_data='back')
        self.keyboard.row(goods_key_10)
        self.keyboard.row(goods_key_11)
        self.keyboard.row(goods_key_12)
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/cakes_main.jpg', 'rb'), "Торты для вашего праздника",
                            reply_markup=self.keyboard)


class Goods(Condition):

    def proceed_goods_1(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_croissant')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/classic.jpg', 'rb'), "Классический круассан",
                            reply_markup=self.keyboard)

    def proceed_goods_2(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_croissant')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/mondial.png', 'rb'), "Круассан с миндалем",
                            reply_markup=self.keyboard)

    def proceed_goods_3(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_croissant')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/chocolate.jpg', 'rb'), "Круассан с шоколадом",
                            reply_markup=self.keyboard)

    def proceed_goods_4(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_pie')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/cabbage_pie.jpg', 'rb'), "Пирожок с капустой",
                            reply_markup=self.keyboard)

    def proceed_goods_5(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_pie')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/egg_pie.jpg', 'rb'), "Пирожок с яйцом",
                            reply_markup=self.keyboard)

    def proceed_goods_6(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_pie')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/meat_pie.jpg', 'rb'), "Пирожок с мясом",
                            reply_markup=self.keyboard)

    def proceed_goods_7(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_pancake')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/salmon.jpg', 'rb'), "Блинчик с лососем",
                            reply_markup=self.keyboard)

    def proceed_goods_8(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_pancake')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/standard_pancake.jpg', 'rb'), "Классический блинчик",
                            reply_markup=self.keyboard)

    def proceed_goods_9(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_pancake')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/cheese_ham_pancake.jpg', 'rb'), "Блинчик с ветчиной и сыром",
                            reply_markup=self.keyboard)

    def proceed_goods_10(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_cake')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/kyiv.png', 'rb'), "Киевский торт", reply_markup=self.keyboard)

    def proceed_goods_11(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_cake')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/bird_milk.jpg', 'rb'), "Птичье молоко",
                            reply_markup=self.keyboard)

    def proceed_goods_12(self, message):
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        back_key = telebot.types.InlineKeyboardButton(text='Вернуться в предыдущий раздел',
                                                      callback_data='back_cake')
        self.keyboard.row(back_key)
        self.bot.send_photo(message.chat.id, open('images/prague.jpeg', 'rb'), "Прага", reply_markup=self.keyboard)
