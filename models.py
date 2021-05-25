import peewee

from bot_conditions import Freshman, Section, Showcase, Goods

db = peewee.SqliteDatabase('bakery_users.db')


class Condition(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db


class BakeryUser(peewee.Model):
    user_id = peewee.CharField()
    condition = peewee.ForeignKeyField(Condition, related_name='cond')

    class Meta:
        database = db


def choose_condition(number):
    if number == 1:
        return Freshman
    elif number == 2:
        return Showcase
    elif number == 3:
        return Section
    elif number == 4:
        return Goods
